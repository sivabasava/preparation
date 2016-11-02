# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def process_helper(a, b, start):
    bi = 0
    flag = 0
    ah = {}
    for ac in a:
        if ac.isupper():
            ah[ac] = ah.get(ac,0)+1

    for i in xrange(start, len(a)):
        if bi == len(b):
            for ac in a[i:]:
                if ac.isupper():
                    return 'NO'
            return 'YES'
        if a[i].isupper():
            if a[i] == b[bi]:
                bi += 1
                ah[a[i]] -= 1
            else: #got a caps not matching cant proceed
                return 'NO'
        else: #a[i] is lower
            if a[i].upper() == b[bi]:
                if a[i].upper() in ah and ah[a[i].upper()] >= b[bi:].count(a[i].upper()): # there is a caps one following
                    pass
                else:
                    bi += 1

    if bi == len(b):
        return 'YES'
    return 'NO'

from sets import Set
def process(a, b):
    c = Set([ac for ac in a if ac.isupper() and ac not in b]).difference(Set(list(b)))
    if len(c) != 0:
        return 'NO'
    bh = {}
    for bc in b:
        bh[bc] = bh.get(bc,0)+1

    ah = {}
    for ac in a.upper():
        ah[ac] = ah.get(ac,0)+1

    for k in b:
        if k in ah and ah[k] < bh[k]:
            return 'NO'

    for m in re.finditer(b[0].lower(), a.lower()):
        if process_helper(a, b, m.start()) == 'YES':
            return 'YES'
    return 'NO'

for _ in xrange(input()):
    a = raw_input().strip()
    b = raw_input().strip()
    print process(a, b)