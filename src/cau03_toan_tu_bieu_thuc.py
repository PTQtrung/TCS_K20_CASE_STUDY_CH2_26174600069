tong_phut = 135
cong_suat_w = 250

# 9. Tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"Số giờ: {so_gio}, Số phút còn lại: {so_phut_du}")

# 10. su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("su_dung_lau:", su_dung_lau)

# 11. du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("du_lieu_hop_le:", du_lieu_hop_le)

# 12. Dự đoán rồi kiểm chứng hai biểu thức: 100 + 20 * 3 và (100 + 20) * 3
# Dự đoán: 100 + 20 * 3 = 160 (nhân chia trước); (100 + 20) * 3 = 360 (ưu tiên ngoặc)
print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)
