a=int(input("nhap so a: "))
b=int(input("nhap so b: "))
c=int(input("nhap so c: "))
tong_trung_binh = ( a+ b + c )/3
print(f"Tong trung binh 3 so la: {tong_trung_binh}")
#viet ct nhap so n chia het cho 3 va 5
n=int(input("nhập số N: "))
if n%3 == 0 and n%5==0:
    print("n chia het cho 3 va 5")
else:
    print("n khong chia het cho 3 va 5")