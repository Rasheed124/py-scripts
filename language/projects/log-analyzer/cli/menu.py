
VALID_ACTIONS = {
    "load",
    "view",
    "log",
    "clean",
    "validate",
    "missing",
    "save",
}


def display_welcome() -> None:
    print("=" * 45)
    print("             LOG FILE ANALYZER")
    print("=" * 45)


def display_menu() -> None:
    print("\nAvailable Actions")
    print("-" * 45)
    print("  load     -> Reload the current log file")
    print("  view     -> View all log entries")
    print("  log      -> Analyze log levels")
    print("  clean    -> Remove surrounding whitespace")
    print("  validate -> Validate log levels and dates")
    print("  missing  -> Find empty or unclassified entries")
    print("  save     -> Save entries to a new file")
    print("  exit     -> Exit the program")
    print("-" * 45)
