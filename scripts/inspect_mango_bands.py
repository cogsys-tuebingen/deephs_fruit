"""Inspect a few mango ENVI cubes and report band metadata.

Run this file directly with the deephs_env interpreter
(VS Code: Run Python File). It only reads the dataset and the
repository, then writes mango_band_inspection.txt beside this script.
"""

import ast
import json
import re
from collections import Counter
from pathlib import Path

import numpy as np
from spectral.io import envi

DATASET_ROOT = Path(r"D:\deephs_data\Mango_extracted\Mango")
PROJECT_DIR = Path(__file__).resolve().parent
REPORT_PATH = PROJECT_DIR / "mango_band_inspection.txt"
SAMPLES_PER_CAMERA = 2

# ENVI data-type codes. complex64/complex128 are included.
# complex256 is intentionally absent: spectral 0.23 calls
# np.dtype("complex256") inside SpyFile.load for every cube, and that
# dtype is not available in this NumPy build. Metadata still comes from
# envi.open; pixel values are read with np.fromfile.
ENVI_DATA_TYPES = {
    "1": np.dtype("u1"),
    "2": np.dtype("i2"),
    "3": np.dtype("i4"),
    "4": np.dtype("f4"),
    "5": np.dtype("f8"),
    "6": np.dtype("c8"),
    "9": np.dtype("c16"),
    "12": np.dtype("u2"),
    "13": np.dtype("u4"),
    "14": np.dtype("i8"),
    "15": np.dtype("u8"),
}

BAND_NAME = re.compile(r"band|wavelength|channel", re.IGNORECASE)
BAND_PHRASES = (
    re.compile(r"usable\s+bands?", re.IGNORECASE),
    re.compile(r"\b56\s+bands?\b", re.IGNORECASE),
    re.compile(r"band\s+selection", re.IGNORECASE),
    re.compile(r"selected\s+bands?", re.IGNORECASE),
    re.compile(r"bands?\s*(?:==|=|:)\s*56\b"),
)
SEARCH_SUFFIXES = {".py", ".json", ".md", ".yml", ".yaml", ".txt", ".cfg", ".ini", ".toml"}
SKIP_DIRS = {"__pycache__", ".git", ".venv", "venv"}


def envi_dtype(data_type, byte_order):
    """Map an ENVI data type and byte order to a NumPy dtype."""
    key = str(data_type).strip()
    if key not in ENVI_DATA_TYPES:
        raise ValueError(f"Unsupported ENVI data type: {data_type}")
    base = ENVI_DATA_TYPES[key]
    if base.itemsize == 1:
        return base
    order = "<" if int(byte_order) == 0 else ">"
    return base.newbyteorder(order)


def header_int(metadata, key):
    return int(str(metadata[key]).strip())


def wavelength_values(metadata):
    """Return parsed wavelengths and how many entries could not be parsed."""
    raw = metadata.get("wavelength")
    if raw is None:
        return None, 0
    if isinstance(raw, str):
        raw = [part.strip() for part in raw.strip("{}").split(",") if part.strip()]
    values = []
    invalid = 0
    for item in raw:
        text = str(item).strip()
        if text == "":
            invalid += 1
            values.append(None)
            continue
        try:
            values.append(float(text))
        except ValueError:
            invalid += 1
            values.append(None)
    return values, invalid


def load_cube(bin_path, metadata):
    """Load an ENVI binary cube as a (lines, samples, bands) array."""
    lines = header_int(metadata, "lines")
    samples = header_int(metadata, "samples")
    bands = header_int(metadata, "bands")
    offset = header_int(metadata, "header offset") if "header offset" in metadata else 0
    interleave = str(metadata["interleave"]).strip().lower()
    dtype = envi_dtype(metadata["data type"], metadata["byte order"])
    count = lines * samples * bands
    expected_bytes = offset + count * dtype.itemsize
    file_bytes = bin_path.stat().st_size

    if interleave not in {"bip", "bil", "bsq"}:
        raise ValueError(f"Unsupported interleave: {interleave}")
    if file_bytes < expected_bytes:
        raise ValueError(
            f"Binary file is {file_bytes} bytes; "
            f"header requires {expected_bytes} bytes"
        )

    flat = np.fromfile(bin_path, dtype=dtype, count=count, offset=offset)
    if flat.size != count:
        raise ValueError(f"Expected {count} values, read {flat.size}")

    if interleave == "bip":
        cube = flat.reshape((lines, samples, bands))
    elif interleave == "bil":
        cube = flat.reshape((lines, bands, samples)).transpose(0, 2, 1)
    else:
        cube = flat.reshape((bands, lines, samples)).transpose(1, 2, 0)
    return cube, dtype, interleave, file_bytes, expected_bytes


