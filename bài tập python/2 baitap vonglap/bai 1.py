from ast import main



n = int(input("\n\t - Nhập vào số nguyên dương n : "))
sum = 0
# TÌNH TỔNG TỪ 1 ĐẾN N ??

for i in range(1,n+1):
    sum += i
else: 
    print("\n\t ->>  Tổng Các Số Từ 1 đến %d là : %d "%(n,sum))

# TÌNH TÍCH TỪ 1 ĐẾN N ?? n!

sum = 1
for i in range(1,n+1):
    sum *= i
else: 
    print("\n\t ->>  Tích Các Số Từ 1 đến %d là : %d "%(n,sum))

if __name__=="__name__":
    main()