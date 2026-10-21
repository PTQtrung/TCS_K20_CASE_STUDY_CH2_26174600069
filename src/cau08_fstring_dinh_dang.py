ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Đã sửa từ input() str sang float
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")  # Đã sửa lỗi thiếu dấu ngoặc đóng ) ở cuối hàng

# Ghi chú lỗi phát hiện 
# Lỗi 1: TypeError do cong_suat_w nhận giá trị chuỗi từ input() đem nhân với số. Khắc phục: ép kiểu sang float.
# Lỗi 2: SyntaxError / NameError do thiếu dấu đóng ngoặc tròn `)` ở cuối đoạn, ta thêm ngoặc tròn ở cuối