def finite_stats(cube):
    """Report NaN/infinite presence for a loaded cube."""
    if np.issubdtype(cube.dtype, np.floating):
        has_nan = bool(np.isnan(cube).any())
        has_inf = bool(np.isinf(cube).any())
        finite = np.isfinite(cube)
    elif np.issubdtype(cube.dtype, np.complexfloating):
        has_nan = bool(np.isnan(cube).any())
        has_inf = bool(np.isinf(cube).any())
        finite = np.isfinite(cube)
    else:
        return {
            "has_nan": False,
            "has_inf": False,
            "finite_note": "Integer data cannot contain NaN or infinite values.",
            "minimum": str(cube.min()),
            "maximum": str(cube.max()),
        }

    if finite.any():
        minimum = str(np.min(cube[finite]))
        maximum = str(np.max(cube[finite]))
    else:
        minimum = "undefined"
        maximum = "undefined"
    return {
        "has_nan": has_nan,
        "has_inf": has_inf,
        "finite_note": "",
        "minimum": minimum,
        "maximum": maximum,
    }


def iter_headers(root):
    for camera_dir in sorted(path for path in root.iterdir() if path.is_dir()):
        for header in sorted(camera_dir.rglob("*.hdr")):
            yield camera_dir.name, header


def choose_samples(root):
    """Pick a few header/binary pairs from different capture folders."""
    chosen = []
    for camera_dir in sorted(path for path in root.iterdir() if path.is_dir()):
        paired = [
            header for header in sorted(camera_dir.rglob("*.hdr"))
            if header.with_suffix(".bin").is_file()
        ]
        picks = []
        seen_folders = set()
        for header in paired:
            if header.parent in seen_folders:
                continue
            picks.append(header)
            seen_folders.add(header.parent)
            if len(picks) == SAMPLES_PER_CAMERA:
                break
        if len(picks) < SAMPLES_PER_CAMERA:
            for header in paired:
                if header not in picks:
                    picks.append(header)
                if len(picks) == SAMPLES_PER_CAMERA:
                    break
        chosen.extend(picks)
    return chosen


def wavelength_summary(values, band_count, invalid):
    lines = []
    if values is None:
        lines.append("Wavelength field: absent")
        lines.append(f"Missing wavelength entries: {band_count} of {band_count}")
        lines.append("Minimum wavelength: not available")
        lines.append("Maximum wavelength: not available")
        lines.append("Duplicate wavelength values: not available")
        return lines

    numeric = [value for value in values if value is not None]
    missing = band_count - len(numeric)
    lines.append(f"Wavelength entries in header: {len(values)}")
    lines.append(f"Parsed numeric wavelengths: {len(numeric)}")
    lines.append(f"Unparseable wavelength entries: {invalid}")
    lines.append(f"Missing wavelength entries: {missing}")
    if numeric:
        lines.append(f"Minimum wavelength: {min(numeric)}")
        lines.append(f"Maximum wavelength: {max(numeric)}")
        counts = Counter(numeric)
        duplicates = sorted(value for value, count in counts.items() if count > 1)
        if duplicates:
            shown = ", ".join(f"{value} (x{counts[value]})" for value in duplicates[:20])
            lines.append(f"Duplicate wavelength values: {len(duplicates)} [{shown}]")
        else:
            lines.append("Duplicate wavelength values: none")
    else:
        lines.append("Minimum wavelength: not available")
        lines.append("Maximum wavelength: not available")
        lines.append("Duplicate wavelength values: none")
    return lines


