n=int(input("Nhap so n: "))
tong=0
for i in range (1, n+1):
 tong= tong + i
 print(f"+ Thêm {i} → Tổng: {tong}")
print(f"Kết quả: 1 + 2 + ... + {n}={tong}")