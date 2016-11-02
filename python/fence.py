def process():        
    up = [[0 for i in xrange(M)][:] for j in xrange(N)]
    left = [[0 for i in xrange(M)][:] for j in xrange(N)]
    for i in xrange(1,N):
        for j in xrange(0,M):
            if L[i][j]=='x': 
                up[i][j]=0
            elif L[i-1][j]=='.':
                up[i][j]=up[i-1][j]+1
            elif L[i-1][j]=='x':
                up[i][j]=0
            
    for i in xrange(0,N):
        for j in xrange(1,M):
            if L[i][j]=='x': 
                left[i][j]=0
            elif L[i][j-1]=='.':
                left[i][j]=left[i][j-1]+1
            elif L[i][j-1]=='x':
                left[i][j]=0
    mx_perimeter = 0
    for i in xrange(N-1,0,-1):
        for j in xrange(M-1,0,-1):
            if L[i][j]=='x' or (up[i][j]+left[i][j])*2 < mx_perimeter: continue
            for ui in xrange(up[i][j],0,-1):
                for sui in xrange(min(left[i-ui][j],left[i][j]),0,-1):
                    # compute perimeter
                    length = min(up[i][j-sui],ui)
                    if ui != length or 0 in [ui, length]: 
                        continue
                    perimeter = (sui+ui)*2
                    if perimeter > mx_perimeter:
                        mx_perimeter = perimeter
                    break
    if mx_perimeter <= 0: return 'impossible'
    return mx_perimeter
 
#N = 136
#M = 91
#L = []
#for line in open('f3_24').read().split('\n')[1:-1]:
#    L.append(list(line)[:M])
#print process()
#exit()
#N,M=(4,5)
#L=[
#['.','.','.','.','.'],
#['.','x','.','x','.'],
#['.','.','.','.','.'],
#['.','.','.','.','.']
#]
#print process()
#exit()

N,M=map(int, raw_input().strip().split(' '))
L = []
for _ in xrange(N):
    L.append(list(raw_input().strip()[:M]))

print process()
