from pathlib import Path

def normalize_file_name(file_name: str, extension: str) -> Path:
    """Return a filename with the requested extension."""
    if not isinstance(file_name, str):
        raise TypeError("file_name must be a string.")
    cleaned = file_name.strip()
    if not cleaned:
        raise ValueError("file_name cannot be empty.")

    suffix = f".{extension.lstrip('.')}"
    path = Path(cleaned)
    if path.suffix.lower() != suffix.lower():
        path = path.with_suffix(suffix) if path.suffix else Path(f"{cleaned}{suffix}")
    return path
