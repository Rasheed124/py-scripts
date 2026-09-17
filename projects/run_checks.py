import subprocess
import sys


subprocess.run([sys.executable, "calculator/main.py"])

subprocess.run([sys.executable, "-m", "mypy", "."])