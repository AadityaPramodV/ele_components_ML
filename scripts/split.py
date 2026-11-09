import os, random, shutil
random.seed(42)

src, dst = "data", "dataset"
exts = (".jpg", ".jpeg", ".png")

if os.path.exists(dst):
    shutil.rmtree(dst)

classes = sorted(d for d in os.listdir(src)
                 if os.path.isdir(os.path.join(src, d)) and not d.startswith("."))

for c in classes:
    name = c.lower().replace("-", "_")
    files = [f for f in os.listdir(os.path.join(src, c)) if f.lower().endswith(exts)]
    random.shuffle(files)
    n = len(files)
    n_tr, n_val = int(n * 0.7), int(n * 0.2)
    parts = {
        "train": files[:n_tr],
        "val": files[n_tr:n_tr + n_val],
        "test": files[n_tr + n_val:],
    }
    for split, fl in parts.items():
        os.makedirs(os.path.join(dst, split, name), exist_ok=True)
        for f in fl:
            shutil.copy(os.path.join(src, c, f), os.path.join(dst, split, name, f))
    print(f"{name}: {n} images -> train {len(parts['train'])}, val {len(parts['val'])}, test {len(parts['test'])}")
