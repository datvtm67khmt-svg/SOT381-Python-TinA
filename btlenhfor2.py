diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for diem in  diem_so:
    if diem >=8:
      xeploai= "Giỏi"
    elif diem >=6.5:
     xeploai= "Khá"
    else:
      xeploai= "Trung bình"
    print(f"Điểm {diem}: Xếp loại {xeploai}")