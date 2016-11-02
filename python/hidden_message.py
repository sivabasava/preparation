import re
t = raw_input()
p = raw_input().split()
#t='bbbab'
#p = 'ab b'.split(' ')
pos = []

for word in p:
    wordpos = [ i.start() for i in re.finditer(r'(?=(%s))'%word,t)]
    #print word, wordpos
    pos.append(wordpos)
def pick(pos,i,chosen=[]):
    if len(chosen) == len(pos):
        return (chosen, True)
    for p_i in pos[i]:
        if len(chosen) == 0 or p_i > chosen[-1]:
            chosen.append(p_i)
            c,f = pick(pos,i+1,chosen)
            if f == False:
                chosen.pop(-1)
                continue
            else:
                return (chosen, True)
    return (chosen, False)

chosen, flag = pick(pos, 0)

if len(chosen) != len(p):
    print 'NO'
    start = 0
    printed = False
    for word in p:
        wordpos = [ i.start() for i in re.finditer(r'(?=(%s))'%word,t[start:])]
        #print word, wordpos
        if len(wordpos) != 0:
            print '%s %d %d'%(word, wordpos[0], wordpos[0]+len(word)-1),
            start = wordpos[0]+len(word)
            if printed == False:
                printed = True
        else:
            break # as it will break longest prefix sequence constraint
    if printed == False:
        print 0
    else:
        print
    print 0
else:
    print 'YES'
    intervals = []
    for i in xrange(len(p)):
        print '%s %d %d'%(p[i],chosen[i],chosen[i]+len(p[i])-1),
        intervals.append((chosen[i],chosen[i]+len(p[i])-1))
    print 
    #cost
    delete_cost = intervals[0][0]-0+len(t)-1-intervals[-1][1]

    current_interval = intervals[0]
    overlap_cost = 0
    for i in intervals[1:]:
        if i[0] <= current_interval[1]:
            overlap_cost += current_interval[1]-i[0]+1
            current_interval = (current_interval[0],i[1])
        else:
            delete_cost+=i[0]-current_interval[1]-1
            current_interval = (current_interval[0],i[1])
    print delete_cost+len(intervals)-1+overlap_cost
        
