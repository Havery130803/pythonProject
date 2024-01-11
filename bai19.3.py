# Trò chơi Bánh xe số - Hãy chọn giá đúng

from random import randrange
import time

diem_1 = 0
diem_2 = 0
print("PHẦN QUAY BÁNH XE SỐ")
name_1 = input("Tên người chơi 1: ")
name_2 = input("Tên người chơi 2: ")
lt_1 = int(input(f"Nhập số tiền thưởng đã có của bạn {name_1}: "))
lt_2 = int(input(f"Nhập số tiền thưởng đã có của bạn {name_2}: "))
if lt_1 >= lt_2:
    print(f"Bạn {name_1} sẽ là người quay trước, và bạn có 2 lượt quay. Chúc bạn may mắn !!! ")
    q = input("Nhấn q để quay: ")
    if q == "q":
        print("100 100 !!!!!")
        time.sleep(randrange(20, 30))
        diem = randrange(1, 21) * 5
        if diem == 100:
            print("Bạn có 1.000.000đ với 100đ. Bạn quá giỏi !!!")
            diem_1 = 100
            print(f"Bạn hãy chờ bạn {name_2} một lát nhé !!!")
        else:
            diem_1 += diem
            print(f"{diem} điểm !!")
            con = input("Bạn có muốn quay tiếp không. Nhấn c để có, nhấn k để dừng cuộc choi ")
            if con == "c":
                q = input("Nhấn q để quay: ")
                if q == "q":
                    thieu = 100 - diem_1
                    print(f"{thieu} {thieu} !!!!!")
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    if diem_1 + diem == 100:
                        print("Bạn có 1.000.000đ với 100đ. Bạn quá giỏi")
                    elif diem_1 + diem < 100:
                        diem_1 += diem
                        print(f"{diem} điểm !!! Rất tốt !!!")
                        print(f"Bạn {name_1} đã có {diem_1} điểm của chương trình ! Và hãy chờ bạn {name_2} một lát")
                    else:
                        print(f"{diem} điểm !! Quá mất mục tiêu rồi ! Thật đáng tiếc")
                        diem_1 += diem
                        diem_1 -= 100
                        print(f"Bạn {name_1} đã có {diem_1} của chương trình ! Và hãy chờ bạn {name_2} một lát")
            else:
                print(f"Bạn {name_1} đã có {diem_1} điểm của chương trình ! Và hãy chờ bạn {name_2} một lát !")
    print(f"Và xin mời bạn {name_2}. Cố gắng lên và bạn sẽ có 1 triệu đồng !!!!")
    q = input("Nhấn q để quay: ")
    if q == "q":
        print("100 100 !!!!!")
        time.sleep(randrange(20, 30))
        diem = randrange(1, 21) * 5
        if diem == 100:
            print(f"Bạn có 1.000.000đ với 100đ. Bạn quá giỏi !!!")
            diem_2 = 100
        else:
            diem_2 += diem
            print(f"{diem} điểm !!")
            con = input("Bạn có muốn quay tiếp không. Nhấn c để có, nhấn k để dừng cuộc choi ")
            if con == "c":
                q = input("Nhấn q để quay: ")
                if q == "q":
                    thieu = 100 - diem_2
                    print(f"{thieu} {thieu} !!!!!")
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    if diem_2 + diem == 100:
                        print(f"Bạn có 1.000.000đ với 100đ. Bạn quá giỏi !!! Và mời bạn qua bên kia để chờ đợi bạn {name_2}")
                    elif diem_2 + diem < 100:
                        diem_2 += diem
                        print(f"{diem} điểm !! ")
                    else:
                        print(f"{diem} điểm !!! Quá mất mục tiêu rồi ! Thật đáng tiếc")
                        diem_2 += diem
                        diem_2 -= 100
        if diem_1 > diem_2:
            print(f"Vậy là bạn có {diem_2} điểm, và bạn sẽ ra về. Cảm ơn bạn đến với chương trình !")
            print(f"Và chúc mừng bạn {name_1}, bạn đã chiến thắng. Hẹn gặp lại bạn !")
        elif diem_1 < diem_2:
            print(f"Vậy là bạn có {diem_2} điểm, và bạn là người chiến thắng. Chúc mừng bạn !")
            print(f"Và cảm ơn bạn {name_1} đã đến với chương trình. Hẹn gặp lại bạn !")
        else:
            print("2 bạn sẽ quay 1 lượt phụ để tìm ra người chiến thắng: ")
            print(f"Xin mời bạn {name_1}, bạn sẽ quay trước !!!")
            while(diem_1 == diem_2):
                q = input("Nhấn q để quay: ")
                if q == "q":
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    diem_1 = diem
                    print(f"{diem} điểm. Mời {name_2} !!!")
                q = input("Nhấn q để quay: ")
                if q == "q":
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    diem_2 = diem
                    if diem_1 > diem_2:
                        print(f"Vậy là bạn có {diem_2} điểm, và bạn sẽ ra về. Cảm ơn bạn đến với chương trình !")
                        print(f"Và chúc mừng bạn {name_1}, bạn đã chiến thắng. Hẹn gặp lại bạn !")
                    elif diem_1 < diem_2:
                        print(f"Vậy là bạn có {diem_2} điểm, và bạn là người chiến thắng. Chúc mừng bạn !")
                        print(f"Và cảm ơn bạn {name_1} đã đến với chương trình. Hẹn gặp lại bạn !")
                    else:
                        print("2 bạn sẽ quay 1 lượt phụ để tìm ra người chiến thắng: ")
                        print(f"Xin mời bạn {name_1}, bạn sẽ quay trước !!!")

