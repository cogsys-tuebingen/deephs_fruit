
import json
from pathlib import Path
from collections import Counter

folder = Path(r"D:\deephs_data\annotations\extracted\annotations")

for file in sorted(folder.glob("*.json")):
    with file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    records = data.get("records", [])
    annotations = data.get("annotations", [])

    fruit_counts = Counter(
        record.get("fruit", "Unknown") for record in records
    )

    record_by_id = {record["id"]: record for record in records}
    label_counts = Counter()
    mango_records = []

    for annotation in annotations:
        record = record_by_id.get(annotation.get("record_id"))
        if not record:
            continue

        fruit = record.get("fruit", "Unknown")
        state = annotation.get("ripeness_state", "Missing")
        label_counts[(fruit, state)] += 1

        if fruit.lower() == "mango":
            mango_records.append({
                "record": record,
                "annotation": annotation
            })

    print(f"\n{'=' * 55}")
    print(f"FILE: {file.name}")
    print("Records by fruit:", dict(fruit_counts))
    print("Ripeness labels by fruit:")

    for (fruit, state), count in sorted(label_counts.items()):
        print(f"  {fruit} | {state}: {count}")

    print(f"Mango records with annotations: {len(mango_records)}")

    for item in mango_records[:2]:
        print("Mango example:")
        print(json.dumps(item, indent=2))
