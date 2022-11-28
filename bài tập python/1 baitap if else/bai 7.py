from ast import main
import math
print("\n\t GIẢI PHƯƠNG TRÌNH BẬC 2 !!")
a = int(input("\n\t - Nhập vào a = "))
b = int(input("\n\t - Nhập vào b = "))
c = int(input("\n\t - Nhập vào c = "))
if(a==0):
    print("\n\t PHƯƠNG TRÌNH TRỞ THÀNH PHƯƠNG TRÌNH BẬC NHẤT !! ")
    if(b==0):
        if(c==0):
            print("\n\t--> Phương trình vô số nghiệm !! ")
        else:
            print("\n\t--> Phương trình vô  nghiệm !! ")
    else:
        X = -b/c;
        print("\n\t--> Phương trình có nghiệm là %.2f "%(X))
else:
    delta = math.pow(b,2) - 4 *a*c;
    if delta >0:
        x1 = (-b + math.sqrt(delta)) / (2 * a);
        x2 = (-b - math.sqrt(delta)) / (2 * a);
        print("\n\t--> Phương trình có 2 nghiệm x1 = %.3f và x2 = %.3f !!! "%(x1,x2))
    elif(delta == 0):
        print("\n\t--> Phương trình có nghiệm kép x1 = x2 = %.3f !!"%(-b/2*a))
    else:
        print("\n\t--> Phương trình vô nghiệm !!! ")
print("\n")
if __name__ == "__name__":
    main()