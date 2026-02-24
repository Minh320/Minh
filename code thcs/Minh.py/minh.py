import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1" 

import sys
import time
import random
import threading

lyrics = [
    (1, "Cầm nhẫn cưới trên tay"),
    (2, "Em vội lau đi nước mắt ngay"),
    (3, "Đàn ông tốt như vậy"),
    (4, "Nếu là anh cũng sẽ yêu thôi"),
    (5, "Bờ môi đã chạm rồi"),
    (6, "Anh cũng thấy bồi hồi"),
    (7, "Thế nhưng! Thế nhưng.."),
    (8, "Anh vui đến nổi nghẹn ngào"),
    (9, "Nhìn người ta cầm nhẫn cưới trao"),
    (10, "Anh cũng có chút tự hào"),
    (11, "Vì người mình thương hạnh phúc nhường nào"),
    (12, "Áo cưới em màu trắng tinh"),
    (13, "Cô gái anh thật rất xinh"),
    (14, "Giật mình cứ ngỡ anh đứng cạnh em trong lễ cưới")
]

timeline = [
    0.8, 2.0, 4.0, 5.7, 7.8, 9.5, 11.0, 13.0,
    15.0, 17.0, 18.7, 20.4, 22.0, 23.1
]

colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m"]

# Hiệu ứng chữ 
def effect_typewriter(line, duration=1.0):
    color = random.choice(colors)
    delay = max(duration / max(len(line), 1), 0.01)
    for char in line:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def effect_slide_right(line, duration=1.0):
    color = random.choice(colors)
    steps = 5
    for i in range(steps + 1):
        sys.stdout.write("\r" + " " * i + color + line + "\033[0m")
        sys.stdout.flush()
        time.sleep(duration / (steps + 1))
    print()

def effect_slide_left(line, duration=1.0):
    color = random.choice(colors)
    steps = 5
    for i in range(steps, -1, -1):
        sys.stdout.write("\r" + " " * i + color + line + "\033[0m")
        sys.stdout.flush()
        time.sleep(duration / (steps + 1))
    print()

def effect_wave(line, duration=1.0):
    color = random.choice(colors)
    delay = max(duration / max(len(line), 1), 0.01)
    new_line = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(line)])
    for char in new_line:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def effect_char_color(line, duration=1.0):
    delay = max(duration / max(len(line), 1), 0.01)
    for char in line:
        color = random.choice(colors)
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

effects_list = [
    effect_typewriter,
    effect_slide_right,
    effect_wave,
    effect_char_color
]

def display_lyrics():
    start_time = time.time()
    for i, (lyric_id, line) in enumerate(lyrics):
        wait_time = timeline[i] - (time.time() - start_time)
        if wait_time > 0:
            time.sleep(wait_time)

        if lyric_id == 7:
            effect_slide_left(line, duration=1.5)
        else:
            effect = random.choice(effects_list)
            effect(line, duration=1.0)

if __name__ == "__main__":
    display_lyrics()




def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang/chieu_cao**2
    return bmi

heigh = float(input("Nhập chiều cao (m): "))
weight = float(input("Nhập cân nặng (kg): "))
bmi = tinh_bmi(heigh, weight)

print(f"Chỉ số bmi là: {bmi}")