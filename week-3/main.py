import json

with open("knowledge_base.json") as f:
    kb = json.load(f)

VALID_SYMPTOMS = kb["symptoms"]
RULES = kb["rules"]


def get_symptoms():
    print("\nAvailable symptoms:")
    for i, s in enumerate(VALID_SYMPTOMS, 1):
        print(f"  {i}. {s.title()}")

    raw = input("\nEnter symptoms (comma-separated): ").strip().lower()
    entered = [s.strip() for s in raw.split(",") if s.strip()]

    valid, invalid = [], []
    for s in entered:
        (valid if s in VALID_SYMPTOMS else invalid).append(s)

    if invalid:
        print(f"Warning: unrecognized symptoms ignored: {', '.join(invalid)}")

    return valid


def infer(symptoms):
    results = []
    for rule in RULES:
        if all(c in symptoms for c in rule["conditions"]):
            results.append(rule["diagnosis"])
    return results


def main():
    print("=" * 40)
    print("  Medical Expert System")
    print("=" * 40)

    symptoms = get_symptoms()

    if not symptoms:
        print("No valid symptoms entered.")
        return

    print(f"\nSymptoms recorded: {', '.join(s.title() for s in symptoms)}")

    diagnoses = infer(symptoms)

    print("\n--- Diagnosis ---")
    if diagnoses:
        for d in diagnoses:
            print(f"  Possible condition: {d}")
    else:
        print("  No matching condition found. Please consult a doctor.")


if __name__ == "__main__":
    main()
