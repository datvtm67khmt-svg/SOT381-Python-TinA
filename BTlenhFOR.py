n = int(input("Nhập n: "))
tong = 0
for i in range (1, n +1):
     tong = tong + i
     if tong>n:
      continue
ket_qua = tong
print(f"Tổng từ 1 đến {n} là :{ket_qua}")