def inspect_headers(root):
    signatures = Counter()
    examples = {}
    wavelength_files = []
    unpaired = []
    total = 0
    for camera, header in iter_headers(root):
        total += 1
        metadata = envi.read_envi_header(str(header))
        signature = (
            camera,
            header_int(metadata, "samples"),
            header_int(metadata, "lines"),
            header_int(metadata, "bands"),
            str(metadata.get("data type", "")).strip(),
            str(metadata.get("interleave", "")).strip().lower(),
            str(metadata.get("byte order", "")).strip(),
            "wavelength" in metadata,
        )
        signatures[signature] += 1
        examples.setdefault(signature, header)
        if "wavelength" in metadata:
            wavelength_files.append(header)
        if not header.with_suffix(".bin").is_file():
            unpaired.append(header)
    return {
        "total": total,
        "signatures": signatures,
        "examples": examples,
        "wavelength_files": wavelength_files,
        "unpaired": unpaired,
    }


def inspect_sample(header):
    bin_path = header.with_suffix(".bin")
    image = envi.open(str(header), image=str(bin_path))
    metadata = image.metadata
    lines = []
    lines.append(f"Header: {header}")
    lines.append(f"Binary: {bin_path}")
    lines.append(
        "Dimensions (lines x samples x bands): "
        f"{metadata.get('lines')} x {metadata.get('samples')} x {metadata.get('bands')}"
    )
    lines.append(f"spectral shape: {tuple(image.shape)}")
    lines.append(f"spectral nbands: {image.nbands}")
    lines.append(f"spectral dtype: {image.dtype}")
    lines.append(f"Data type: {metadata.get('data type')}")
    lines.append(f"Interleave: {metadata.get('interleave')}")
    lines.append(f"Byte order: {metadata.get('byte order')}")
    lines.append(f"Header offset: {metadata.get('header offset', 0)}")
    lines.append(f"File type: {metadata.get('file type', '')}")

    values, invalid = wavelength_values(metadata)
    lines.extend(wavelength_summary(values, header_int(metadata, "bands"), invalid))

    cube, dtype, interleave, file_bytes, expected_bytes = load_cube(bin_path, metadata)
    stats = finite_stats(cube)
    lines.append(f"Loaded with: numpy.fromfile dtype={dtype}, interleave={interleave}")
    lines.append(f"Binary bytes: {file_bytes} (expected {expected_bytes})")
    lines.append(f"Array shape: {cube.shape}")
    lines.append(f"Array dtype: {cube.dtype}")
    lines.append(f"Contains NaN: {stats['has_nan']}")
    lines.append(f"Contains infinite values: {stats['has_inf']}")
    if stats["finite_note"]:
        lines.append(stats["finite_note"])
    lines.append(f"Finite minimum: {stats['minimum']}")
    lines.append(f"Finite maximum: {stats['maximum']}")
    lines.append("Binary load: OK")
    return lines


def numeric_sequence(node):
    if not isinstance(node, (ast.List, ast.Tuple)):
        return None
    values = []
    for elt in node.elts:
        if isinstance(elt, ast.Constant) and isinstance(elt.value, (int, float)) and not isinstance(elt.value, bool):
            values.append(elt.value)
        elif (
            isinstance(elt, ast.UnaryOp)
            and isinstance(elt.op, ast.USub)
            and isinstance(elt.operand, ast.Constant)
            and isinstance(elt.operand.value, (int, float))
        ):
            values.append(-elt.operand.value)
        else:
            return None
    return values


def assigned_name(target):
    if isinstance(target, ast.Name):
        return target.id
    return None


def looks_like_wavelengths(values):
    return all(isinstance(value, float) or (isinstance(value, int) and not isinstance(value, bool)) for value in values) and all(200 <= float(value) <= 3000 for value in values)


def looks_like_band_indices(values):
    return all(isinstance(value, int) and not isinstance(value, bool) for value in values) and all(0 <= value <= 400 for value in values)


