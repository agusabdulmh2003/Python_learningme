
# import keyword
# print(keyword.kwlist)


# a=20
# b=10
# if a/b==2:
#     print("yap")
# else:
#     print("Blok")


 
#indentasi line continaution
# a=20
# b=10
# if a/b==2:print("yap")
# else:print("Blok")


# a= 100
# b= 50
# if a<b :
#     print("y")
# else:
#     print("z")




# day = input("hari apa ini ? : ")
# hari_ini = (day)

# if(hari_ini == "Senin"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Selasa"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Rabu"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Kamis"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Jumat"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Sabtu"):
#     print("Saya akan libur")
# elif(hari_ini == "Minggu"):
#     print("Saya akan libur")





# nama = input("hari apa ini ? : ")
# hari_ini = (day)
# def sapa(nama) :
#     '''ini merupakan docstring'''
#     print("hai selamat pagi", nama)
# sapa("agus")
# print(sapa.__doc__)



# menentukan tipe data
# a=23
# b='apel'
# c=3.21
# d="cabai,1,kg"

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))






# konversi tipe data
# a=23
# print(type(a))
# # membuat variabel baru
# p=float(a)  
# print(p)
# print(type(p))






# formating number
# print('saya mempunyai %d kucing'%7)
# print('saya mempunyai %3d kucing'%7)
# print('saya mempunyai %03d kucing'%7)
# print('saya mempunyai %f kucing'%7)
# print('saya mempunyai %.2f kucing'%7)




# x=20
# y=25

# print('x =',x)
# print('y =',y)
# print('\n')

# print('x == y maka',x==y)
# print('x != y maka',x !=y)
# print('x < y maka',x<y)
# print('x > y maka',x>y)
# print('x <= y maka',x<=y)
# print('x >= y maka',x>=y)


# tugas  program konstanta

# '''jumlah hari dalam 1 bulan'''
# bln=30 
# jml = input("berapa kali kamu libur dalam bulan ini ? : ")
# # hari_ini = (day)

# print(bln-jml)



# konstanta
# import Constants 
# tahun= 12
# bulan= 30

# print(Constants.tahun)
# print(Constants.bulan)



# def constant(f):
#     def fset(self, value):
#         raise TypeError
#     def fget(self):
#         return f()
#     return property(fget, fset)

# class _Const(object):
#     @constant
#     def FOO():
#         return 0xBAADFACE
#     @constant
#     def BAR():
#         return 0xDEADBEEF

# CONST = _Const()

# print CONST.FOO
##3131964110

# CONST.FOO = 0
##Traceback (most recent call last):
##    ...
##    CONST.FOO = 0
##TypeError: None



# konstanta
# from asyncio import constant


# PI = 3.14
# GRAVITASI = 9.8

# print(constant.PI)
# print(constants.GRAVITASI)















# """The asyncio package, tracking PEP 3156."""

# flake8: noqa

# import sys

# # This relies on each of the submodules having an __all__ variable.
# from .base_events import *
# from .coroutines import *
# from .events import *
# from .exceptions import *
# from .futures import *
# from .locks import *
# from .protocols import *
# from .runners import *
# from .queues import *
# from .streams import *
# from .subprocess import *
# from .tasks import *
# from .threads import *
# from .transports import *

# __all__ = (base_events.__all__ +
#            coroutines.__all__ +
#            events.__all__ +
#            exceptions.__all__ +
#            futures.__all__ +
#            locks.__all__ +
#            protocols.__all__ +
#            runners.__all__ +
#            queues.__all__ +
#            streams.__all__ +
#            subprocess.__all__ +
#            tasks.__all__ +
#            threads.__all__ +
#            transports.__all__)

# if sys.platform == 'win32':  # pragma: no cover
#     from .windows_events import *
#     __all__ += windows_events.__all__
# else:
#     from .unix_events import *  # pragma: no cover
#     __all__ += unix_events.__all__
# """The asyncio package, tracking PEP 3156."""

# # flake8: noqa

# import sys

# This relies on each of the submodules having an __all__ variable.
# from .base_events import *
# from .coroutines import *
# from .events import *
# from .exceptions import *
# from .futures import *
# from .locks import *
# from .protocols import *
# from .runners import *
# from .queues import *
# from .streams import *
# from .subprocess import *
# from .tasks import *
# from .threads import *
# from .transports import *

# __all__ = (base_events.__all__ +
#            coroutines.__all__ +
#            events.__all__ +
#            exceptions.__all__ +
#            futures.__all__ +
#            locks.__all__ +
#            protocols.__all__ +
#            runners.__all__ +
#            queues.__all__ +
#            streams.__all__ +
#            subprocess.__all__ +
#            tasks.__all__ +
#            threads.__all__ +
#            transports.__all__)

# if sys.platform == 'win32':  # pragma: no cover
#     from .windows_events import *
#     __all__ += windows_events.__all__
# else:
#     from .unix_events import *  # pragma: no cover
#     __all__ += unix_events.__all__











# C:\Users\ACER\AppData\Local\Programs\Python\Python310\lib\asyncio\__init__.py



# import numpy as np
# import cv2

# img=cv2.imread('contoh.jpg')
# cv2.imshow('contoh.jpg', img)
# cv2.waitKey(0) &0xFF

# cv2.destroyAllWindows()


# masuk=input("masukan uang : ")
# keluar1=input("uang keluar : ")
# keluar2=input("uang keluar : ")
# print (masuk -(keluar1+keluar2))



# import os
# os.remove("hand.txt")