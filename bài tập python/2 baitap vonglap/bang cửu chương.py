from ast import main
from tkinter import W

# BÀI TẬP IN RA BẢNG CỬU CHƯƠNG 

n = int(input("\n\t - Nhập vào bảng cửu chương  : "))

while(n < 1 or n > 9):
    n = int(input("\n\t - Nhập lại bảng cửu chương  : "))

print("\t   BẢNG CỬU CHƯƠNG %d"%n)
for i in range(1,11):
    print("\t\t {0:^3} x {1:^3} = {2:^3}".format(n,i,n*i))

# TẤT CẢ BẢNG CỬU CHƯƠNG ?

print("\n\t-------------------------------------- IN RA TẤT CẢ BẢNG CỬU CHƯƠNG --------------------------------------",end='\n\n')
for i in range(1,11):
    for j in range(2,10):
        print("\t{0:^3} x {1:^3} = {2:^3}".format(j,i,i*j),end='')
    print("")

if __name__== "__name__":
    main()