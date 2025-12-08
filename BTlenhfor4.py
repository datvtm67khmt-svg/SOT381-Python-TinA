n=int(input("Nhập số n: "))
tong_le = 0
print(f"Các số lẻ từ 1 đến {n}:")    

for i in range(1, n+1, 2):
    tong_le= tong_le + i
    print(f"+{i}")
print(f"Tổng số lẻ: {tong_le}")