S = input().split(",")
N = int(input())

A1 = []

for i in S:
    A1.append(int(i))

print(max(A1[N:]))