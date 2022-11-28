from ast import main
from re import ASCII
from xmlrpc.client import boolean

# kiểu dữ liệu boolean trả về 2 giá trị true or false

a = True
print(type(a))

# tương tự như bool c++
# lấy ra bảng  mã ASCII thì dùng ord print(ord('h')) truyền vào 1 kí tự 

a = 'AAA'
b ='Abb'
c = a < b
print("Toán tử so sánh bool {}".format(c))

# toán tử ==  : là so sánh giá trị 
# còn is : là so sánh id của nó 

# các số từ (-5 đến 256 ) hoặc (1 chuỗi có kí tự <=20) thì các biến cùng giá trị hàm id 

# TOÁN TỬ XÁC THỰC
a_ = -10
b_ = -10

print(id(a_))
print(id(b_))
print('nếu id của a = b thì : %s'%(a_ is b_))
print('nếu id của a != b thì : {}'.format(a_ is not b_))


# TOÁN TỬ KHAI THÁC 
a= 'h'
b = 'đặng thanh hải'
print("chữ h có nằm trong chuỗi trên không ",a in b)
print("chữ h không nằm trong chuỗi trên không ",a not in b)


if __name__ == "__name__":
    main()