def search_python(path):
    findings = []
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        source = path.read_text(encoding="utf-8", errors="replace")
    for pattern in BAND_PHRASES:
        for match in pattern.finditer(source):
            line_no = source.count("\n", 0, match.start()) + 1
            findings.append(
                f"{path.relative_to(PROJECT_DIR)}:{line_no}: phrase '{match.group(0)}'"
            )
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        findings.append(f"{path.relative_to(PROJECT_DIR)}: could not parse ({exc})")
        return findings

    for node in ast.walk(tree):
        targets = []
        value = None
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
            value = node.value
        if value is None:
            continue
        values = numeric_sequence(value)
        if values is None:
            continue
        names = [assigned_name(target) for target in targets]
        names = [name for name in names if name]
        label = ", ".join(names) if names else "<unnamed>"
        if not values:
            continue
        relevant_name = any(BAND_NAME.search(name) for name in names)
        if len(values) == 56 or relevant_name:
            kind = "numeric list"
            if looks_like_wavelengths(values):
                kind = "wavelength-like list"
            elif looks_like_band_indices(values):
                kind = "band-index-like list"
            findings.append(
                f"{path.relative_to(PROJECT_DIR)}:{node.lineno}: {label} "
                f"length={len(values)} min={min(values)} max={max(values)} ({kind})"
            )
    return findings


def search_json(path):
    findings = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        findings.append(f"{path.relative_to(PROJECT_DIR)}: could not parse JSON ({exc})")
        return findings

    seen = set()

    def walk(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if (
                    str(key).lower() in {"wavelength", "wavelengths", "bands", "selected_bands", "usable_bands"}
                    and isinstance(value, list)
                    and value
                    and all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in value)
                ):
                    signature = (str(key), len(value), value[0], value[-1])
                    if signature not in seen:
                        seen.add(signature)
                        findings.append(
                            f"{path.relative_to(PROJECT_DIR)}: key '{key}' "
                            f"length={len(value)} first={value[0]} last={value[-1]}"
                        )
                else:
                    walk(value)
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, (dict, list)):
                    walk(item)

    walk(payload)
    return findings


def search_text_phrases(path):
    if path.suffix.lower() == ".py" or path.resolve() == REPORT_PATH.resolve():
        return []
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        source = path.read_text(encoding="utf-8", errors="replace")
    findings = []
    for pattern in BAND_PHRASES:
        for match in pattern.finditer(source):
            line_no = source.count("\n", 0, match.start()) + 1
            findings.append(
                f"{path.relative_to(PROJECT_DIR)}:{line_no}: phrase '{match.group(0)}'"
            )
    return findings


