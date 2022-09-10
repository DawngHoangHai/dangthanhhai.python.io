from ast import main
from gettext import ngettext
import string
#  kiểu dữ liệu chuỗi trong  python 
#  - cách phần tử mà nằm trong dấu 'chuỗi bên trong', "chuỗi bên trong", '''chuỗi bên trong''', """chuỗi bên trong"""  điều là kiểu chuỗi

a = """Đặng Thanh Hải"""
b = 'Đặng Hải Thanh'
c = '''Hải Đặng Thanh '''
d = "Thanh Đặng Hải"
print(a,b,c,d)
print(type(a),type(b),type(c),type(d))

# sự khác nhau đối với các dấu nháy là :
# ->> khi chuỗi bên trong có chứa dấu nháy thì dùng dấu lớn hơn bao lấy nó

string1 = "I'am Hải"
string2 = ''' anh ấy tên là " Hải " '''

print(string1,string2)

# ->> chuỗi nhiều dòng thì sử dụng """ chuỗi bên trong  """ , '''chuỗi bên trong. '''
chuoinhieudong = """Đặng Thanh Hải
DHTI14A1ND 
Thái Bình 
Nam"""

# viết chuỗi nhiều dòng theo kiểu khác (trong chuỗi nhiều dòng phím enter = \n khi viết hàng ngang)
# chuoinhieudong = """Đặng Thanh Hải\nDHTI14A1ND\nThái Bình\nNam"""

print(chuoinhieudong)

""" các kí tự \gì đấy  trong pythpn
\a : tạo ra tiếng bíp
\b :đưa con trỏ về 1 khoảng trắng(cắt đi 1 kí tụ trước nó)
\n : xuống dòng
\t : tab ra 1 khoảng
\' : tạo ra kí tự '
\" : tạo ra kí tự "
\\ : tạo ra kí tự \ """

print('hải\bhải')
print('hải\ahải')
print('hải\nhải')
print('hải\thải')
print('hải\\hải')
print('hải\'hải')
print('hải\"hải')



if __name__ =="__name__":
    main()