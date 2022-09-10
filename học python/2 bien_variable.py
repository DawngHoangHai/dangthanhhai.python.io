from ast import main
# biến trong lập trình python
#  - Biến không bắt đầu bằng số
#  - Không được chùng với từ khóa của pt
#  - biến sẽ có chữ cái, số và _
#  - có phân biệt chữ hoa và chữ thường
# khởi tạo biến :tên biến = <giá trị của biến>
a4_ = 100
b = 300
c = a4_+b
print(a4_)
print('Tổng bằng = ',c)

# ta có thể khai báo nhiều biến cùng lúc tên biến tương đương với vị trí giá trinh của biến 
hoten,tuoi,quequan = "Đặng Hải",20,"Thái Bình"
# cách kiểm tra kiểu dữ liệu trong python
type(tuoi),type(hoten),type(quequan)

print(type(tuoi),type(hoten),type(quequan))
print(hoten,tuoi,quequan)

if __name__ =="__name__":
    main()