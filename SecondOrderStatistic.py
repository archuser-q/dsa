n = int(input())
array = list(map(int, input().split()))
array = sorted(set(array))
if len(array) > 1:
    min_value = min(array)
    for i in array:
        if i > min_value:
            print(i)
            break
else:
    print("NO")