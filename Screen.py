# -*- coding: utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width=value

    @property
    def heigth(self):
        return self.__heigth
    @heigth.setter
    def heigth(self,value):
        self.__heigth=value

    @property
    def resolution(self):
        return self.__width * self.__heigth

# test:
s = Screen()
s.width = 1024
s.heigth = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' %s.resolution