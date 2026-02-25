#!/usr/bin/env bash
chmod +x run-nogui.sh
if [[ "$OSTYPE" == "msys" ]]; then
	source ./.venv/Scripts/activate
else
	source ./.venv/bin/activate
fi
python3 btd6bot -nogui