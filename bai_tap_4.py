def kiem_tra_chuoi(text):
    tu_1 = "Python"
    tu_2 = "Programming"
    
    text_lower = text.lower()
    
    dieu_kien_1 = tu_1.lower() in text_lower 
    dieu_kien_2 = tu_2.lower() in text_lower 
    
    if dieu_kien_1 and dieu_kien_2:
        print(f" Chuỗi thỏa mãn: Chứa cả '{tu_1}' và '{tu_2}'.")
        return True
    else:
        print(f" Chuỗi KHÔNG thỏa mãn: Thiếu một trong hai từ '{tu_1}' hoặc '{tu_2}'.")
        return False

chuoi_tot = "Tôi rất thích lập trình Python Programming."
chuoi_thieu = "Python là một ngôn ngữ tuyệt vời."
chuoi_co_hoa = "Để thành thạo PYTHOn PrOGraMming cần có thời gian."

print("--- Kết quả kiểm tra ---")
kiem_tra_chuoi(chuoi_tot)
kiem_tra_chuoi(chuoi_thieu)
kiem_tra_chuoi(chuoi_co_hoa)