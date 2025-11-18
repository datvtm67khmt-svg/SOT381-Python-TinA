def tong_cap_so_cong():
    try:
        a1 = float(input("Nhập số hạng đầu (a1): "))
        d = float(input("Nhập công sai (d): "))
        n = int(input("Nhập số lượng số hạng (n, nguyên dương): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ.")
        return

    if n <= 0:
        print("Lỗi: Số lượng số hạng (n) phải là số nguyên dương.")
        return

    an = a1 + (n - 1) * d
    
    tong_sn = n * (a1 + an) / 2

    print("-" * 40)
    print(f"Cấp số cộng: a1={a1}, d={d}, n={n}")
    print(f"Số hạng cuối (an): {an}")
    print(f"Tổng cấp số cộng (Sn) là: {tong_sn:.2f}")
    print("-" * 40)

tong_cap_so_cong()