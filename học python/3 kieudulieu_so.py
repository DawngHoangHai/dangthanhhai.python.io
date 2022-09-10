from ast import main
import math
from platform import python_branch
from tkinter import N
from tkinter.ttk import Style
from unicodedata import decimal, name
# kiểu số nguyên int(intergers)
a,b,c = 10,20,3
# kiểu số thực float(số thập phân kiểu số thực là sấp sỉ 15 chữ số sau dấu chấm)
a = 7.123456789123456789
print(type(a))
print(a)

# cách dùng kiểu dữ liệu Decimal là : 

# lấy thư viện decimal ra và import vào : from decimal import
from decimal import*

# giới hạn sau chữ số thập phân của decimal : getcontext().prec = <số lượng sau dấu thập phân>
getcontext().prec = 3 

a = Decimal(a)
print(a/c)
print(type(a))

# kiểu phân số trong python 

# lấy thư viện fractions ra và import vào : from fractions import*
from fractions import*

phanso1 = Fraction(1,5)
phanso2= Fraction(6,3)
phansotong = phanso1 * phanso2

print(phansotong)
print(type(phansotong))

# kiểu số phức trong python : complex(<phần thực , phần ảo)

sophuc = complex(5,5)
print(sophuc)

# để lấy được phần thực của số phức -> .real , phần ảo là imag

print("phần thực = ",sophuc.real ,"\tphần ảo = ",sophuc.imag)

sp1 = complex(3,6)
sp2 = complex(2,4)
sum = sp1 - sp2
print(sum,type(sum))

""" Các toán tử tính toán trong python 
 - X + Y : cộng

 - X - Y : trừ

 - X * Y : nhân

 - X / Y : chia 
 - X // Y : chia lấy phần nguyên
 - X % Y : chia lấy phần dư

 - X ** Y : lũy thừa của 1 số (X ^ Y) 
 
 các phép toán gán và so sánh tương đương c++ 
 
 """

X, Y = 10 , 12
print("Tổng là : ",X+Y)
print("Hiệu là : ",X-Y)
print("Tích là : ",X*Y)
print("Thương là : ",(Decimal(X)/Y))
print("Thương Nguyên là : ",X//Y)
print("Thương Dư là : ",X%Y)
print("Lũy Thừa : ",X**Y)


    
""" sử dụng hàm math trong python 
{
     abs() : giá trị tuyệt đối
     complex(thực,ảo) :số phức
     divmod(X,Y) : (X//Y),(X%Y) lấ dư và nguyên 
     pow(x,y) : X^y
*    math.ceil () Làm tròn một số lên đến số nguyên gần nhất
*    math.fabs () Trả về giá trị tuyệt đối của một số
*    math.floor () Làm tròn một số xuống số nguyên gần nhất
*    math.gcd () Trả về ước số chung lớn nhất của hai số nguyên
*    math.pow () Trả về giá trị của x bằng lũy ​​thừa của y(mũ)
*    math.sqrt () Trả về căn bậc hai 
*    math.trunc () Trả về phần số nguyên 

} """
print("\t----------------------------------------------------------------------\n")
if __name__ =="__name__":
    main()