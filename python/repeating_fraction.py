'''
1/3=0.33333 output 0.(3), put paranthesis around repeating fraction
'''
def get(n,d):
    print '%d/%d --> '%(n,d),
    sub = {} # to hold division subs
    quotients = []
    prefix = 0
    if n > d:
         prefix = n/d
         n%=d
    index = 0
    while n>0:
       q = n*10/d  
       n = n*10%d
       quotients.append(q)
       if n in sub:
          break
       sub[n]=index
       index+=1

    print '%d.%s(%s)'%(prefix,''.join(map(str,quotients[:sub[n]])),''.join(map(str,quotients[sub[n]:index])))
      
for (numerator,denominator) in [ (1,3),(4,7),(10,9),(25,99),(22,7),(122,999)]:
    get(numerator, denominator)
        
