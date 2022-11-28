from ast import main
import mailbox
import math

a = int(input("Nhập vào cạnh bên 1 : "))
b = int(input("Nhập vào cạnh bên 2 : "))
c = int(input("Nhập vào cạnh  đáy  : "))

# TÍNH CHU VI DIỆN TÍCH 

if (a >= b + c or b >= a + c or c >= a + b):
    print("--> Ba Cạnh {0:^5},{1:^5},{2:^5} không phải cạnh của tam giác".format(a,b,c))
else:
    print("--> Tính Chu Vi Và Diện tích của Tam Giác : {0:^5},{1:^5},{2:^5}".format(a,b,c))
    chuVi = a + b + c; 
    print("--> Chu Vi Của tam giác có cạnh %d, %d, %d là : %d cm"%(a,b,c,chuVi)) 
    p = chuVi / 2 ;
    dienTich = math.sqrt(p * (p - a) * (p - b) * (p -c)) 
    print("--> Diện Tích Của tam giác có cạnh %d, %d, %d là : %d cm"%(a,b,c,dienTich))

# KIỂM TRA TAM GIÁC LÀ 

if (a >= b + c or b >= a + c or c >= a + b):
    print("--> Ba Cạnh {0:^5},{1:^5},{2:^5} không phải cạnh của tam giác".format(a,b,c))
else:
    if(a==b and b == c):
        print("--> Ba Cạnh %d , %d , %d Tạo Thành Tam Giác Đều !!!"%(a,b,c))
    elif (a == c or b == c or a == c):
        if((a * a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == b * b + a * a)):
            print("--> Ba Cạnh %d , %d , %d Tạo Thành Tam Giác Vuông Cân !!!"%(a,b,c))
        else:
            print("--> Ba Cạnh %d , %d , %d Tạo Thành Tam Giác Cân  !!!"%(a,b,c))
    elif ((a * a == b * b + c * c )or (b * b == a * a + c * c) or (c * c == b * b + a * a)):
        print("--> Ba Cạnh %d , %d , %d Tạo Thành Tam Giác Vuông  !!!"%(a,b,c))
    else:
        print("--> Ba Cạnh %d , %d , %d Tạo Thành Tam Thường  !!!"%(a,b,c))

if __name__=="__name__":
    main()