else:
    print(f"Bạn {name_2} sẽ là người quay trước, và bạn có 2 lượt quay. Chúc bạn may mắn !!! ")
    q = input("Nhấn q để quay: ")
    if q == "q":
        print("100 100 !!!!!")
        time.sleep(randrange(20, 30))
        diem = randrange(1, 21) * 5
        if diem == 100:
            print("Bạn có 1.000.000đ với 100đ. Bạn quá giỏi !!!")
            diem_2 = 100
            print(f"Bạn hãy chờ bạn {name_1} một lát nhé !!!")
        else:
            diem_2 += diem
            print(f"{diem} điểm !!")
            con = input("Bạn có muốn quay tiếp không. Nhấn c để có, nhấn k để dừng cuộc choi ")
            if con == "c":
                q = input("Nhấn q để quay: ")
                if q == "q":
                    thieu = 100 - diem_2
                    print(f"{thieu} {thieu} !!!!!")
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    if diem_2 + diem == 100:
                        print("Bạn có 1.000.000đ với 100đ. Bạn quá giỏi")
                    elif diem_2 + diem < 100:
                        diem_2 += diem
                        print(f"{diem} điểm !!! Rất tốt !!!")
                        print(f"Bạn {name_2} đã có {diem_2} điểm của chương trình ! Và hãy chờ bạn {name_1} một lát")
                    else:
                        print(f"{diem} điểm !! Quá mất mục tiêu rồi ! Thật đáng tiếc")
                        diem_2 += diem
                        diem_2 -= 100
                        print(f"Bạn {name_2} đã có {diem_2} của chương trình ! Và hãy chờ bạn {name_1} một lát")
            else:
                print(f"Bạn {name_2} đã có {diem_2} điểm của chương trình ! Và hãy chờ bạn {name_1} một lát !")
    print(f"Và xin mời bạn {name_1}. Cố gắng lên và bạn sẽ có 1 triệu đồng !!!!")
    q = input("Nhấn q để quay: ")
    if q == "q":
        print("100 100 !!!!!")
        time.sleep(randrange(20, 30))
        diem = randrange(1, 21) * 5
        if diem == 100:
            print(f"Bạn có 1.000.000đ với 100đ. Bạn quá giỏi !!!")
            diem_1 = 100
        else:
            diem_1 += diem
            print(f"{diem} điểm !!")
            con = input("Bạn có muốn quay tiếp không. Nhấn c để có, nhấn k để dừng cuộc choi ")
            if con == "c":
                q = input("Nhấn q để quay: ")
                if q == "q":
                    thieu = 100 - diem_1
                    print(f"{thieu} {thieu} !!!!!")
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    if diem_1 + diem == 100:
                        print(f"Bạn có 1.000.000đ với 100đ. Bạn quá giỏi !!!")
                        diem_1 = 100
                    elif diem_1 + diem < 100:
                        diem_1 += diem
                        print(f"{diem} điểm !! ")
                    else:
                        print(f"{diem} điểm !!! Quá mất mục tiêu rồi ! Thật đáng tiếc")
                        diem_1 += diem
                        diem_1 -= 100
        if diem_1 > diem_2:
            print(f"Vậy là bạn có {diem_1} điểm, và bạn sẽ ra về. Cảm ơn bạn đến với chương trình !")
            print(f"Và chúc mừng bạn {name_2}, bạn đã chiến thắng. Hẹn gặp lại bạn !")
        elif diem_1 < diem_2:
            print(f"Vậy là bạn có {diem_1} điểm, và bạn là người chiến thắng. Chúc mừng bạn !")
            print(f"Và cảm ơn bạn {name_2} đã đến với chương trình. Hẹn gặp lại bạn !")
        else:
            print("2 bạn sẽ quay 1 lượt phụ để tìm ra người chiến thắng: ")
            print(f"Xin mời bạn {name_1}, bạn sẽ quay trước !!!")
            while (diem_1 == diem_2):
                q = input("Nhấn q để quay: ")
                if q == "q":
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    diem_1 = diem
                    print(f"{diem} điểm. Mời {name_2} !!!")
                q = input("Nhấn q để quay: ")
                if q == "q":
                    time.sleep(randrange(20, 30))
                    diem = randrange(1, 21) * 5
                    diem_2 = diem
                    if diem_1 > diem_2:
                        print(f"Vậy là bạn có {diem_1} điểm, và bạn sẽ ra về. Cảm ơn bạn đến với chương trình !")
                        print(f"Và chúc mừng bạn {name_2}, bạn đã chiến thắng. Hẹn gặp lại bạn !")
                    elif diem_1 < diem_2:
                        print(f"Vậy là bạn có {diem_1} điểm, và bạn là người chiến thắng. Chúc mừng bạn !")
                        print(f"Và cảm ơn bạn {name_2} đã đến với chương trình. Hẹn gặp lại bạn !")
                    else:
                        print("2 bạn sẽ quay 1 lượt phụ để tìm ra người chiến thắng: ")
                        print(f"Xin mời bạn {name_1}, bạn sẽ quay trước !!!")
print("Và chúng ta đến với phần chơi tiếp theo của Hãy chọn giá đúng !!!!!!!!")
