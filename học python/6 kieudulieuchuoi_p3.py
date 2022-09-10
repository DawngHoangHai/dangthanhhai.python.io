from ast import main

"""  định dạng với toán tử %
    - %s : giá trị của phương thức str
    - %d : giá trị của phương thức int
    - %f : giá trị của phương thức float
    - %r : giá trị của phương thức rept
 """

a = "đặng thanh hải %s"%("dhti14a1nd")# thay thế cái %s = %(bên trong đây)

b="%s và %s" #có thể viết như này
print(a)
print(b%(4,6)) #có thể viết như này

print("Đặng Thanh %s tuổi\nLớp %s"%(21,"DHTI14A1ND"))

print("số đầu tiên = %f ,số thứ 2 = %d"%(6.6,7.7))

#->> đối với %f muấn lấy số sau số thập phân -->> %.sốlượng+f
print("số 2 sô thập phân : %.2f"%(6.66))

#->> muấn làm tròn lên hay xuống thì %.f
print("sô thập phân làm tròn lên : %.f làm tròn xuống : %.f" %(7.7,7.4))

#cho bao nhiêu %s thì bên kia có bằng đấy %(...,...,...) (cách nhau dấu ,)

# chuỗi f tương tự như chuỗi $ trong C#

hoten = 'ĐẶNG THANH HẢI'
diachi = 'Thái Bình'
phone = 1434433430
diem = 8.8

# chuỗi f tương tự như chuỗi $ trong C#
print(f"Ho Tên : {'hải'}\t\tĐịa Chỉ : {diachi}\tPhone : {phone}\tĐiểm : {diem}")

# ta có thể viết như này (tham số truyền vào thừa cũng được)
print("Họ Tên : {0}\t\tĐịa Chỉ : {1}\tPhone : {2}\tĐiểm : {3}".format("hải hải",diachi,phone,diem))

# có thể để như này sẽ sắp xếp theo thứ tự thuộc tính trái sang phải
print("Họ Tên : {}\t\tĐịa Chỉ : {}\tPhone : {}\tĐiểm : {}".format("hải hải",diachi,phone,diem))


""" căn lề của phương thức format

 - {<thuộc tính> : (c)<n} :căn lề trái

 - {<thuộc tính> : (c)>} :căn lề phải

 - {<thuộc tính> : (c)^n} :căn lề giữa

 ---> c : là kí tự chèn vào khoảng trắng(để trống là khoảng trắng)
        n : là số kí tự dùng để căn lề
==>> Cách này nên ưu tiên vì độ đẹp cao
         """

print("\t+------------------------------------------------------------------------------------------------------------------------------+")        
print("\t| Họ Tên : {0:^25}| Địa Chỉ : {1:^25}| Phone : {2:-<20}| Điểm : {3:*>10}điểm |"
.format(hoten,diachi,phone,diem))
print("\t+------------------------------------------------------------------------------------------------------------------------------+")

if __name__ == "__name__":
    main()