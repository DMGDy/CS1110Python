#!/usr/bin/python


def m2(cl):
    pl = 0
    cl = str(''.join(cl))
    clchk = cl[::-1]
    if cl == clchk:
        pl = 1
    else:
        pl = 0
    if pl == 1:
        print("These letters form a palindrome.")
    if pl == 0:
        print("These letters do not form a palindrome.")
