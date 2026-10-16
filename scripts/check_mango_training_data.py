
import json
from pathlib import Path
from collections import Counter

annotation_dir = Path(
    r"D:\deephs_data\annotations\extracted\annotations"
)
mango_dir = Path(r"D:\deephs_data\Mango_extracted\Mango")

files_to_check = [
    "train_all_v2.json",
    "train_only_labeled_v2.json",
    "val_v2.json",
    "test_v2.json",
]

for filename in files_to_check:
    path = annotation_dir / filename

    if not path.exists():
        print(f"\n{filename}: file not found")
        continue

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    records = data.get("records", [])
    annotations = data.get("annotations", [])

    record_by_id = {r["id"]: r for r in records}
    annotations_by_record = {
        a["record_id"]: a for a in annotations
    }

    mango_records = [
        r for r in records
        if r.get("fruit", "").lower() == "mango"
    ]

    label_counts = Counter()
    matched_hdr = 0
    matched_bin = 0
    examples = []

    for record in mango_records:
        annotation = annotations_by_record.get(record["id"], {})
        label = annotation.get("ripeness_state", "MISSING")
        label_counts[label] += 1

        relative_path = record["files"]["header_file"]
        parts = Path(relative_path).parts

        # Annotation paths start with Mango/, already represented
        # by mango_dir, so remove that first path component.
        local_relative = Path(*parts[1:])
        hdr_path = mango_dir / local_relative
        bin_path = hdr_path.with_suffix(".bin")

        hdr_exists = hdr_path.exists()
        bin_exists = bin_path.exists()

        matched_hdr += hdr_exists
        matched_bin += bin_exists

        if len(examples) < 3:
            examples.append({
                "id": record["id"],
                "camera": record.get("camera_type"),
                "label": label,
                "header_exists": hdr_exists,
                "binary_exists": bin_exists,
                "path": str(hdr_path),
            })

    print(f"\n{'=' * 55}")
    print("FILE:", filename)
    print("All records:", len(records))
    print("Mango records:", len(mango_records))
    print("Mango ripeness labels:", dict(label_counts))
    print("Matching header files:", matched_hdr)
    print("Matching binary files:", matched_bin)
    print("Examples:")
    for example in examples:
        print(json.dumps(example, indent=2))
