$python = "$PSScriptRoot\.venv\Scripts\python.exe"

& $python -m watchfiles "`"$python`" run_checks.py"