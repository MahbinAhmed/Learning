# Link :- https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def mutate_string(string, position, character):
    list1 = list(string)
    list1[position] = character
    final = "".join(list1)
    return final

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)