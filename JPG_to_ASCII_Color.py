from PIL import Image, ImageDraw, ImageFont
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

def JPG_to_ASCII_colored():
    '''Преобразование изображения в цветное изображение из ASCII-символов'''
    print ('Введите имя файла')
    file_name=str(input())
    img = Image.open('input_files/'+file_name)

    WIDTH, HEIGHT = img.size
    '''Сжатие под заданные размеры символов'''
    img = img.resize((int(WIDTH / char_width), int(HEIGHT / char_height)), Image.NEAREST)
    width, height = img.size
    img = img.load()
    
    '''Создание пустого чёрного файла-"полотна" для записи символов'''
    ascii_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0)) 
    
    '''Выбор шрифта символов'''
    fnt = ImageFont.truetype('fonts/BRITANIC.ttf', 17)

    drw = ImageDraw.Draw(ascii_img)

    for i in range(height):
        for j in range(width):
            '''Определение цвета пикселя'''
            r, g, b = img[j, i]
            '''Вычисление относительной яркости цвета,
            источник формулы https://habr.com/ru/post/304210/'''
            h = int(0.2126*r+0.7152*g+0.0722*b)
            '''Вставка символа по нужным координатам'''
            drw.text((j * char_width, i * char_height), get_char(h), font=fnt, fill=(r, g, b))
    
    ascii_img.save('output_files/'+'ASCII_colored_'+file_name)
    
if __name__ == '__main__':
    JPG_to_ASCII_colored()