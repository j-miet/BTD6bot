"""Auto-updates helpwindow images."""

import os
from pathlib import Path
import shutil

img_address = Path(__file__).parent.parent/'docs/images'
destination = Path(__file__).parent.parent/'btd6bot/Files/helpwindow/images'

if os.path.isdir(destination):
    shutil.rmtree(destination)
shutil.copytree(img_address, destination)