#!/usr/bin/env python3

# ========================== Global Vars
MAX_HIST_LEN = 100

# ========================== Imports modules
import os
import sys


# ========================== program functions
def seekTerm(x, L):
    
    # first check folders at farthest depth
    for t in L:
        if x in t.split("/")[-1]:
            return (t, 0)

    p = os.getcwd()+"/"+x
    if os.path.exists( os.path.abspath(x) ):
        return ( os.path.abspath(x), 1 )
    elif os.path.exists( p ):
        return ( p, 1 )

    # check entire paths for matches
    for t in L:
        if x in t:
            return (t, 0)

    exit("ERROR: could not find path ({})".format( p ))


# ========================== main function
def main():

    argc = len(sys.argv)
    if argc > 3:
        exit("ERROR: invalid number of arguments")
    elif argc == 2:
        return 0
    elif argc == 3:
        # show .jd-hist file in terminal output
        if sys.argv[2] == "--show":
            hist = open(sys.argv[1], "r")
            hist_fd = hist.read().splitlines()
            for i in range(len(hist_fd)):
                print("{}...{}".format(1+i, hist_fd[i]))
            return 0
        else:
            seek = sys.argv[2]
    else:
        return 0

    hist = open(sys.argv[1], "r")
    hist_fd = hist.read().splitlines()
    hist.close()

    res = seekTerm(x=seek, L=hist_fd)
    global MAX_HIST_LEN
    i = 0
    if res[1]:
        hist = open(sys.argv[1], "w+")
        hist_fd = [res[0]] + hist_fd
        for ln in hist_fd:
            if i >= MAX_HIST_LEN:
                break
            hist.write(ln + "\n")
            i+=1
        hist.close()

    elif res[1] == 0:
        hist = open(sys.argv[1], "w+")
        hist.write(res[0] + "\n")
        for ln in hist_fd:
            if i >= MAX_HIST_LEN:
                break
            if ln != res[0]:
                hist.write(ln + "\n")
            i+=1

        hist.close()

    print(res[0])
    return 0


if __name__ == '__main__':
    main()
