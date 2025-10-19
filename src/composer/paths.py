from pathlib import Path

Root = Path(__file__).resolve().parents[2]
# parents[2] goes up 2 levels back to repo root


CLIPS = ROOT / "clips"
WORK = ROOT / "work"
OUT = ROOT / "out"

# create folder if doesnt already exist
for p in (CLIPS, WORK, OUT):
  p.mkdir(exist_ok=True)
