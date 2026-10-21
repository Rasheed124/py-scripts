
class LogAnalyzerError(Exception):
    """Base exception for log analyzer errors."""


class InvalidInputError(LogAnalyzerError):
    """Raised when user input is invalid."""


class LogFileNotFoundError(LogAnalyzerError):
    """Raised when a log file does not exist or is empty."""


class StorageError(LogAnalyzerError):
    """Raised when reading or writing a log file fails."""
