# fo4msm
Fallout 4 multiple save folders management tool




# requirements
 - Fallout 4
 - F4SE
 - python 2 / python 3

# installation
- copy 'main.py' and 'config.json' from the root directory (of this repository) into the folder where F4SE ('f4se_loader.exe') is located
- update the content of 'config.json' and set the directory path of your Fallout 4 save folder as "directory" value
- copy 'version_data.json' from '/example_save' into the 'Save' folder where all saves are listed
-> update 'version_data.json' to match your wishes:
 - "description" -> an alias name for the save directories listing
 - "folderName" -> will be used as suffix for every save directory if it isn't used as current save diroty for Fallout 4
    "additionalContents" -> possible comments for the save can be added here (each comment must be within double quotes and comments must be separated via a comma)
-> for multiple save directories new save folders can be created
 - all save directories must be in the same parent directory
 - all save directory names exact the active one must be named like this: 'Saves_[folderName value from version_data.json]'
