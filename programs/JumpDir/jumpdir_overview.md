
# Jump Directory
An evolution of the famous change directory (cd) program, jd allows the user to jump from a directory to another directory which has previously been jumped to.

---

## How it works
Jump directory allows the user to jump from directories based on previous jumps to those paths. All paths are stored in a file `.jd-hist` which is treated as a stack where most recent paths are moved to the top of the file. This changes the priority of paths based on their use, as more recently used paths will be closer to the top of the que and thereby aquired first if two paths with a same name exist in the `.jd-hist` file.

When searching through the history of paths, priority is given first to the first occurence of the search term in the name of the deepest directory only, then if no hits are found, a second scan is performed searching the entire path in the history. if no results are found then a simple `cd` is attempted and if successful the path is added to the `.jd-hist` file.

## Setup
** also viewable from readme.txt and source code **

#### Step 1: clone repo or download
first clone this repo to your desired location using

`git clone https://github.com/HarmonicHemispheres/SuperScripts.git`

or download to a local directory.


#### Step 2: move files and set paths
Edit the paths in the `jd` shell script to match the absolute path of the actual files for (`jd.py` & `.jd-hist`). 

OPTIONAL: Adjust the parameter `MAX_HIST_LEN = 100` in `jd.py` if you want the stored number of paths to be different.

NOTE: paths stored are unique and are not duplicates.

#### Step 3: add path to current environment
Add the following code to your shell rc (i.e. ~/.bashrc) file to include the script to your current environment. This allows the program to run cd in the current environment to other directories.

`source /path/to/jd`      or       `. /path/to/jd`

#### Step 4: Restart your shell, and start jumping!!!

## Use and Commands

* To view all current paths stored in the history run:

    `jd --show`

* To jump to a stored path or cd to directory in current path:
    
    `jd /path/to/jump/to`


## Notes
I highly recomend using an advanced shell such as [ZSH](http://ohmyz.sh/) because tab-autocomplete for paths using cd or jd is much nicer than bash.

## Contact Author

robby.boney@harmonichemispheres.com