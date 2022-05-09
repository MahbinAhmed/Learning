# Link :- https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen

def split_and_join(line):
    splitter = line.split(" ")
    splitter = "-".join(splitter)
    return splitter

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)