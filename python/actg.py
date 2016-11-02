def within(h, l_s):
    return not any([i > l_s for i in h.values()])
def process(S):
    l_s = len(S)/4
    h = { 'A':0,'C':0,'T':0,'G':0}
    for c in xrange(len(S)):
        h[S[c]]+=1
        if h[S[c]] > l_s:
           h[S[c]]-=1
           break
    if c == len(S)-1: return 0
    mx_left = c-1 # inclusive
    right_index = len(S)
    min_count = 999999
    while mx_left >= 0 and mx_left < right_index:
         while mx_left >=0  and not within(h,l_s):
             h[S[mx_left]]-=1
             mx_left-=1
         if mx_left < 0 or not within(h,l_s): break
         cur_len = max(0, right_index - mx_left -1 )
         if cur_len < min_count:
             min_count = cur_len
         h[S[right_index-1]]+=1
         right_index-=1
    return min_count

N = input()
S = raw_input().strip()[:N]
print process(S)
