## How to install BTD6bot via install script

## Scripts

- *win* includes **install.bat** which has ``.bat`` format and uses Windows Powershell to execute commands and 
therefore cannot be run on non-Windows systems
 - *other* includes **install.sh** which has ``.sh`` format which requires 'bash': this is included in Mac and Unix 
 systems by default but not on Windows

<u>Both 'install.sh' and 'install.bat' will automatically perform following operations</u>:

 1. download the Btd6bot github main branch zip file to directory where script is (e.g. ``c:/CUSTOM_DIR/install.sh`` -> 
 running script produces ``c:/CUSTOM_DIR/main.zip``)
 2. unzip the contents into './BTD6bot-main' directory (e.g. ``c:/CUSTOM_DIR/BTD6bot-main``)
    - (*install.bat* only) check if existing 'BTD6bot-main' directory exists in this location; if it does then remove 
    this before unzipping the new one
 3. remove zip file
 4. set working directory to ./BTD6bot-main/
 5. copy all script files from ``BTD6bot-main/_install/{script-type}/_copy``:
    - *run* and *run-nogui* are copied into root folder 'BTD6bot-main'
    - tool scripts are copied into their respective tool directories under 'BTD6bot-main/tools/tool_name'
    
    -> Therefore you should not edit or copy these files manually!
 6. create a virtual environment in 'BTD6bot-main/.venv' using Python standard library venv command 
 **python -m venv ./.venv**
 7. activate the virtual environment so all external packages are installed under venv locally instead mixing them with
  global package collection
 8. install all packages with **pip install -r requirements.txt**


### For Windows users

From https://docs.python.org/3/library/venv.html#creating-virtual-environments


>On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the 
user. You can do this by issuing the following PowerShell command:
>
>PS C:\> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

=> This means Windows users might need to run following command in powershell in order to allow use of virtual environments:

**Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser**


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

	