cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phí:", chi_phi, type(chi_phi))

# Thay so_phut bằng 60 rồi chạy lại:
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Sau khi đổi số phút thành 60:")
print("Điện năng:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phí:", chi_phi, type(chi_phi))

#tính điện năng
#dien_nang_kwh = 250*90/60/1000 = 0.375 Kwh
#tính chi phí
#chi_phi = 0.375*3000 = 1125 VND
