from ast import main
diemKt = float(input("Nhập vào điểm kiểm tra : "))
diemGk = float(input("Nhập vào điểm giữa kì : "))
diemCk = float(input("Nhập vào điểm cuối kì : "))

diemTb = (diemKt + diemGk + diemCk)/3;

if(diemTb >= 9):
    print("\t--> Học sinh này đạt học sinh giỏi với %.2f điểm "%(diemTb))
elif(diemTb < 9 and diemTb >= 7):
    print("\t--> Học sinh này đạt học sinh khá với %.2f điểm "%(diemTb))
elif(diemTb < 7 and diemTb >= 5):
    print("\t--> Học sinh này đạt học sinh trung bình với %.2f điểm "%(diemTb))
else:
    print("\t--> Học sinh này bị ở lại lớp với %.2f điểm "%(diemTb))
if __name__ == "__name__":
    main()