def search_repository():
    findings = []
    for path in sorted(PROJECT_DIR.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in SEARCH_SUFFIXES:
            continue
        if path.resolve() == REPORT_PATH.resolve() or path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() == ".py":
            findings.extend(search_python(path))
        elif path.suffix.lower() == ".json":
            findings.extend(search_json(path))
            findings.extend(search_text_phrases(path))
        else:
            findings.extend(search_text_phrases(path))
    return findings


def repository_band_lists():
    """Read the camera wavelength constants without importing model code."""
    source = (PROJECT_DIR / "core" / "spectral_io.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    lists = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        values = numeric_sequence(node.value)
        if values is None:
            continue
        for target in node.targets:
            name = assigned_name(target)
            if name and name.endswith("_BANDS"):
                counts = Counter(values)
                duplicates = sorted(value for value, count in counts.items() if count > 1)
                lists.append(
                    {
                        "name": name,
                        "count": len(values),
                        "minimum": min(values),
                        "maximum": max(values),
                        "duplicates": duplicates,
                    }
                )
    return lists


def format_signature(signature, count, example):
    camera, samples, lines, bands, data_type, interleave, byte_order, has_wave = signature
    return (
        f"{camera}: {count} files | samples={samples}, lines={lines}, bands={bands}, "
        f"data type={data_type}, interleave={interleave}, byte order={byte_order}, "
        f"wavelength field={'present' if has_wave else 'absent'} | example: {example.name}"
    )


def build_report():
    lines = []
    lines.append("Mango hyperspectral band inspection")
    lines.append(f"Dataset: {DATASET_ROOT}")
    lines.append(f"Project: {PROJECT_DIR}")
    lines.append(f"NumPy: {np.__version__}")
    import spectral
    lines.append(f"spectral: {spectral.__version__}")
    lines.append("")
    lines.append("Binary values are loaded with numpy.fromfile from the header")
    lines.append("data type and interleave. SpyFile.load is not used, because")
    lines.append("spectral 0.23 evaluates np.dtype('complex256') for every cube.")
    lines.append("")

    if not DATASET_ROOT.is_dir():
        lines.append(f"Dataset folder was not found: {DATASET_ROOT}")
        return lines

    census = inspect_headers(DATASET_ROOT)
    lines.append("1. Header metadata")
    lines.append(f"Header files found: {census['total']}")
    lines.append(f"Headers without a matching .bin file: {len(census['unpaired'])}")
    lines.append(f"Headers that contain a wavelength field: {len(census['wavelength_files'])}")
    lines.append("Distinct header layouts:")
    for signature, count in sorted(census["signatures"].items()):
        lines.append("  " + format_signature(signature, count, census["examples"][signature]))
    lines.append("")

    lines.append("2. Sample cubes")
    samples = choose_samples(DATASET_ROOT)
    if not samples:
        lines.append("No header/binary pairs were found.")
    for header in samples:
        lines.append("")
        try:
            lines.extend(inspect_sample(header))
        except Exception as exc:
            lines.append(f"Header: {header}")
            lines.append(f"Binary load: FAILED ({type(exc).__name__}: {exc})")
    lines.append("")

    lines.append("3. Wavelength summary")
    band_lists = repository_band_lists()
    if census["wavelength_files"]:
        lines.append("Wavelength statistics above come from the ENVI headers.")
    else:
        lines.append("None of the mango ENVI headers store wavelength values.")
        lines.append("Minimum, maximum, and duplicate wavelengths therefore cannot")
        lines.append("be calculated from the headers. Every band is missing a")
        lines.append("header wavelength entry.")
    lines.append("")
    lines.append("Repository camera wavelength lists in core/spectral_io.py:")
    if not band_lists:
        lines.append("  No *_BANDS lists were found.")
    for item in band_lists:
        duplicate_text = "none" if not item["duplicates"] else str(item["duplicates"][:10])
        lines.append(
            f"  {item['name']}: count={item['count']}, "
            f"minimum={item['minimum']}, maximum={item['maximum']}, "
            f"duplicates={duplicate_text}"
        )
    lines.append("")
    lines.append("These lists are the full camera wavelength tables used by the")
    lines.append("existing training code. VIS_BANDS matches the 224-band VIS cubes.")
    lines.append("VIS_COR_BANDS matches the 249-band VIS_COR cubes. NIR_BANDS has")
    lines.append("no corresponding camera folder in this mango extract.")
    lines.append("")

    lines.append("4. Search for a 56-band selection")
    lines.append("Searched Python, JSON, and configuration files under the project")
    lines.append("for band/wavelength lists and for phrases that name a band selection.")
    findings = search_repository()
    selection = [
        finding for finding in findings
        if "length=56" in finding or "phrase" in finding
    ]
    lines.append("Band-related definitions found:")
    if findings:
        for finding in findings:
            lines.append(f"  {finding}")
    else:
        lines.append("  none")
    lines.append("")
    if selection:
        lines.append("A 56-value or explicitly named band-selection match was found.")
        lines.append("Review the matches above before treating any of them as the")
        lines.append("usable band set. This script does not propose a new selection.")
    else:
        lines.append("No selection of 56 usable bands is defined in the repository.")
        lines.append("The camera tables above contain 224, 249, and 252 wavelengths.")
        lines.append("This script does not propose a band selection.")
    lines.append("")
    return lines


def main():
    report = "\n".join(build_report())
    REPORT_PATH.write_text(report + "\n", encoding="utf-8")
    print(report)
    print(f"Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
