# input
n = str(input())
# only break ending
while True:
    # integer sum
    s = sum(map(int,str(n)))
    if len(str(n)) <= 1:
        break
    n = s
print(s)
