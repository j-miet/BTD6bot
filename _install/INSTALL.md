## How to install BTD6bot using an install script file

- [<u>Scripts</u>](#scripts)
    - [For Windows users](#for-windows-users)
- [<u>Optional</u>](#optional)
    - [Global installation](#global-installation)
- [<u>Detailed explanation of scripts</u>](#detailed-explanation-of-scripts)
    - [Windows](#windows)
        - [Install.bat](#installbat)
        - [Other .bat scripts](#other-bat-scripts-located-in-win_copy-directory)
    - [Linux/MacOS](#linuxmacos)
        - [Install.sh](#installsh)
        - [Other .sh scripts](#other-sh-scripts-located-in-other_copy-directory)


## Scripts

- *win* includes **install.bat** which has ``.bat`` format and uses Windows Powershell to execute commands and 
therefore cannot be run on non-Windows systems
 - *other* includes **install.sh** which has ``.sh`` format which requires 'bash': this is included in Mac and Unix 
 systems by default but not on Windows

<u>Both 'install.sh' and 'install.bat' will automatically perform following operations</u>:

 1. download the Btd6bot github main branch zip file to directory where script is (e.g. ``c:/your/path/install.sh`` -> 
 running script produces ``c:/your/path/main.zip``)
 2. unzip the contents into './BTD6bot-main' directory (e.g. ``c:/your/path/BTD6bot-main``)
    - (*install.bat* only) check if existing 'BTD6bot-main' directory exists in this location; if it does then remove 
    this before unzipping the new one
 3. remove zip file
 4. set working directory to ./BTD6bot-main/
 5. copy all script files from ``BTD6bot-main/_install/{script-type}/_copy``:
    - *run* and *run-nogui* are copied into root directory 'BTD6bot-main'
    - tool scripts are copied into their respective tool directories under 'BTD6bot-main/tools/tool_name'
    
    -> Therefore you should not edit or copy these files manually!
 6. create a virtual environment in 'BTD6bot-main/.venv' using Python standard library venv command 
 **python -m venv ./.venv**
 7. activate the virtual environment so all external packages are installed under venv locally instead mixing them with
  global package collection
 8. install all packages with **pip install -r requirements.txt** under your currently activate virtual environment


### For Windows users

From https://docs.python.org/3/library/venv.html#creating-virtual-environments


>On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the 
user. You can do this by issuing the following PowerShell command:
>
>PS C:\> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

=> This means Windows users might need to run following command in powershell in order to allow use of virtual environments:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


## Optional 

### Global installation

If for some reason you'd prefer a manual installation, for example 
- you wish to enable ocr gpu support for bot (you can still do this with script installation, just need to install pytorch+cuda locally to venv),
- you couldn't get the install script to work,

then you can

1. Download source files
   - clone the repo from https://github.com/j-miet/BTD6bot.git

    OR

   - *github*: download ZIP file
 

2. (optional) create and activate a virtual environment for local install; this way all required python packages reside under 
    same local location as other bot files and importantly don't bloat your global Python package collection.


3. Install packages via command

	    pip install -r -requirements.txt

   >This installs packages globally unless you have venv activated

   - (Windows/Linux only; Mac has no CUDA support)

        If you'd like to install pytorch gpu CUDA support, uninstall existing cpu packages

   	    pip uninstall torch torchvision

        then go to https://pytorch.org/get-started/locally/ and follow instructions

3. Run bot with following command
        
        python btd6bot


## Detailed explanation of scripts

### Windows

#### install.bat

    powershell -NoProfile -Command ^

Executes script in powershell without loading user's profile (e.g. Microsoft or powershell profile file)

    Invoke-WebRequest 'https://github.com/j-miet/BTD6bot/archive/refs/heads/main.zip' -Outfile './main.zip' ^

Sends a web request to BTD6bot github project url to retrieve data from main branch as a zip file, then downloads this zip and saves it in './main.zip' i.e. current script run directory. So if your install.bat is located in 'C:/your/path/install.bat' then zip file becomes 'C:/your/path/main.zip'

    if (Test-Path ./BTD6bot-main) { ^

    Remove-Item './BTD6bot-main' -Recurse -Force -Confirm:$false ^

    } ^

Checks if previous BTD6bot-main directory exists in script run directory. If yes, **delete entire directory**.

    Expand-Archive -Path './main.zip' -DestinationPath '.' ^

Unzips the main.zip into current directory. Github names the project directory as {project_name}-{branch} -> this means after unzip, bot files are located in C:/your/path/BTD6bot-main

    Remove-Item './main.zip' ^

After unzip auto-delete the zip file

    Set-Location "./BTD6bot-main/" ^

Change current directory location inside bot dir

    Copy-Item './_install/win/_copy/run.bat' -Destination './run.bat' ^

Copies run.bat scripts from _install directory so it can be found in c:/your/path/BTD6bot-main/run.bat.

    Copy-Item './_install/win/_copy/run-nogui.bat' -Destination './run-nogui.bat' ^

Like before, copies the no-gui.bat script into root dir

    Copy-Item './_install/win/_copy/show_coordinates.bat' -Destination './tools/show_coordinates/run.bat' ^

    Copy-Item './_install/win/_copy/move_mouse.bat' -Destination './tools/move_mouse/run.bat' ^

    Copy-Item './_install/win/_copy/image_scaler.bat' -Destination './tools/image_scaler/run.bat' ^

    Copy-Item './_install/win/_copy/command_tracker.bat' -Destination './tools/command_tracker/run.bat' ^

These commands copy tooling scripts into their respective dirs under c:/your/path/BTD6bot-main/tools/tool_name/tool_name.bat

    python -m venv ./.venv ^

Setup a python virtual environment so all packages from requirements.txt are installed locally and don't interfere with global package space. Virtual environment files are found under c:/your/path/BTD6bot-main/.venv

    ./.venv/Scripts/activate ^

Activate virtual environment

    pip install -r requirements.txt

Install required external packages listed in requirements.txt. Because virtual environment is activated, these packages are installed locally under c:/your/path/BTD6bot-main/.venv/Lib/site-packages

#### Other .bat scripts (located in win/_copy directory)

    powershell -NoProfile -Command ^

    ./.venv/Scripts/activate ^

    python btd6bot

These all follow similar pattern:
1. run script in powershell without a user profile
2. activate virtual environment so script can access locally installed packages
3. run main file using Python
    - if run/run no-gui, uses 'python btd6bot'. This is same as 'python btd6bot/\_\_main\_\_.py'.
    - for tool scripts, uses 'python tool_name.py'

### Linux/macOS

<u>Important</u>
- scripts have not been tested outside Windows environment yet
- Bot has not been tested on Linux. MacOS compatibility is also largely untested.

#### install.sh

    #!/usr/bin/env bash

Search your PATH, find bash executable then run script with this bash version

    chmod +x install.sh

Allow install.sh operate as an executable

    curl -OL https://github.com/j-miet/BTD6bot/archive/refs/heads/main.zip

Client url command sends request to download main.zip from BTD6bot github archive. Here -O means zip is saved with its original name 'main.zip', -L allows server redirects if main.zip cannot be downloaded directly from that github link. File will be downloaded into current working directory e.g. your path which could be c:/your/path. So running c:/your/path/install.sh results in c:/your/path/main.zip

    unzip main.zip

Unzips main.zip contents into 'c:/your/path/BTD6bot-main' directory. Github defaults directory names to {project_name}-{branch} which is why it becomes 'BTD6bot-main'

    rm main.zip

After unzip, auto-remove zip file

    cd ./BTD6bot-main/

Change working directory to BTD6bot install folder

    cp ./_install/other/_copy/run.sh ./run.sh
    cp ./_install/other/_copy/run-nogui.sh ./run-nogui.sh

Copy bot running scripts (gui and without gui) into bot root folder

    cp ./_install/other/_copy/show_coordinates.sh ./tools/show_coordinates/run.sh
    cp ./_install/other/_copy/move_mouse.sh ./tools/move_mouse/run.sh
    cp ./_install/other/_copy/image_scaler.sh ./tools/image_scaler/run.sh
    cp ./_install/other/_copy/commands_tracker.sh ./tools/command_tracker/run.sh

For tool scripts, copy them into their respective tool directories under c:/your/path/BTD6bot-main/tools

    python3 -m venv ./.venv

Setup a virtual environment so all external packages are installed locally under c:/your/path/BTD6bot-main/.venv dir and don't interfere with global package space

    if [[ "$OSTYPE" == "msys" || "OSTYPE" == "cygwin" ]]; then
        source ./.venv/Scripts/activate
    else
        source ./.venv/bin/activate
    fi

Activate virtual environment. If operating system is Windows (msys/cygwin), use first path. If not, use second path.

    pip3 install -r requirements.txt

In current virtual environment, install external packages listed in requirements.txt. These can then be found in c:/your/path/BTD6bot-main/.venv/Lib/site-packages


#### Other .sh scripts (located in other/_copy directory)

    #!/usr/bin/env bash
    chmod +x run.sh
    if [[ "$OSTYPE" == "msys" ]]; then
        source ./.venv/Scripts/activate
    else
        source ./.venv/bin/activate
    fi
    python3 btd6bot

These all follow similar pattern:
1. run file using bash
2. treat file as a script by adding it executable permissions
3. activate virtual environment:
    - if Windows, run venv activation script in 'Scripts' dir (generally you want to use .bat script but this also works)
    -  otherwise run activation script in 'bin' dir
4. run main file using Python
    - if run/run no-gui, uses 'python3 btd6bot'. This is same as 'python3 btd6bot/\_\_main\_\_.py'.
    - for tool scripts, uses 'python3 tool_name.py'
   
   Note that specifying python version is required for Unix and some Mac systems, hence python3 is used.




