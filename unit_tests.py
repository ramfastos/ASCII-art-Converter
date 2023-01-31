import unittest
from main import ASCII_generator, JPG_to_ASCII_colored, JPG_to_ASCII_gray

class Test_ASCII_main(unittest.TestCase):
    '''Тесты для main.py, JPG_to_ASCII_Color.py, JPG_to_ASCII_Gray.py'''

    def test_strange_number(self):
        '''Ввод при выборе некорректной опции конвертирования'''
        self.assertEqual(ASCII_generator(5), 'Введите корректное значение' )

    def test_color_image(self):
        '''Ввод при выборе цветного изображения'''
        self.assertEqual(ASCII_generator(1), 'imgc' )     #Ввести girl_with_pearl.jpg
    
    def test_gray_image(self):
        '''Ввод при выборе чёрно-белого изображения'''
        self.assertEqual(ASCII_generator(2), 'imgbw' )    #Ввести mona_lisa.jpg

    def test_video(self):
        '''Ввод при выборе видео-конвертирования'''
        self.assertEqual(ASCII_generator(3), 'vid' )    #Ввести matrix.mp4

    def test_camera(self):
        '''Ввод при выборе камеры'''
        self.assertEqual(ASCII_generator(4), 'cam' )

    def test_value(self):
        '''Ошибка при вводе некорректного значения'''
        self.assertRaises(ValueError, ASCII_generator, 'abc')
        
    def test_png_color(self):
        '''Ошибка при выборе png-файла для конвертирования цветного изображения'''
        self.assertRaises(ValueError, JPG_to_ASCII_colored)     #Ввести morning.png
    
    def test_png_bw(self):
        '''Ошибка при выборе png-файла для конвертирования чёрно-белого изображения'''
        self.assertRaises(ValueError, JPG_to_ASCII_gray)     #Ввести morning.png

if __name__ == '__main__':
    unittest.main()
