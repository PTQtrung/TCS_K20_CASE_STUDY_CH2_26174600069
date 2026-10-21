from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# 24. Dự đoán phép trừ: Trả về khoảng thời gian (timedelta) là 1 giờ 50 phút.
# 25. Giải thích:
# - datetime: Đối tượng biểu diễn mốc thời gian cụ thể (gồm năm, tháng, ngày, giờ, phút, giây).
# - str: Kiểu chuỗi ký tự dùng để hiển thị định dạng văn bản trực quan.
# - timedelta: Đối tượng biểu diễn khoảng thời gian chênh lệch giữa hai mốc datetime.
