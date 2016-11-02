def poison(A):
    if len(A)==0: return 0
    stack = A[0]
    queue = []
    mx_days = 0
    for i in xrange(1,len(A)):
        if A[i] <= stack:
            stack = A[i]
            queue = []
        else:
           shield = 0
           while len(queue) and queue[-1][0] > A[i]:
              shield = max(queue[-1][1], shield)
              del queue[-1]
           if len(queue)==0:
               queue.append((A[i],shield+1))
           elif queue[-1][0] < A[i]:
               if shield == 0:
                   queue.append((A[i],1))
               else:
                   queue.append((A[i],shield+1))
           elif queue[-1][0] == A[i]:
               queue.append((A[i],queue[-1][1]+1))
           mx_days = max(mx_days, queue[-1][1])

    if len(queue) == 0: return 0
    return mx_days
        
#N=17
#A = [ 20,5,6,15,2,2,17,2,11,5,14,5,10,9,19,12,5]
#print poison(A)
#exit()
#N = 7
#A = [6,5,8,4,7,10,9]
#print poison(A)
#exit()
   
N = input()
A = map(int, raw_input().strip().split(' '))[:N]
print poison(A)
