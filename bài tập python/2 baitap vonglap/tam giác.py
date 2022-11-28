from ast import main
n = 10;
print("\tIN TAM GIÁC VUÔNG TRÁI DƯỚI\n")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" *",end='')
    print()

print("\n================================================================================\n")

print("\tIN TAM GIÁC VUÔNG TRÁI TRÊN\n")
for i in range(n,0,-1):
    for j in range(1,i+1,1):
           print(" *",end='')
    print() 

print("\n================================================================================\n")
print("\t IN RA TAM GIÁC VUÔNG PHẢI DƯỚI\n")
for i in range(0,n+1):
    for j in range(0,n+1):
        if(j <= n - i):
            print("  ",end='')
        else:
            print(" *",end='')
    print()

print("\n================================================================================\n")
print("\t IN RA TAM GIÁC VUÔNG PHẢI TRÊN\n")
for i in range(n,0,-1):
    for j in range(0,n+1,1):
        if(j <= n - i):
            print("  ",end='')
        else:
            print(" *",end='')
    print()
if __name__ == "__name__":
    main()