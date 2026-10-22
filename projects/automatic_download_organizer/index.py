



from pathlib import Path
import shutil
from time import sleep
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


class DownloadOrganizerError(Exception):
    """Base exception for Download Organizer domain errors."""
    pass


class StorageError(DownloadOrganizerError):
    """Raised when file moving or directory creation fails."""
    pass


def organize_single_file(file_path: Path, base_directory: Path) -> None:
    """Classify a single file by extension and move it into its respective subfolder."""
    try:
        if not file_path.is_file() or file_path.suffix in (".crdownload", ".part", ".tmp"):
            return

        ext = file_path.suffix.lstrip(".").lower()
        if not ext:
            ext = "no_extension"

        subfolder = base_directory / ext
        subfolder.mkdir(exist_ok=True)

        destination = subfolder / file_path.name

        if destination.exists():
            counter = 1
            while destination.exists():
                stem = file_path.stem
                destination = subfolder / f"{stem}_{counter}{file_path.suffix}"
                counter += 1

        if file_path.resolve() != destination.resolve():
            shutil.move(str(file_path), str(destination))
            print(f"[Organized] '{file_path.name}' ➔ /{ext}/")

    except OSError as err:
        raise StorageError(f"Failed to process file '{file_path.name}': {err}") from err


def watch_and_organize_downloads() -> None:
    """Monitor the Downloads directory in real-time and automatically organize incoming files."""
    
    class DownloadHandler(FileSystemEventHandler):
        def __init__(self, target_dir: Path):
            self.target_dir = target_dir

        def on_created(self, event: FileSystemEvent) -> None:
            if event.is_directory:
                return
            
            sleep(0.5)
            created_file = Path(event.src_path)
            
            try:
                organize_single_file(created_file, self.target_dir)
            except DownloadOrganizerError as err:
                print(f"[Error] {err}")

    download_folder = Path.home() / "Downloads"

    if not download_folder.exists():
        download_folder.mkdir(exist_ok=True)

    event_handler = DownloadHandler(download_folder)
    observer = Observer()
    observer.schedule(event_handler, download_folder, recursive=False)
    observer.start()

    print("=" * 50)
    print("        AUTOMATIC DOWNLOADS ORGANIZER ACTIVE")
    print("=" * 50)
    print(f"Monitoring: {download_folder}")
    print("Files will be automatically classified and sorted upon download.")
    print("Press Ctrl+C to stop the daemon.\n")

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()
        print("\nDownload Organizer stopped. Goodbye!")


if __name__ == "__main__":
    watch_and_organize_downloads()