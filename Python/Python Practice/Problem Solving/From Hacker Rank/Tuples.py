# Link :- https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

n = int(input())
integers = tuple(map(int, input().split()))
# integers = tuple(integers)

print(hash(integers))