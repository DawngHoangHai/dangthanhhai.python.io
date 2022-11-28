from ast import main

print("\n===============================================================================\n")
n = int(input('\n\t - Nhập vào chiều dài : '))
m = int(input('\n\t - Nhập vào chiều rộng : '))
print("\t In ra Hình chữ nhật đặc\n")
for i in range(1,m + 1):
    for j in range(1,n + 1):
        print(" * ",end='')
    print()

print("\n===============================================================================\n")

n = int(input('\n\t - Nhập vào chiều dài : '))
m = int(input('\n\t - Nhập vào chiều rộng : '))
for i in range(1,m + 1):
    for j in range(1,n + 1):
        if (i == 1 or i == n or j == 1 or j == m):
            print(" * ",end='')
        else:
            print("   ",end='')   
    print()        
if __name__ == "__name__":
    main()