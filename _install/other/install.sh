#!/usr/bin/env bash
chmod +x install.sh
curl -OL https://github.com/j-miet/BTD6bot/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
cd ./BTD6bot-main/
cp ./_install/other/_copy/run.sh ./run.sh
cp ./_install/other/_copy/run-nogui.sh ./run-nogui.sh
cp ./_install/other/_copy/show_coordinates.sh ./tools/show_coordinates/run.sh
cp ./_install/other/_copy/move_mouse.sh ./tools/move_mouse/run.sh
cp ./_install/other/_copy/image_scaler.sh ./tools/image_scaler/run.sh
cp ./_install/other/_copy/commands_tracker.sh ./tools/command_tracker/run.sh
python3 -m venv ./.venv
if [[ "$OSTYPE" == "msys" || "OSTYPE" == "cygwin" ]]; then
	source ./.venv/Scripts/activate
else
	source ./.venv/bin/activate
fi
pip3 install -r requirements.txt