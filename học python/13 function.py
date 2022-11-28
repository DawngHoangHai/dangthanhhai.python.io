# KIỂU DỮ LIỆU TRONG PYTHON 

from ast import Return, keyword, main
""" CẤU TRÚC KHAI BÁO HÀM :
    def <tên hàm>(giá trị truyền vào , giá trị n truyền vào ):
        khối thực thi câu lệch
 """

# HÀM KHÔNG CÓ DỮ LIỆU TRUYỀN VÀO ?

def outPut():
    print("\nĐặng Thanh Hải\n"*5)

outPut()


# HÀM CÓ DỮ LIỆU ĐẦU VÀO ?

# khai báo bao nhiêu tham số truyền vào bằng đấy tham số 
def outPut2(a,b):
    print("\nTổng 2 giá trị là : ",a+b)
outPut2(5,5)

# hàm có thể truyền vào giá trị mà mk gán trước nhưng phải để cuối tham số

# def outPut2(b="hải hi hi",a): như này sẽ nỗi
# CÁCH 1 :
def outPut2(a,b="hải hi hi"):
    print("\nGiá trị của a = ",a)
    print("\nGiá trị của b = ",b)

# chỉ cần truyền tham số với giá trị chưa gán 
outPut2(6)
outPut2(6,"hải thay thế") # vẫn truyền tham số vào đk 


# CÁCH 2:
a = "hải hải hải";
def outPut2(b,a = a):
    print("\nGiá trị của a = ",a)
    print("\nGiá trị của b = ",b)
outPut2(6)

# HÀM TRUYỀN VÀO THAM SỐ MÀ CÓ KEYWORD ?

def TinhToan(a,b,c,d):
    print("\nTổng = %d + %d + %d + %d  = %d"%(a,b,c,d,a+b+c+d))

TinhToan(5,6,7,8) # truyền the tuần tự
TinhToan(b=5,c=3,d=2,a=10)# truyền theo keyword

""" khi gọi hàm mà muấn có cả tham số và tham số keyword 
        + thì tham số luôn đi trước và theo trình tự
        + còn tham số keyword theo sau """

TinhToan(10,5,d= 4,c=5)#truyền vào có tham số và tham số keywold

# Return TRONG PYTHON (CHỈ DÙNG TRONG HÀM - > return là hàm kết thức)

def tinhToan(dai,rong):
    chuVi = (dai +rong) *2;
    return chuVi;
    print("câu lệnh này sẽ không được in ra !!!! vì sau return ")
ketQua = tinhToan(5,4);
print("\nChu vi Hinh chữ nhật là : ",ketQua)
print("\nChu vi Hinh chữ nhật là : ",tinhToan(5,4))

    
if __name__ == "__name__":
    main()