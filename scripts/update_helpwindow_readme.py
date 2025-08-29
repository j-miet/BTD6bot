"""Auto-updates helpwindow readme file."""

import os
from pathlib import Path
import shutil

readme_address = Path(__file__).parent.parent/'README.md'
destination = Path(__file__).parent.parent/'btd6bot/Files/helpwindow'

if not os.path.isdir(destination):
    os.mkdir(destination)
shutil.copy2(str(readme_address), destination/'README.md')