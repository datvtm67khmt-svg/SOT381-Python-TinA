import math

def van_toc_roi_tu_do():
    g = 9.8  
    try:
        h = float(input("Nhập độ cao (h) mà vật rơi (mét): "))
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ cho độ cao.")
        return

    if h < 0:
        print("Lỗi: Độ cao không thể là số âm.")
        return

    v = math.sqrt(2 * g * h)

    print("-" * 40)
    print(f"Độ cao (h) = {h} mét")
    print(f"Gia tốc trọng trường (g) = {g} m/s²")
    print(f"Vận tốc của vật khi chạm đất (v) là: {v:.2f} m/s")
    print("-" * 40)

van_toc_roi_tu_do()