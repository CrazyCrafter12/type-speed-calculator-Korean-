import time
from random import *

sentence = {1:"삶이 있는 한 희망은 있다.", 2:"오랫동안 꿈을 그리는 사람은 마침내 그 꿈을 닮아간다."}
#1:36, 2:68
def typing():
    #타이머 시작
    rand_sent = sentence[int(random() * 2) +1]
    begin_timer = time.time()
    typed_sent = input(rand_sent)

    if typed_sent == rand_sent:
        stop_timer = time.time()
        result_time = round(stop_timer - begin_timer, 1)

        if rand_sent == sentence[1]:
            result_speed = round(36/result_time, 1)*60
            print("당신의 타자 속도는 {0}타/분입니다.".format(result_speed))

        elif rand_sent == sentence[2]:
            result_speed = round(68/result_time, 1)*60
            print("당신의 타자 속도는 {0}타/분입니다.".format(result_speed))
    
    elif typed_sent != rand_sent:
        stop_timer = time.time()
        print("잘못 입력하셨습니다. 다시 실행해 주세요.")


typing()