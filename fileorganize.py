from extensionlists import document_ext, images_ext, archives_ext, videos_ext, music_ext
from pathlib import Path
import shutil
import time


class FileOrganizer:
    def __init__(self, src_dir = None):
        self.src_dir = src_dir or Path.cwd() / "unorganized"

        # Sets paths
        self.documents_dir = Path.cwd() / "organized" / "documents"
        self.images_dir = Path.cwd() / "organized" / "images"
        self.archives_dir = Path.cwd() / "organized" / "archives"
        self.videos_dir = Path.cwd() / "organized" / "videos"
        self.music_dir = Path.cwd() / "organized" / "music"

        # Ensures directory exists
        self.documents_dir.mkdir(parents = True, exist_ok = True)
        self.images_dir.mkdir(parents = True, exist_ok = True)
        self.archives_dir.mkdir(parents = True, exist_ok = True)
        self.videos_dir.mkdir(parents = True, exist_ok = True)
        self.music_dir.mkdir(parents = True, exist_ok = True)

        # Initiate counter
        self.docu_count = 0
        self.images_count = 0
        self.archives_count = 0
        self.videos_count = 0
        self.music_count = 0

    # Identifies the file according to .suffix of the item
    def identify_file(self):
        for item in self.src_dir.iterdir():
            if item.suffix in document_ext:
                print(f"{item.name} is a document")

            elif item.suffix in images_ext:
                print(f"{item.name} is an image")

            elif item.suffix in archives_ext:
                print(f"{item.name} is a archive")

            elif item.suffix in videos_ext:
                print(f"{item.name} is a video")

            elif item.suffix in music_ext:
                print(f"{item.name} is a music")

            else:
                print(f"{item.name} is uncategorized")

    # Moves the item to its respective directory
    def move_item(self):
        for item in self.src_dir.iterdir():
            if item.suffix in images_ext:
                shutil.move(str(item), self.images_dir)
                self.images_count += 1

            elif item.suffix in document_ext:
                shutil.move(str(item), self.documents_dir)
                self.docu_count += 1

            elif item.suffix in archives_ext:
                shutil.move(str(item), self.archives_dir)
                self.archives_count += 1

            elif item.suffix in videos_ext:
                shutil.move(str(item), self.videos_dir)
                self.videos_count += 1

            elif item.suffix in music_ext:
                shutil.move(str(item), self.music_dir)
                self.music_count += 1

    # Shows summary of how many items are sorted
    def move_summary(self):
        summary = [
            f"Documents: {self.docu_count}",
            f"Images: {self.images_count}",
            f"Archives: {self.archives_count}",
            f"Videos: {self.videos_count}",
            f"Music: {self.music_count}",
            ]

        for ln in summary:
            print(ln)
            time.sleep(0.2)
