print("-- Kết Quả Chuẩn Hóa Dữ Liệu--")
code_bn = input(" Mã bệnh nhân:")
temperature = float(input("Nhiệt độ cơ thể:"))
heart_rate = int(input("Nhịp tim:"))

print('kẾT QUẢ')
print(f"Mã Bệnh Nhân:{code_bn}")
print(f"Nhiệt Độ Cơ Thể: {temperature}")
print(f"Nhip Tim:{heart_rate}")


# Input:
# - Mã bệnh nhân      -> kiểu chuỗi (str)
# - Nhiệt độ cơ thể   -> cần lưu kiểu số thực (float)
# - Nhịp tim          -> cần lưu kiểu số nguyên (int)

# Vì dữ liệu nhập từ input() luôn là string
# nên cần ép kiểu dữ liệu bằng:
# - float() cho nhiệt độ
# - int() cho nhịp tim
# Sử dụng Type Casting:
# float()  -> chuyển chuỗi sang số thực
# int()    -> chuyển chuỗi sang số nguyên
