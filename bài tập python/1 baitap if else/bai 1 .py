#  VIẾT CHƯƠNG TRÌNH NHẬP VÀO 2 SỐ NGUYÊN VÀ TÍNH + - * 

a = int(input('Nhập vào số nguyên a : '))
b = int(input('Nhập vào số nguyên b : '))
phepTinh = a + b ;
print('--> Tổng 2 số %d + %d = %d'%(a,b,phepTinh))
phepTinh = a - b ;
print('--> Hiệu 2 số %d - %d = %d'%(a,b,phepTinh))
phepTinh = a * b ;
print('--> Tích 2 số %d x %d = %d'%(a,b,phepTinh))
phepTinh = a / b ;
print('--> Thương 2 số %d / %d = %.2f'%(a,b,phepTinh))
phepTinh = a // b ;
print('--> Thương Nguyên 2 số %d // %d = %.2f'%(a,b,phepTinh))
phepTinh = a % b ;
print('--> Thương Dư 2 số %d dư %d = %.2f'%(a,b,phepTinh))
