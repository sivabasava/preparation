# Enter your code here. Read input from STDIN. Print output to STDOUT

class Trie:
    class Node:
        def __init__(self, c):
            self.c = c
            self.freq = 1
            self.childs = {}
            self.next = None
        def copy(self,c):
            n = Trie.Node(c)
            n.freq = self.freq
            n.childs = dict( (k,v) for (k,v) in self.childs.items())
            return n
    def __init__(self):
        self.root = self.Node('/')
        self.root.freq = 0

    def addName(self, name, cur):
        if name[0] in cur.childs:
            existing = cur.childs[name[0]]
            if name == existing.c:
                existing.freq+=1
                cur.freq+=1
            else:
                comm = 0
                while comm < min(len(existing.c), len(name)) and existing.c[comm] == name[comm]:
                    comm+=1
                if comm == min(len(existing.c), len(name)):
                    if comm == len(existing.c):
                        if name[comm] in existing.childs:
                            cur.freq+=1
                            return self.addName(name[comm:],existing)
                        else:
                            newNode = self.Node(name[comm:])
                            existing.childs[name[comm]]=newNode
                    elif comm == len(name):
                        newNode = existing.copy(existing.c[comm:])
                        existing.childs = {}
                        existing.childs[existing.c[comm]]=newNode
                        existing.c = existing.c[:comm]
                    existing.freq+=1
                    cur.freq+=1
                else:
                    splitNode = existing.copy(existing.c[comm:])
                    existing.childs = {}
                    existing.childs[existing.c[comm]] = splitNode
                    existing.c = existing.c[:comm]
                    newNode = self.Node(name[comm:])
                    existing.childs[name[comm]]=newNode
                    existing.freq+=1
                    cur.freq+=1
        else: #not present    
            newNode = self.Node(name)
            cur.childs[name[0]]=newNode
            cur.freq+=1

    def find(self,s,cur):
        if cur == self.root:
            if len(s) > 0 and s[0] in cur.childs:
                cur = cur.childs[s[0]]
            else:
                return 0
        comm = 0
        while comm < min(len(cur.c), len(s)) and cur.c[comm] == s[comm]:
            comm+=1
        if comm == min(len(cur.c), len(s)):
            if comm == len(s):
                return cur.freq
            elif comm == len(cur.c):
                if s[comm] not in cur.childs:
                    return 0
                else:
                    return self.find(s[comm:],cur.childs[s[comm]])
        else:
            return 0

t = Trie()
for _ in xrange(input()):
    x,y = raw_input().strip().split(' ')
    if x == 'add':
        t.addName(y,t.root)
    elif x == 'find':
        print t.find(y,t.root)
        
