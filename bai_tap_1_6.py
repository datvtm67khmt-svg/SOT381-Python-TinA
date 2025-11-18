import math

def chu_vi_dien_tich_tam_giac():
    try:
        a = float(input("Nhập độ dài cạnh thứ nhất (a): "))
        b = float(input("Nhập độ dài cạnh thứ hai (b): "))
        c = float(input("Nhập độ dài cạnh thứ ba (c): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ.")
        return

    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        print("Lỗi: Ba cạnh này không tạo thành một tam giác.")
        return

    chu_vi = a + b + c
    nua_chu_vi = chu_vi / 2
    
    dien_tich = math.sqrt(nua_chu_vi * (nua_chu_vi - a) * (nua_chu_vi - b) * (nua_chu_vi - c))

    print("-" * 40)
    print(f"Ba cạnh tam giác: a={a}, b={b}, c={c}")
    print(f"Chu vi tam giác là: {chu_vi:.2f}")
    print(f"Diện tích tam giác là: {dien_tich:.2f}")
    print("-" * 40)

chu_vi_dien_tich_tam_giac()