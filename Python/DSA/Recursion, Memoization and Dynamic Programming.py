# LONGEST COMMONG SUB-SEQUENCE(Inefficient)--->>>

# def len_of_lcs(seq1,seq2,idx1=0,idx2=0):
#     if idx1==len(seq1) or idx2==len(seq2):
#         return 0
#     elif seq1[idx1]==seq2[idx2]:
#         return 1+len_of_lcs(seq1,seq2,idx1+1,idx2+1)
#     else:
#         return max(len_of_lcs(seq1,seq2,idx1+1,idx2),len_of_lcs(seq1,seq2,idx1,idx2+1))

# LONGEST COMMON SUB-SEQUENCE(Efficient)--->>>
def len_of_lcs(seq1,seq2):
    reg = {}
    def memoization(idx1=0,idx2=0):
        key = (idx1,idx2)
        if key in  reg:
            return reg[key]
        elif idx1==len(seq1) or idx2==len(seq2):
            reg[key] = 0
        elif seq1[idx1]==seq2[idx2]:
            reg[key] = 1 + memoization(idx1+1, idx2+1)
        else:
            reg[key] = max(memoization(idx1+1,idx2),memoization(idx1,idx2+1))
        # print(reg)
        return reg[key]
    return memoization(seq1,seq2)

def lcs_dp(s1,s2):
    n1, n2 = len(s1), len(s2)
    table = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i]==s2[j]:
                table[i+1][j+1] = 1+table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1],table[i+1][j])
    return table[-1][-1]

# t0 = {"1":"serendipitous","2":"precipitation"} 
# t1 = {"1":[1, 3, 5, 6, 7, 2, 5, 2, 3],"2":[6, 2, 4, 7, 1, 5, 6, 2, 3]}
# t2 = {"1":"longest","2":"stone"}
# t3 = {"1":"asdfwevad","2":"opkpoiklklj"}
# t4 = {"1":"dense","2":"condensed"}
# t5 = {"1":"","2":"opkpoiklklj"}
# t6 = {"1":"","2":""}
# t7 = {"1":"abcdef","2":"badcfe"}
# print(len_of_lcs("serendipitous","precipitation"))
# test_cases = [t0,t1,t2,t3,t4,t5,t6,t6,t7]
# for i in test_cases:
    # print(len_of_lcs(i["1"],i["2"]))
    # print(lcs_dp(i["1"],i["2"]))
# print(lcs_dp("no","lon"))

# 0-1 KNAPSACK (Recursive)(Inefficient)--->>>
def max_profit(weights,profits,capacity,idx=0):
    if idx==len(profits):
        return 0
    elif weights[idx]>capacity:
        return max_profit(weights,profits,capacity,idx+1)
    else:
        return max(max_profit(weights,profits,capacity,idx+1), profits[idx]+max_profit(weights,profits,capacity-weights[idx],idx+1))
        
# 0-1 KNAPSACK (Recursive)(with Memoization)(Inefficient)--->>>
def max_profit_memoization(weights,profits,capacity):
    cache = {}
    def main(capacity,idx=0):
        pair = (capacity,idx)
        if pair in cache:
            return cache[pair]
        elif idx==len(weights):
            return 0
        elif weights[idx]>capacity:
            cache[pair] = main(capacity,idx+1)
        else:
            cache[pair] = max(main(capacity,idx+1), profits[idx]+main(capacity-weights[idx],idx+1))
        return cache[pair]
    return main(capacity)

# 0-1 KNAPSACK (DYNAMIC PROGRAMMING)(EFFICIENT)--->>>
def knapsack_dp(weights,profits,capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(capacity):
            if weights[i]>j+1:
                table[i+1][j+1] = table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1],profits[i]+table[i][(j+1)-weights[i]])
    for i in table:
        print(i)
        # print(i*2)
    return table[-1][-1]

t0 = {"weights":[23, 31, 29, 44, 53, 38, 63, 85, 89, 82], "profits":[92, 57, 49, 68, 60, 43, 67, 84, 87, 72], "capacity":165}
t1 = {"weights":[4, 5, 6], "profits":[1, 2, 3], "capacity":3}
t2 = {"weights":[4, 5, 1], "profits":[1, 2, 3], "capacity":4}
t3 = {"weights":[41, 50, 49, 59, 55, 57, 60], "profits":[442, 525, 511, 593, 546, 564, 617], "capacity":170}
t4 = {"weights":[4, 5, 6], "profits":[1, 2, 3], "capacity":15}
t5 = {"weights":[4, 5, 1, 3, 2, 5], "profits":[2, 3, 1, 5, 4, 7], "capacity":15}
# t5 = {"weights":[2, 3, 3, 4, 6], "profits":[1, 2, 5, 9, 4], "capacity":10}
test_cases = [t0,t1,t2,t3,t4,t5]
for i in test_cases:
    # print(max_profit_memoization(i["weights"],i["profits"],i["capacity"]))
    print(knapsack_dp(i["weights"],i["profits"],i["capacity"]))