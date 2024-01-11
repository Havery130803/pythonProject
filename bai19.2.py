# Trò chơi "Đồng hồ may mắn" - Hãy chọn giá đúng 2009

from random import randrange
import time

print("TRÒ CHƠI ĐỒNG HỒ MAY MẮN")
# Bạn có 60s để đoán giá cho 2 sản phẩm, thời gian đoán liên tiếp nhau. Hệ thống sẽ cho bạn biết giá đúng cao hơn
# gía gốc. Nếu đúng, hệ thống sẽ thông báo đoán đúng. Nếu còn thời gian, hãy chuyển sang đoán sản phẩm thứ 2
# Nếu đoán đúng cả 2 sản phẩm, bạn sẽ có 10 triệu đồng, mỗi sản phẩm đoán đúng bạn có 5tr đồng
tienthuong = 0
a = randrange(2000, 2201) * 1000
b = randrange(2000, 2201) * 1000
ch = int(input("Bạn sẽ đoán sản phẩm nào trước, 1 hay 2: "))
print("Cả 2 sản phẩm sẽ có giá trong khoảng từ 2.000.000 đến 2.200.000 !")
print("Khi nhập giá không cần nhập dấu chấm !")
if ch == 1:
    start = input("Bạn có 30s. Bấm s để sẵn sàng: ")
    if start == "s":
        print("30s chuẩn bị !")
        time.sleep(3)
        print("Bắt đầu !")
        guess = input()
        while True:
            if guess == "tu":
                print("Hết giờ !")
                break
            elif int(guess) == a:
                print("Chính xác !")
                tienthuong += 5000000
                break
            elif int(guess) > a:
                print("Thấp hơn !")
            elif int(guess) < a:
                print("Cao hơn !")

            guess = input()
        print()
        print("Sản phẩm còn lại ! Nhanh lên nào !")
        print()
        while True:
            if guess == "tu":
                break
            guess = input()
            if guess == "tu":
                print("Hết giờ !")
                break
            elif int(guess) == b:
                print("Chính xác !")
                tienthuong += 5000000
                break
            elif int(guess) > b:
                print("Thấp hơn !")
            elif int(guess) < b:
                print("Cao hơn !")
if ch == 2:
    start = input("Bạn có 60s. Bấm s để sẵn sàng: ")
    if start == "s":
        print("60s chuẩn bị !")
        time.sleep(3)
        print("Bắt đầu !")
        guess = input()
        while True:
            if guess == "tu":
                print("Hết giờ !")
                break
            elif int(guess) == b:
                print("Chính xác !")
                tienthuong += 5000000
                break
            elif int(guess) > b:
                print("Thấp hơn !")
            elif int(guess) < b:
                print("Cao hơn !")
            guess = input()
        print()
        print("Sản phẩm còn lại ! Nhanh lên nào !")
        print()
        while True:
            if guess == "tu":
                break
            guess = input()
            if guess == "tu":
                print("Hết giờ !")
                break
            elif int(guess) == a:
                print("Chính xác !")
                tienthuong += 5000000
                break
            elif int(guess) > a:
                print("Thấp hơn !")
            elif int(guess) < a:
                print("Cao hơn !")
print("Giá của sản phẩm thứ nhất là: ", a)
print("Giá của sản phẩm thứ hai là: ", b)
if tienthuong == 0:
    print("Thật tiếc, bạn đã không chiến thắng trong trò chơi này !")
else:
    print(f"Chúc mừng bạn với {tienthuong}đ tiền thưởng của Hãy chọn giá đúng !")
print("Hẹn gặp lại bạn trong phần quay bánh xe số !")
