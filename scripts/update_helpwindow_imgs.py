"""Auto-updates helpwindow images."""

from pathlib import Path
import shutil

img_address = Path(__file__).parent.parent/'docs/images'
destination = Path(__file__).parent.parent/'btd6bot/Files/helpwindow/images'

shutil.copytree(img_address, destination, dirs_exist_ok=True)