

=== Jump Directory ===

A command line program to jump between directories smartly

Author: Robby Boney


=== Install ===

1) edit the paths in the jd shell script to match the location of
the actual file for (jd.py & .jd-hist). also adjust the parameter

MAX_HIST_LEN = 100

in the jd.py file if you a history larger than 100 paths. duplicate 
paths are not recorded in the history.

2) add the following code to your shell rc file to include the script
to your current environment. this allows the script to cd the current
environment to other directories.

source /path/to/jd      or       . /path/to/jd

3) restart your shell, and enjoy smart directory jumping!!!

=== USAGE ===

To use this program, simply call 

~$ jd "some path"

jd will search for the path in the history of and jump to that path
if possible, else if provided a valid path that is not in record, jd
will add the path to the history. Because of this jd will function better
for you the more you use it.

ENJOY JUMPING!!!
