n, m = map(int, input().split())
flag = []
valid = True

# Đọc các hàng
for i in range(n):
    s = input().strip()
    flag.append(s)

# Kiểm tra mỗi hàng có đồng nhất không?
for row in flag:
    if len(row) != m:
        valid = False
    else:
        first_char = row[0]
        for char in row:
            if char != first_char:
                valid = False
                break
    if not valid:
        break

# Kiểm tra các hàng liền kề có khác nhau không?
if valid:
    for i in range(1, n):
        if flag[i] == flag[i-1]:
            valid = False
            break

if valid:
    print("YES")
else:
    print("NO")