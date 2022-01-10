import time
from random import *

sentence = [{"name":"삶이 있는 한 희망은 있다.", "length":36}, 
    {"name":"오랫동안 꿈을 그리는 사람은 마침내 그 꿈을 닮아간다.", "length":68}, 
    {"name":"사람의 행복과 불행을 좌우하는 것은 비교이다.", "length":57}]

(sentence[0])["length"]

def typing():
    rand_int = int(random() * 3)
    rand_sent = (sentence[rand_int])["name"]
    begin_timer = time.time()
    typed_sent = input(rand_sent)

    if typed_sent == rand_sent:
        stop_timer = time.time()
        result_time = round(stop_timer - begin_timer, 1)

        result_speed = round((sentence[rand_int])["length"] / result_time, 1) * 60
        print("당신의 타자 속도는 {0}타/분입니다.".format(result_speed))
    else:
        stop_timer = time.time()
        print("잘못 입력하셨습니다. 다시 입력해 주세요.")

typing()
