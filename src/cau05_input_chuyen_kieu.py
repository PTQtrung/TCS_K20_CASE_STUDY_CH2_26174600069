ma_may = input("Nhập mã máy: ")
print(type(ma_may))

cong_suat_w = input("Nhập công suất W: ")
print(type(cong_suat_w))

so_phut = input("Nhập số phút sử dụng: ")
print(type(so_phut))

don_gia_kwh = input("Nhập đơn giá điện/kWh: ")
print(type(don_gia_kwh))

# Chuyển đổi kiểu dữ liệu
cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

# Tính lại điện năng và chi phí
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} VND")
