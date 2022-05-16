import os
from PIL import Image

def get_avg_fps(PIL_Image_object):
    """ Returns the average framerate of a PIL Image object """
    PIL_Image_object.seek(0)
    frames = 0
    duration = []
    while True:
        try:
            frames += 1
            duration.append(PIL_Image_object.info['duration'])
            PIL_Image_object.seek(PIL_Image_object.tell() + 1)
            # print(duration)
        except EOFError:
            return duration
    return None

def main():
    img_obj = Image.open("gift.gif")
    duration = get_avg_fps(img_obj)
    # print(duration)
    flag = ""
    for i in duration:
        flag += (chr( int(i // 10)))
    print(flag)

if __name__ == '__main__':
    main()