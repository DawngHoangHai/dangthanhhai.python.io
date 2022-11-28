from ast import main
import math

print("\n\tTAM GIÁC VUÔNG CÂN ĐẶC \n")
n = 10;
for i in range(1,n+1,1):
    for j in range(1,2*n,1):
        if(abs(n-j)<i):
            print(" * ",end='')
        else:
            print("   ",end='')
    print()

print("\n================================================================================\n")
print("\n\t TAM GIÁC VUÔNG CÂN RỖNG")
for i in range(1,n+1,1):
    for j in range(1,2*n,1):
        if(abs(n-j) == i - 1 or i == n):
             print(" * ",end='')
        else:
            print("   ",end='')
    print()
if __name__ =="__name__":
    main();