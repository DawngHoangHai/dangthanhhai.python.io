from ast import main
from itertools import count
import math
n = float(input('\n\t - Nhập vào số nguyên bất kì : '))
sum = 0;counts = 0
for i in range(2,float(n/2)):
    if(n % i == 0):
        counts += 1
else:
    if(counts == 0):
        print("\n\t---> %d Là Số Nguyên Tố !!! "%(n))
    else:
        print("\n\t---> %d Không Là Số Nguyên Tố !!! "%(n))
if __name__ == "__name__":
    main()