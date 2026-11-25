import os

ENTRY = "OOO: on vacation. My neural nets are literal nets now, cast into the sea. Urgent? Don't be."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print("length:", len(ENTRY))


if __name__ == "__main__":
    main()
