def phan_nguyen_va_phan_du():
    try:
        a = int(input("Nhập số nguyên dương a: "))
        b = int(input("Nhập số nguyên dương b: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên dương hợp lệ.")
        return

    if a <= 0 or b <= 0:
        print("Lỗi: a và b phải là số nguyên dương.")
        return

    phan_nguyen = a // b
    phan_du = a % b

    print("-" * 30)
    print(f"Phần nguyên của {a} chia {b} là: {phan_nguyen}")
    print(f"Phần dư của {a} chia {b} là: {phan_du}")
    print("-" * 30)

phan_nguyen_va_phan_du()