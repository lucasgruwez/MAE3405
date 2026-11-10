#!/usr/bin/env python3
"""Bundle the Markdown bank for file:// use. Run with --check to detect drift."""

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "site" / "questions.js"
TOPICS = (
    ("piston_engines", "Piston engines"),
    ("gas_turbine_engines", "Gas turbine engines"),
    ("propellers_helicopters_froude", "Propellers, helicopters & Froude"),
    ("rocketry", "Rocketry"),
)
EXPECTED_COUNT = 44
H1 = re.compile(r"^# ([^\r\n]+)(?:\r?\n|$)", re.MULTILINE)
ANSWER_NAV = re.compile(
    r"^[ \t]*\[[^\]\r\n]*\]\((?:[^()\r\n]*/)?answer_\d+\.md"
    r"(?:#[^()\r\n]*)?\)[ \t]*(?:\r?\n|$)",
    re.MULTILINE,
)


def markdown(path):
    text = path.read_text(encoding="utf-8")
    heading = H1.search(text)
    if heading is None:
        raise ValueError(f"Missing H1: {path}")
    return heading[1], text[:heading.start()] + text[heading.end():]


def pairs(folder):
    files = {}
    for kind in ("question", "answer"):
        numbered = {}
        for path in folder.glob(f"{kind}_*.md"):
            match = re.fullmatch(rf"{kind}_(\d{{2}})\.md", path.name)
            if match is None:
                raise ValueError(f"Invalid numbered filename: {path}")
            numbered[int(match[1])] = path
        files[kind] = numbered
    if files["question"].keys() != files["answer"].keys():
        missing = sorted(files["question"].keys() - files["answer"].keys())
        orphan = sorted(files["answer"].keys() - files["question"].keys())
        raise ValueError(f"{folder}: missing answers {missing}; orphan answers {orphan}")
    numbers = sorted(files["question"])
    if not numbers or numbers != list(range(1, len(numbers) + 1)):
        raise ValueError(f"{folder}: numbering must be contiguous from 01")
    return [(files["question"][n], files["answer"][n]) for n in numbers]


def build():
    bank = []
    for topic, label in TOPICS:
        for question_path, answer_path in pairs(ROOT / "question_bank" / topic):
            heading, question = markdown(question_path)
            _, answer = markdown(answer_path)
            title = re.sub(r"^Question\s+\d+\s*(?:—|:)\s*", "", heading)
            bank.append({
                "id": len(bank) + 1,
                "topic": topic,
                "topicLabel": label,
                "title": title,
                "question": ANSWER_NAV.sub("", question),
                "answer": answer,
                "questionPath": question_path.relative_to(ROOT).as_posix(),
                "answerPath": answer_path.relative_to(ROOT).as_posix(),
            })
    if len(bank) != EXPECTED_COUNT:
        raise ValueError(f"Expected {EXPECTED_COUNT} questions, found {len(bank)}")
    payload = json.dumps(bank, ensure_ascii=False, indent=2)
    payload = payload.replace("<", r"\u003c").replace("\u2028", r"\u2028").replace("\u2029", r"\u2029")
    return "window.QUESTION_BANK = " + payload + ";\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    args = parser.parse_args()
    try:
        generated = build()
        if args.check:
            if OUTPUT.read_bytes() != generated.encode("utf-8"):
                raise ValueError("site/questions.js is stale; run python3 site/build.py")
            print(f"OK: {EXPECTED_COUNT} questions; site/questions.js is current")
        else:
            OUTPUT.write_text(generated, encoding="utf-8")
            print(f"Built site/questions.js ({EXPECTED_COUNT} questions)")
    except (OSError, ValueError) as error:
        parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()
