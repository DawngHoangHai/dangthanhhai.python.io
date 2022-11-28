from ast import main
from os import sep

# BÀI TOÁN TÌM ƯỚC CHUNG CỦA SỐ N ?
n = int(input("\n\t - Nhập vào số nguyên dương n : "))

print("\n\t - >Ước Của Số NGuyên %d Là : "%(n),end='\t')

for i in range(1,n):
    if(n%i == 0):
        print("%d"%(i),sep="-",end='\t')


if __name__== "__name__":
    main()