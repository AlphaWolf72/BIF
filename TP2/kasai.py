def lcp_kasai(s, sa, inv):
    n = len(sa)
    l = 0
    lcp = [0]*(n)
    for i in range(n):
        if inv[i] > 0:
            k = inv[i]
            j = sa[k-1]
            while i+l < n and j+l < n and s[i+l] == s[j+l]:
                l+=1
            lcp[k] = l
            if l>0 : 
                l-=1
    return lcp
