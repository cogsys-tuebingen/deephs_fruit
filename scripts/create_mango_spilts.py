
import csv
import random
from pathlib import Path
from collections import defaultdict, Counter

manifest = Path(__file__).resolve().parent / "mango_labeled_manifest.csv"
output = Path(__file__).resolve().parent / "mango_fruit_splits.csv"

random.seed(42)

# Group all views of a likely physical mango together.
groups = defaultdict(list)

with manifest.open("r", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        stem = Path(row["header_path"]).stem
        if stem.endswith("_front"):
            stem = stem[:-6]
        elif stem.endswith("_back"):
            stem = stem[:-5]

        groups[stem].append(row)

# Check that every fruit group has one consistent label.
fruits = []
for fruit_id, rows in sorted(groups.items()):
    labels = {row["ripeness"] for row in rows}
    if len(labels) != 1:
        raise ValueError(f"Inconsistent labels for {fruit_id}: {labels}")

    fruits.append({
        "fruit_id": fruit_id,
        "ripeness": next(iter(labels)),
        "record_count": len(rows),
    })

# Stratify separately within each ripeness class.
by_label = defaultdict(list)
for fruit in fruits:
    by_label[fruit["ripeness"]].append(fruit)

assignments = {}
for label, items in sorted(by_label.items()):
    random.shuffle(items)
    n = len(items)

    # Approximate 70/15/15 split within each class.
    n_test = max(1, round(n * 0.15))
    n_val = max(1, round(n * 0.15))

    # Ensure at least one training fruit remains.
    while n_test + n_val >= n:
        if n_val > 1:
            n_val -= 1
        else:
            n_test -= 1

    for item in items[:n_test]:
        assignments[item["fruit_id"]] = "test"
    for item in items[n_test:n_test + n_val]:
        assignments[item["fruit_id"]] = "validation"
    for item in items[n_test + n_val:]:
        assignments[item["fruit_id"]] = "train"

with output.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f, fieldnames=["fruit_id", "ripeness", "record_count", "split"]
    )
    writer.writeheader()
    for fruit in fruits:
        writer.writerow({
            **fruit,
            "split": assignments[fruit["fruit_id"]],
        })

print("Saved:", output)
print("Unique mangoes:", len(fruits))

for split in ["train", "validation", "test"]:
    selected = [
        fruit for fruit in fruits
        if assignments[fruit["fruit_id"]] == split
    ]
    print(f"\n{split}: {len(selected)} mangoes")
    print(dict(Counter(f["ripeness"] for f in selected)))

# Verify that each fruit belongs to exactly one split.
assert len(assignments) == len(fruits)
print("\nLeakage-safe group assignment: PASS")
