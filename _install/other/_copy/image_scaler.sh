#!/usr/bin/env bash
chmod +x run.sh
if [[ "$OSTYPE" == "msys" ]]; then
	source ./../../.venv/Scripts/activate
else
	source ./../../.venv/bin/activate
fi
python3 image_scaler.py