from ast import main
from ctypes.wintypes import HDC


# CẤU TRÚC IF ELSE 
""" 1 số điều kiện khi định dạng code trong python 
    + dùng song câu lệnh if phải có dấu (:)
    + bên trong khối thực thi bắt buộc phải có nội dung không sẽ báo nỗi
    + những dòng code cùng nề đầu dòng là cùng 1 block 
    + không sử dụng tab và space để căn lề block 
    + sử dụng 4 space để căn lề block 
    + nội dung trong khối thực thi phải đều đầu dòng """
a = int(input("Nhập vào số nguyên a : "))   
b = int(input("Nhập vào số nguyên b : ")) 
if (a+b)>10: 
    print("{0} + {1} = {2}".format(a,b,a+b)) 
    print("lơn hơn 10.")
elif (a+b<10):
    print("{0} + {1} = {2}".format(a,b,a+b)) 
    print("nhỏ hơn 10")
else:
    print("{0} + {1} = {2}".format(a,b,a+b))
    print("bằng 10") 
print('END...........')
if __name__ == "__name__":
    main()