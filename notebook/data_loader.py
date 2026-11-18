import pandas as pd

def load_log(path):
    rows = []

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        first_line = f.readline()

        # Ignore l'en-tête s'il est présent
        if first_line.strip() != "category,log":
            category, separator, log = first_line.rstrip("\n").partition(",")
            if not separator:
                raise ValueError(f"Ligne 1 invalide dans {path}")
            rows.append({"category": category.strip(), "log": log.strip()})

        for line_number, line in enumerate(f, start=2):
            line = line.rstrip("\n")
            if not line:
                continue

            category, separator, log = line.partition(",")
            if not separator:
                raise ValueError(f"Ligne {line_number} invalide dans {path}")

            rows.append({"category": category.strip(), "log": log.strip()})

    return pd.DataFrame(rows)