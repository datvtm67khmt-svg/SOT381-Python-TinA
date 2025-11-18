def dien_tich_tam_giac_toa_do():
    try:
        x1 = float(input("Nhập tọa độ x1 của đỉnh A: "))
        y1 = float(input("Nhập tọa độ y1 của đỉnh A: "))
        x2 = float(input("Nhập tọa độ x2 của đỉnh B: "))
        y2 = float(input("Nhập tọa độ y2 của đỉnh B: "))
        x3 = float(input("Nhập tọa độ x3 của đỉnh C: "))
        y3 = float(input("Nhập tọa độ y3 của đỉnh C: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập các giá trị số hợp lệ.")
        return

    # Công thức diện tích (Sarrus): S = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
    dien_tich = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    print("-" * 50)
    print(f"Tọa độ 3 đỉnh: A({x1},{y1}), B({x2},{y2}), C({x3},{y3})")
    print(f"Diện tích tam giác là: {dien_tich:.3f}")
    print("-" * 50)

dien_tich_tam_giac_toa_do()