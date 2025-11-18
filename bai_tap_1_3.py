import math

def dien_tich_hinh_tron():
    try:
        r = float(input("Nhập bán kính hình tròn (r): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ cho bán kính.")
        return

    if r < 0:
        print("Lỗi: Bán kính không thể là số âm.")
        return

    dien_tich = math.pi * r ** 2

    print("-" * 30)
    print(f"Bán kính (r) = {r}")
    print(f"Diện tích hình tròn là: {dien_tich:.2f}")
    print("-" * 30)

dien_tich_hinh_tron()