# fo4msm
Fallout 4 multiple save directories management tool


A simple multiple save directories management tool to switch between mulitple save directories when starting Fallout 4. This tool requires F4SE, but should run Fallout 4 directly (without F4SE) with little changes.

On program start a list of all save directories will be listed. For every save directory (except the 'active' directory [that Fallout 4 uses]) an entry is listed and can be made to the active directory via button click.
The button next to the active directory start F4SE itself.


# requirements
 - Fallout 4
 - F4SE (should run without F4SE with little changes)
 - python 2 / python 3

# installation
- copy 'main.py' and 'config.json' from the root directory (of this repository) into the folder where F4SE ('f4se_loader.exe') is located
- update the content of 'config.json' and set the directory path of your Fallout 4 save folder as "directory" value
- copy 'version_data.json' from '/example_save' into the 'Save' folder where all saves are listed
- update 'version_data.json' to match your wishes:
  - "description" -> an alias name for the save directories listing
  - "folderName" -> will be used as suffix for every save directory if it isn't used as current save diroty for Fallout 4
    "additionalContents" -> possible comments for the save can be added here (each comment must be within double quotes and comments must be separated via a comma)
- for multiple save directories new save folders must be created
  - all save directories must be in the same parent directory
  - all save directory names exact the active one must be named like this: 'Saves_[folderName value from version_data.json]'

# usage
- launch via steam: add new external game/program
   - set 'python.exe' as TARGET   (example: "C:/[path to python directory]/python.exe")
   - set 'main.py' as LAUNCH OPTION(S)   (example: "C:/[path to Fallout 4 directory]/main.py")
