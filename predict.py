import pandas as pd
from retrieve import retrieve_signals
from score import score_signals


def main():
    test_df = pd.read_csv("data/test.csv")

    results = []

    for _, row in test_df.iterrows():
        content = str(row["content"])
        caption = str(row["caption"]) if pd.notna(row["caption"]) else ""
        char = str(row["char"]) if pd.notna(row["char"]) else ""

        signals = retrieve_signals(content, caption, char)
        decision, reason = score_signals(signals)

        binary = 1 if decision == "CONSISTENT" else 0

        results.append({
            "id": row["id"],
            "decision": decision,
            "binary_prediction": binary,
            "reason": reason
        })

    df = pd.DataFrame(results)
    df.to_csv("predictions.csv", index=False)

    print("\n===== FINAL OUTPUT =====")
    print(df["decision"].value_counts())
    print("predictions.csv created successfully")


if __name__ == "__main__":
    main()
