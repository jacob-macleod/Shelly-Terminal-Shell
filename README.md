# Shelly Terminal Shell
Version 2

## Shelly is a terminal shell written in python
![Sorry, this image cannot be displayed](https://github.com/jacob-macleod/Shelly-Terminal-Shell/blob/master/Screenshot%202020-07-08%20at%205.53.05%20PM.png "Shelly with the default theme")

## Installation:
To install Shelly, you can clone the repository: `git clone https://github.com/jacob-macleod/Shelly-Terminal-Shell.git`. To run Shelly, you can cd into the repository with `cd Shelly-Terminal-Shell` and run `python3 main.py`. 


## Set as default editor:
There are many ways to set Shelly as your default editor. One way is to add the following line in your .bashrc file, which should be located in your home directory: `python3 <path_to_shelly_installation>/main.py`. 
<br>Currently, Shelly only supports being run from the same folder where it is installed, so the easiest way to solve this is to move all your Shelly config files to your home directory, where your .bashrc file is located. This can be done by running `mv Shelly-Terminal-Shell/* $HOME` when in your home directory.
<br><br>However, this may not be ideal, since you may not want lots of files in your home directory. Therefore, you can keep Shelly in it's own folder by doing the following:
<br> ** Sorry, the below instructions are not valid - the code has been updated since! We'll update them asap. ***
<br>Replace line 7 in main.py with `command_history_location = <path_to_shelly_installation> + "/command_history.txt"`
<br>Replace line 24 in main.py with `with open("<path_to_shelly_installation>/shellyRC.txt") as rc:`
<br>Replace line 41 in main.py with `with open("<path_to_shelly_installation>/core_placeholder.py", "w") as f1:`
<br>Replace line 46 in main.py with `with open("<path_to_shelly_installation>/user_placeholder.py", "w") as f1:`
<br>You will need to make sure you have the correct indentation on these lines!
<br>Replace the file paths to the pluginns in shellyRC.txt with the absolute file paths, and please open an issue if there are any problems with this!

## Adding aliases
Shelly has support for aliases! To use this, add at least one line in shellyRC.txt containing `%"alias_name"="alias_command"`. Please open an issue if there are any problems!

## Contribution:
We would love any contributors! The issues labeled 'good first issue' are good things to contribute towards.

## Installing Plugins
Shelly can be easily updated through plugins. To install a plugin, you can just download one from the internet, or make one yourself (see below). Once the plugin is downloaded, you need to update your shellyRC.txt file to include the file path of your plugin. There are two types of plugins, core and user plugins. If you installed a core plugin, you can replace the line in your shellyRC.txt file starting with a '#' to `#Core-Plugin "<file_path_to_core plugin>"`
<br>If you installed a user plugin, you can replace the line in your shellyRC.txt starting with a '!' to `!User-Plugin "<file_path_to_core_plugin>"`

## Developing Plugins:
Shelly can be easily updated through plugins. There are two types of plugins, core and user plugins. Core plugins display the current directory the user is in and the username, for example `default@home/default/my_dir`. To write a plugin, create a .py file with a function called 'core'. The output of this function will be printed whenever the user presses a key. To create a plugin that prints the current directory the user is in, you first need to `import subprocesses as sp`, then inside the core function, enter `return sp.getoutput("pwd")`. This line can be augmented, for example, `return sp.getoutput("whoami") + "/" + sp.getoutput("pwd")`. You can also use ansi escape codes to add color - here's an example: `return "\033[31m" + sp.getoutput("whoami") + "\033[0m~" + "\033[34m" +  sp.getoutput("pwd") + "/\033[0m~$ "`
<br>User plugins determine what the user sees when they hit a key. They are developed in a similar way - except they use a function named 'user' instead of 'core'.
<br>Finally, you need to update shellyRC.txt file to include the file path of your plugin - see above for help
