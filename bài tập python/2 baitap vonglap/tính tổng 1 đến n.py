from ast import main
import math


print("\n===============================================================================\n")
print("\t TÍNH TỔNG 1 + 3 + 5 +...+(2*n - 1)\n")
n = int(input("\t - Nhập vào số nguyên n : "))
sum = 0;
for i in range(1,n+1):
    sum += ((2*i) - 1)
else:
    x = (n)
    print("\n\t - >> Tổng của 1 + 3 + 5 +...+ %d là : %d "%(x,sum))


print("\n===============================================================================\n")
print("\tViết chương trình tính tổng S = 1 + 1/2 + 1/3 + 1/4 + … + 1/n \n")
n = int(input("\t - Nhập vào số nguyên n : "))
sum = 0;
for i in range(1,n+1):
    sum += 1/i;
else:
    x = 1/n;
    print("\n\t - >> Tổng S = 1 + 1/2 + 1/3 + 1/4 + … + 1/%d là : %.3f "%(x,sum))


print("\n===============================================================================\n")
print("\tViết chương trình tính tính tích P = 2*4*6* …*2n \n")
n = int(input("\t - Nhập vào số nguyên n : "))
sun = 1;
for i in range(2,n+1):
    sum *= (2*i);
else:
    x = 2*n;
    print("\n\t - >> Tổng S = P = 2 * 4 * 6 * … * %d là : %.3f "%(x,sum))

print("\n===============================================================================\n")
print("\tViết chương trình tính tổng S = 1 + 4 + 9 + … + n2 \n")
n = int(input("\t - Nhập vào số nguyên n : "))
sum = 0;
for i in range(1,n+1):
    sum += math.pow(i,2)
else:
    x = math.pow(n,2)
    print("\n\t - >> Tổng S = 1 + 4 + 9 + … + %d là : %.3f "%(x,sum))
if __name__=="__name__":
    main()