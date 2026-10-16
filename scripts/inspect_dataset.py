
from pathlib import Path

root = Path(r"D:\deephs_data\Mango_extracted\Mango")

for camera_dir in sorted(root.iterdir()):
    if not camera_dir.is_dir():
        continue

    headers = list(camera_dir.rglob("*.hdr"))
    binaries = list(camera_dir.rglob("*.bin"))

    print(f"\nCamera folder: {camera_dir.name}")
    print("Header files:", len(headers))
    print("Binary files:", len(binaries))

    binary_stems = {p.with_suffix("").as_posix() for p in binaries}
    matched = sum(
        1 for p in headers
        if p.with_suffix("").as_posix() in binary_stems
    )
    print("Matched header/binary pairs:", matched)

    print("Example folders:")
    for folder in sorted(camera_dir.iterdir())[:5]:
        if folder.is_dir():
            print(" ", folder.name)

# Search for any labels or annotations already extracted.
annotation_root = Path(r"D:\deephs_data")

print("\nPotential annotation files:")
for p in annotation_root.rglob("*"):
    if p.is_file() and p.suffix.lower() in {".json", ".csv", ".xlsx", ".xml"}:
        print(p)
