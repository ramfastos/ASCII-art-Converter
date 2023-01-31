from JPG_to_ASCII_Color import JPG_to_ASCII_colored
from JPG_to_ASCII_Gray import JPG_to_ASCII_gray
from Video_to_ASCII import MP4_to_ASCII
from Camera_to_ASCII import cam_to_ASCII

def ASCII_generator(answer1):
    '''Конвертер изображения/видео в изображение/видео, состоящее из ASCII-символов'''

    if (int(answer1)==1):
        JPG_to_ASCII_colored()
        print ('Конвертирование завершено!')
        return ('imgc')
    elif (int(answer1)==2):
        JPG_to_ASCII_gray()
        print ('Конвертирование завершено!')
        return ('imgbw')
    elif (int(answer1)==3):
        print ('Нажмите q для выхода')
        MP4_to_ASCII()
        return ('vid')
    elif (int(answer1)==4):
        print ('Нажмите q для выхода')
        cam_to_ASCII()
        return ('cam')
    else: 
        return ('Введите корректное значение')

if __name__ == '__main__':
    print('Что необходимо конвертировать? (Введите цифру от 1 до 4)\n'
    '1)Изображение в цветную ASCII-мозайку\n'
    '2)Изображение в чёрно-белую ASCII-мозайку\n'
    '3)Видео в ASCII-мозайку\n'
    '4)Камеру в ASCII-мозайку')
    ASCII_generator(input())