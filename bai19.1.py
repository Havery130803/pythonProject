# Minh họa trò chơi "Điểm thưởng" - Hãy chọn giá đúng

from random import randrange
import time

print("TRÒ CHƠI ĐIỂM THƯỞNG ")
print("Nhập 1 nếu đoán đúng, nhập 2 nếu đoán sai: ")
a = int(input("Kết quả đoán giá sản phẩm thứ 1: "))
b = int(input("Kết quả đoán giá sản phẩm thứ 2: "))
c = int(input("Kết quả đoán giá sản phẩm thứ 3: "))
d = int(input("Kết quả đoán giá sản phẩm thứ 4: "))
if a == 1 and b == 1 and c == 1 and d == 1:
    print("Bạn đã chiến thắng !")
elif a == 2 and b == 2 and c == 2 and d == 2:
    print("Bạn chưa chiến thắng !")
else:
    start = input("Nhấn phím s để bắt đầu trò chơi: ")
    time.sleep(5)
    ran = randrange(1, 5)
    print("Sản phẩm may mắn là sản phẩm số: ", ran)
    if ran == 1:
        if a == 1:
            print("Bạn đã chiến thắng !")
        else:
            print("Bạn chưa chiến thắng !")
    elif ran == 2:
        if b == 1:
            print("Bạn đã chiến thắng !")
        else:
            print("Bạn chưa chiến thắng !")
    if ran == 3:
        if c == 1:
            print("Bạn đã chiến thắng !")
        else:
            print("Bạn chưa chiến thắng !")
    if ran == 4:
        if d == 1:
            print("Bạn đã chiến thắng !")
        else:
            print("Bạn chưa chiến thắng !")
