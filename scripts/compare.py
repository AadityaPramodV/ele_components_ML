from ultralytics import YOLO
import pandas as pd

models = {
    "From scratch": "runs/classify/scratch/weights/best.pt",
    "Pre-trained + fine-tuned": "runs/classify/pretrained/weights/best.pt",
}

rows = []
for name, path in models.items():
    m = YOLO(path).val(data="dataset", split="test", device="mps", verbose=False)
    rows.append({"Model": name, "Top-1 accuracy": round(m.top1, 4)})

df = pd.DataFrame(rows)
print()
print(df.to_string(index=False))
df.to_csv("runs/comparison.csv", index=False)
