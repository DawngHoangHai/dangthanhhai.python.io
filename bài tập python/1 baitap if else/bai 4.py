from ast import main

# VIẾT PHƯƠNG TRÌNH KIỂM TRA SỐ ĐO LỚN 100 HAY KHÔNG 

n = int(input("Nhập Vào số Nguyên Để kiểm tra : "))
if(n > 100):
    print("--> Số %d là số lớn hơn 100 !!! "%(n))
elif(n == 100):
    print("--> Số %d == 100 !!! "%(n))
else:
    print("--> Số %d là số bé hơn 100 !!! "%(n))
if __name__ =="__name__":
    main()