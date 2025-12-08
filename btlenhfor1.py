so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
nguon_chi_muc = [0, 1, 2, 3, 4, 5] 
for n in nguon_chi_muc:
    so_luong_ton = so_luong[n]
    if so_luong_ton < 10:
        ten = ten_san_pham[n]
        print(f"- {ten}: Tồn kho hiện tại là {so_luong_ton} ")