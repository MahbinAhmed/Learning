# Link :- https://www.codechef.com/problems/TYRE

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    n_total = 2*n
    m_total = 4*m
    ans = n_total + m_total
    print(ans)