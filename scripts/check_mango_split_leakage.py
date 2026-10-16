
import csv
from pathlib import Path
from collections import defaultdict, Counter

manifest = Path(__file__).resolve().parent / "mango_labeled_manifest.csv"

groups = defaultdict(list)

with manifest.open("r", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        # Use the filename to identify the physical mango.
        # Ignore camera folder and front/back side.
        stem = Path(row["header_path"]).stem

        if stem.endswith("_front"):
            stem = stem[:-6]
        elif stem.endswith("_back"):
            stem = stem[:-5]

        groups[stem].append(row)

print("Total image records:", sum(len(v) for v in groups.values()))
print("Likely unique physical mangoes:", len(groups))

overlap = []
inconsistent_labels = []

for mango_id, rows in sorted(groups.items()):
    splits = sorted(set(row["split"] for row in rows))
    labels = sorted(set(row["ripeness"] for row in rows))

    if len(splits) > 1:
        overlap.append((mango_id, splits, labels, len(rows)))

    if len(labels) > 1:
        inconsistent_labels.append((mango_id, labels, len(rows)))

print("\nPhysical mangoes appearing in multiple splits:", len(overlap))
for item in overlap[:20]:
    print(item)

print("\nPhysical mangoes with inconsistent ripeness labels:",
      len(inconsistent_labels))
for item in inconsistent_labels[:20]:
    print(item)

print("\nRecords per split:")
for split in ["train", "validation", "test"]:
    count = sum(
        1 for rows in groups.values()
        for row in rows if row["split"] == split
    )
    print(f"  {split}: {count}")

print("\nRipeness labels across unique mangoes:")
unique_labels = Counter()
for rows in groups.values():
    labels = {row["ripeness"] for row in rows}
    if len(labels) == 1:
        unique_labels.update(labels)

print(dict(unique_labels))
