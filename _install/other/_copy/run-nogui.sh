#!/usr/bin/env bash
if [[ "$OSTYPE" == "msys" ]]; then
	source ./.venv/Scripts/activate
else
	source ./.venv/bin/activate
fi
python3 btd6bot -nogui