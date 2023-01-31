from PIL import ImageDraw,ImageFont,Image
import cv2
import numpy as np
import math

'''ASCII-символы от тёмного до самого светлого, 
источник - https://stackoverflow.com/questions/30097953/ascii-art-sorting-an-array-of-ascii-characters-by-brightness-levels-c-c'''
chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

char_width = 8
char_height = 8

char_list=list(chars)
char_len=len(char_list)
interval=char_len/256

def get_char(value):
    '''Определение глубины цвета символа, где value = относительная яркость света'''
    return char_list[math.floor(value*interval)]

def cam_to_ASCII():
    '''Преобразование видео c вебки в видео из ASCII-символов'''
    cap = cv2.VideoCapture(0)
    cap.set(3, 500)
    cap.set(4, 300)

    '''Выбор шрифта символов'''
    fnt=ImageFont.truetype('fonts/BRITANIC.ttf', 20)
    
    while True:
        _,img=cap.read()
        img=Image.fromarray(img)

        WIDTH, HEIGHT = img.size
        '''Сжатие под заданные размеры символов'''
        img = img.resize((int(WIDTH / char_width), int(HEIGHT / char_height)), Image.NEAREST)
        width, height = img.size
        screen = img.load()
        
        '''Создание пустого чёрного файла-"полотна" для записи символов'''
        outputImage = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
       
        drw=ImageDraw.Draw(outputImage)

        for i in range(height):
            for j in range(width):
                '''Определение цвета пикселя'''
                r, g, b = screen[j, i]
                '''Вычисление относительной яркости цвета,
                источник формулы https://habr.com/ru/post/304210/'''
                h = int(0.2126*r+0.7152*g+0.0722*b)
                drw.text((j * char_width, i * char_height), get_char(h), font=fnt, fill=(r, g, b))


        open_cv_image=np.array(outputImage)
        '''q = кнопка завершения работы программы'''
        key=cv2.waitKey(1)
        if key == ord("q"):
            break
        cv2.imshow("Cam_to_ASCII",open_cv_image)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cam_to_ASCII()