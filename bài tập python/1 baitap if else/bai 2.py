
from ast import main

# BÀI TOÁN KIỂM TRA NĂM NHUẬN ?

nam = int(input("\t Nhập vào năm mà bạn muấn kiểm tra : "))

if((nam % 4 == 0) and (nam % 100 != 0) or (nam % 400 ==0)):
    print("\t---> Năm %d Là Năm nhuận !!!!"%(nam))
else:
    print("\t---> Năm %d Không Là Năm nhuận !!!!"%(nam))

if __name__ == "__name__":
    main()
