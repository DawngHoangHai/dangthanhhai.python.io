from ast import main
from stat import SF_APPEND
# Bài toán: Hãy viết chương trình giải phương
# trình bậc nhất 1 ẩn: ax + b = 0

# Lập trình:
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
# hoten = input("Nhập Họ Tên Cua Bạn : ")
# print("Họ Tên Bạn Là : ",hoten)
if a == 0:
  if b == 0:
    print("Vô số nghiệm")
  else:
    print("Vô nghiệm")
else:
  print("Phương trình có nghiệm x =", -b / a)
if __name__ =="__name__":
    main()