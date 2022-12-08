n = int(input())
arr = list(map(int, input().split()))
maxi=0
for i in arr:
    if i>maxi:
        maxi=i
max2=0
for j in arr:
    if j>max2 and j<maxi:
        max2=j
print(max2)
