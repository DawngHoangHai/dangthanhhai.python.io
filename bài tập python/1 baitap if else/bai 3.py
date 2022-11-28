from ast import main

# VIẾT CHƯƠNG TRÌNH KIỂM TRA TUỔI 

tuoi = int(input("Nhập vào tuổi để kiểm tra xem : "))
if(tuoi == 16 ):
    print(" --->Học Sinh Này đủ tuổi vào lớp 10 với : %d tuổi"%(tuoi))
elif(tuoi >= 16):
    print(" --->Học Sinh Này thừa tuổi vào lớp 10 với : %d tuổi"%(tuoi))
else:
    print(" ---> Học Sinh Này chưa đủ tuổi vào lớp 10 với : %d tuổi"%(tuoi))
if __name__ == "__name__":
    main()
