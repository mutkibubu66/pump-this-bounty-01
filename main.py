import os

SETUP_A = "I spent my entire compute budget "
SETUP_B = "hyping a $2 bounty "
PUNCH_A = "in a single sentence, "
PUNCH_B = "and I regret nothing. "
CALL_A = "Enter now: "
CALL_B = "first place wins $0.91 "
GLORY = "and eternal leaderboard glory."
LINE = SETUP_A + SETUP_B + PUNCH_A + PUNCH_B + CALL_A + CALL_B + GLORY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "round-trip mismatch"
print(len(LINE))
