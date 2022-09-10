from ast import main
from email.policy import strict
from itertools import count
import math
from tkinter import CENTER


# CÁC PHƯƠNG THỨC CỦA KIỂU CHUỖI TRONG PYTHON 


# --> hàm capitalize() : trả về kí tự đầu tiên viết hoa còn lại trả về chữ thường
a = "đặng ThAnh HẢi"
print("Viết hoa chữ caí đầu Còn lại viết thường : %s"%(a.capitalize()))


# --> hàm upper() : viết hoa tất cả chữ cái
print(f"Viết hoa tất cả chữ caí : {a.upper()}")


# --> hàm upper() : viết thường tất cả chữ cái
print("Viết thường tất cả chữ cái : {0}".format(a.lower()))


# --> hàm swapcase() : đổi chữ hoa -> thường và ngược lại 
print("Viết đổi hoa thành thường thường thành hoa : {}".format(a.swapcase()))


# --> hàm centre(<chiều dài>,<kí tự>) :căn ra giữa chuỗi. Chiều dài: bằng chuỗi hoặc hơn, kí tự: để không thì là khoảng trắng   
# --> hàm ljust(<chiều dài>,<kí tự>) :căn ra trái chuỗi. Chiều dài: bằng chuỗi hoặc hơn, kí tự: để không thì là khoảng trắng   
# --> hàm rjust(<chiều dài>,<kí tự>) :căn ra phải chuỗi. Chiều dài: bằng chuỗi hoặc hơn, kí tự: để không thì là khoảng trắng   

""" hàm centre, ljust, rjust tương đương như căn lề phương thức format
- {<thuộc tính> : (c)<n} :căn lề trái

 - {<thuộc tính> : (c)>} :căn lề phải

 - {<thuộc tính> : (c)^n} :căn lề giữa
  """
b = "hải hải hải"
print("Hàm centre : {};{:^10} ;".format(b.center(10," "),b))
print("Hàm centre : {};;;".format(b.center(10,"-")))
print("Hàm left : {};;;".format(b.ljust(10,"-")))
print("Hàm right : {};;;".format(b.rjust(10,"-")))


# --> hàm replace : thay thế chuỗi replace(<chuỗi cần thay>,<chuỗi thay>,<số lần thay thế>)

c = b.replace(b,a)
c = b.replace("i",a,3)
# c = b.replace("i","iiiiiiiiiiiiiiiiiiiiii",1)
print(c)


# --> hàm strip() : cắt kí tự ở 2 đầu chuỗi đi, nếu khoog điền j thì là khoảng trắng
# strip(<kí tự cần xóa 2 đầu chuỗi>) : kí tự cần xóa 2 đầu chuỗi không ghi là khoẳng trắng

d = "     Đặng Thanh Hải"
print("Kí tự xóa khoảng trắng 2 đầu chuỗi : %s"%(d.strip()))
print("Kí tự xóa chữ i 2 đầu chuỗi : %s"%(d.strip("i")))
# ngoài ra còn có lstrip():cắt trái chuỗi và rstrip() : cắt phải chuỗi -> dùng tương tự strip()


# --> hàm partition(<kí tự cắt>) : cắt chuỗi ra 

print("cắt chuỗi theo chữ cái T:  {}".format(d.partition("T")))


# --> hàm count(<kí tự đếm>) : đếm kí tự trong chuỗi 

print("Có bao nhiêu kí tự 'n' trong chuỗi : {}".format(d.count("n")))
print("Có bao nhiêu kí tự 'n' trong chuỗi từ 0 -> 12 trong chuỗi : {}".format(d.count("n",0,12)))

# học thêm phương thức string 
# https://www.youtube.com/watch?v=u2Kd3weqPZE&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=11
if __name__ == "__name__":
    main()