#https://codeforces.com/problemset/problem/2131/A
t = int(input())
count=0

for i in range(t):
    n = int(input())
    array1 = list(map(int,input().split()))
    array2 = list(map(int,input().split()))
    for i in range (n):
        if (array1[i]>array2[i]):
            count+=(array1[i]-array2[i])
    print(count+1)
    count=0