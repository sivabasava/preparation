import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(cmp=self.compare)
        doll_heights = []
        max_len = 0
        for envelope in envelopes:
            if envelope[1] in doll_heights: continue
            idx = bisect.bisect(doll_heights, envelope[1])
            print idx,max_len, envelopes,doll_heights
            if idx == max_len:
                max_len+=1
                doll_heights.insert(idx,envelope[1])
            else:
                doll_heights[idx]= envelope[1]
        print idx,max_len, envelopes,doll_heights
        return max_len
    def compare(self, x,y):
        if x[0] != y[0]:
            return x[0]-y[0]
        return y[1]-x[1]

print Solution().maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]])


def longest_increasing_subsequence(l):
    lis = []
    length = 0
    for i in l:
        idx = bisect.bisect_right(lis,i)
        print lis, l
        if idx == length:
            length+=1
            lis.insert(idx, i)
        else:
            lis[idx ] = i
    print lis
    return length

print longest_increasing_subsequence([1,3,1,2,5])
