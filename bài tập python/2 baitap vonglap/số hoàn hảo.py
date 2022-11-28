from ast import main

n = int(input('\n\t - Nhập vào số nguyên bất kì : '))
sum = 0;
for i in range(1,n):
    if(n % i == 0):
        sum += i;

if(sum == n):
    print("\n\t---> %d Là Số Hoàn Hảo !!! "%(n))
else:
    print("\n\t---> %d Không Là Số Hoàn Hảo !!! "%(n))

if __name__ == "__name__":
    main()