def quan_ly_diem():
    print("=== CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM HỌC SINH ===")
    
    ho_ten = input("Nhập tên học sinh: ")
    
    try:
        toan = float(input("Nhập điểm Toán (0-10): "))
        ly = float(input("Nhập điểm Lý (0-10): "))
        hoa = float(input("Nhập điểm Hóa (0-10): "))
    except ValueError:
        print("Lỗi: Điểm phải là một số hợp lệ.")
        return

    diem_trung_binh = (toan + ly + hoa) / 3

    if diem_trung_binh >= 8:
        xep_loai = "Giỏi"
    elif diem_trung_binh >= 6.5:
        xep_loai = "Khá"
    elif diem_trung_binh >= 5:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"

    print("\n" + "="*50)
    print("✨ PHIẾU KẾT QUẢ HỌC TẬP ✨")
    print("="*50)
    print(f"Họ và tên: {ho_ten:<40}")
    print("-" * 50)
    print(f"Điểm Toán: {toan:>20.1f}")
    print(f"Điểm Lý: {ly:>22.1f}")
    print(f"Điểm Hóa: {hoa:>22.1f}")
    print("-" * 50)
    print(f"ĐIỂM TRUNG BÌNH: {diem_trung_binh:>14.2f}") 
    print(f"XẾP LOẠI: {xep_loai:>22}")
    print("="*50)  
quan_ly_diem()