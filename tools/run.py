import subprocess, sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
RUNNER_EXT = ROOT_DIR / "external" / "main.py"
SRC_DIR = ROOT_DIR / "src"

num: int = int(sys.argv[1])
ex_dir = SRC_DIR / f"ex{num}"

actions = ("", "Community garden", "5\n3\n", "5\n8\n3\n", "75", "4", "5\n5", "")

subprocess.run(
    ["python3", str(RUNNER_EXT)],
    cwd=ex_dir,
    input=f"{num}\n{actions[num]}",
    text=True,
    check=True,
)
