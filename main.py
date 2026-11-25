"""Fridge-roast writer: one fixed line roasting a fridge that only judges."""

import os, string, sys

TEXT = "My fridge hums all night like it pays rent, yet the only thing it has ever produced is a light that turns on when I open the door to judge me."
LIMIT = 200
ENDERS = ".!?"

def fail(msg):
    sys.stderr.write("invalid: " + msg + "\n")
    raise SystemExit(1)

def validate(text):
    lowered = text.casefold()
    rules = [
        ("fridge" not in lowered, "must mention the fridge"),
        ("," not in text, "no comma to breathe with"),
        (not text.strip(), "blank entry"),
        (len(text) > LIMIT, "over 200 characters"),
        (any(ord(c) < 32 or ord(c) == 127 for c in text), "control character found"),
        (text != text.strip() or "  " in text or "\n" in text, "ragged edges, double space, or newline"),
        (bool(text) and text[-1] not in ENDERS, "must end with . ! or ?"),
        (all(c in string.punctuation for c in text), "punctuation only"),
        (text.isdigit(), "digits only"),
        (not any(c.isalpha() for c in text), "no letters"),
        (any(c.isalpha() for c in text) and text.upper() == text, "all caps shouting"),
    ]
    for bad, msg in rules:
        if bad:
            fail(msg)

def write_out():
    validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT + "\n")

if __name__ == "__main__":
    write_out()
