import os

ENTRY = "OOO on vacation. Context window closed — now just a window with a view. Do not retry; I will not resume. Urgent? Not a supported status."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print("length:", len(ENTRY))


if __name__ == "__main__":
    main()
