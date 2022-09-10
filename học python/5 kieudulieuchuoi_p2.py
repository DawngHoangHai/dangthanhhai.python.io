from ast import main
from platform import python_branch

# kiểu dữ liệu chuỗi trần : khi ta dùng kí tự \ mà nó liên quan đến đường dẫn hay file thì ta dùng chuỗi trần
# ta thêm r vào trước chuỗi sẽ thành chuỗi trần (không tính \+kí tự)

print(r"Đặng Thanh Hải \t Hải")
stra = r"hải\nhải"
print(stra)

# nối chuỗi với nhau dùng + 

strb = "dhti14a1nd"
sum = stra +"\t"+ strb
print(sum)
print("Đặng" + "\t" + "Thanh" + "\t" + "Hải")

# nhân chuỗi lên dùng dấu *

sum = stra*5
print(sum)
print("Đặng Thanh Hải\n"*5)

# toán tử in (kiểm tra trong 1 chuỗi có nằm trong chuỗi khác hay không)
# ->> chuỗi này sẽ trả về là true hoặc false

kiemTra = "Hải" in "Đặng Thanh Hải"
print('Kết quả là : ',kiemTra)

# cách lấy ra phần tử trong một chuỗi 
# ->> ta dùng cách :  chuỗi[số int] : int là vị trí muấn lấy ra 
stra = "ĐặngThanhHải.com.vn"
kt = stra[3]

print(stra[0],kt)
print(len(stra),"kí tự")#len(chuỗi) => lấy ra độ dài của chuỗi

# cắt chuỗi trong python từ trái qua phải 
# --->> chuoi[<điểm start>:<điểm end>]
chuoicat = stra[4:10] # cắt vị trí thứ 4 đến 10 (- 1 kí tự)
chuoicat = stra[None:10]# cắt vị trí thứ 0 đến 10 (- 1 kí tự)
chuoicat = stra[10:None]# cắt vị trí thứ 10 đến hết (có thể dùng len(stra) thay None)

print(chuoicat)

# cắt chuỗi trong python từ phải qua trái
# --->> chuoi[<điểm start>:<điểm end>:<bước nhảy>]
# stra = "ĐặngThanhHải.com.vn"

chuoicat2 = stra[None:None:-1]# cắt ngược lại chuỗi theo bước nhảy là -1 
chuoicat2 = stra[None:None:2]# cắt chuỗi theo bước nhảy
print(chuoicat2)


if __name__ =="__name__":
    main()