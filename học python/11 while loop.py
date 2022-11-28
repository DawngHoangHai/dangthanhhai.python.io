from ast import Break, main
from http.client import CONTINUE
from time import sleep
from turtle import goto

# VÒNG LẶP WHILE LOOP
a = int(input(" - Nhập vào số nguyên dương : "))
i=0
while(i<=a):
    print("{0:^10}".format(i),end='')
    i+=1
else:
    print("cái này sẽ được hiện khi xong vòng while ")

# print()
# b="đăng hải"
# i=0
# lenght = len(b)
# while(i<lenght):
#     print("{0:^3}".format(b[i]),end='')
#     i+=1

""" TA CÓ THỂ SỬ DỤNG WHILE else

        +else sẽ hiển thị khi vòng while được chạy xong 
        +else sẽ không hiển thị nếu trong vòng while có break 

             """

# SỬ DỤNG BREAK VÀ CONTINUE
c = 10
i=0
# Break
while(i<c):
    print("{0:^3}".format(i),end='')
    if(i==6):
        break #dừng chương trình
    i+=1
else:
    print("Cái này sẽ không được hiện  vì có break")


# CONTINUE   
# while(i<c):
#     i+=1
#     print("{0:^3}".format(i),end='')
#     continue
#     print("hai hải hải")


# pass : đánh dấu trong vòng lặp khi chưa có câu lệnh j (để đánh dấu vong lặp sẽ không nỗi)

if __name__ == "__name__":
    main()