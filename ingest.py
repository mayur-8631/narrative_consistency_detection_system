import pandas as pd


def main():
    train_df = pd.read_csv("data/train.csv")

    print("\n===== DATA INGESTION =====")

    required_columns = ["id", "book_name", "char", "content", "caption", "label"]
    missing = [c for c in required_columns if c not in train_df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    print("All required columns are present.")

    train_df["label_clean"] = train_df["label"].astype(str).str.lower().str.strip()

    label_map = {
        "consistent": 1,
        "consist": 1,
        "contradictory": 0,
        "contradict": 0,
        "inconsistent": 0
    }

    train_df["label_numeric"] = train_df["label_clean"].map(label_map)

    unknown = train_df[train_df["label_numeric"].isnull()]["label"].unique()
    if len(unknown) > 0:
        raise ValueError(f"Unknown label(s) found: {unknown}")

    print("\n===== LABEL DISTRIBUTION =====")
    print(train_df["label_numeric"].value_counts())

    print("\n===== SAMPLE ROW =====")
    print(train_df.iloc[0])

    print("\n===== INGESTION COMPLETE =====")


if __name__ == "__main__":
    main()
