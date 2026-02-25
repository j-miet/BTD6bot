powershell -NoProfile -Command ^

Invoke-WebRequest 'https://github.com/j-miet/BTD6bot/archive/refs/heads/main.zip' -Outfile './main.zip' ^

if (Test-Path ./BTD6bot-main) { ^

Remove-Item './BTD6bot-main' -Recurse -Force -Confirm:$false ^

} ^

Expand-Archive -Path './main.zip' -DestinationPath '.' ^

Remove-Item './main.zip' ^

Set-Location "./BTD6bot-main/" ^

Copy-Item './_install/win/_copy/run.bat' -Destination './run.bat' ^

Copy-Item './_install/win/_copy/run-nogui.bat' -Destination './run-nogui.bat' ^

Copy-Item './_install/win/_copy/show_coordinates.bat' -Destination './tools/show_coordinates/run.bat' ^

Copy-Item './_install/win/_copy/move_mouse.bat' -Destination './tools/move_mouse/run.bat' ^

Copy-Item './_install/win/_copy/image_scaler.bat' -Destination './tools/image_scaler/run.bat' ^

Copy-Item './_install/win/_copy/command_tracker.bat' -Destination './tools/command_tracker/run.bat' ^

python -m venv ./.venv ^

./.venv/Scripts/activate ^

pip install -r requirements.txt
