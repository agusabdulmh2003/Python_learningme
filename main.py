# from msilib.schema import Class
# from tkinter import Button
# from unittest import TestCase
# from kivymd.uix.button import kivymd

# Button("hello word")

# while True:
#     i = int (input("masukan saldo: "))
#     j = int(input("pengeluaran : "))
#     if j < 0:
#         print(i = input('masukan saldo:\n'))
#         continue
#     s=(i-j)
#     k=(j+s)
#     if i == 0:
#         print("Exiting the Program")
#         break
#     print(f" sisa saldo anda {s}")

	
# while loop == "y" and status_login == True:
#         u = user[cek_user(user_id)]
#         print("SELAMAT DATANG DI ATM BANK BAGOOD")
#         print("1.Cek Saldo")
#         print("2.Transfer Uang")
#         print("3.Ambil Uang")
#         print("4.Logout")
#         print("5.Keluar ATM")
#         a = int(input("Silahkan pilih menu : "))
#         if a == 1:
#             print("")
#             print("Sisa Saldo anda adalah Rp.",u['saldo'])
#             print("")
#             print("")
#             loop = "n"
#         elif a == 2:
#             print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
#             no_rek = input("Masukan No Rekening Tujuan : ")
#             cnk = cek_rekening(no_rek)
             
#             if cnk >= 0:
#                 print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
#                 nominal = input("Nominal Yang Akan Di Transfer : ")
#                 tranfer_uang(nominal,no_rek)
#                 print("")
#                 loop = "n"
#             else:
#                 print("")
#                 print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
#                 print("")
#                 loop = "n"
                 
#         elif a == 3:
#             nominal = input("Nominal Yang Akan Di Tarik : ")
#             ambil_uang(nominal)
#             print("")
#             loop = "n"
#         elif a == 4:
#             status_login = False
             
#         elif a == 5:
#             status_login = False
#             loop = "n"
#             pakai_atm = "n"
#         else:
#             print("pilihan tidak tersedia")
#         if status_login == True:
             
#             input("kembali Ke menu (Enter) ")
#             print("")
#             loop = "y"


	
# user_id = 0
# loop = "n"
# user =  [
#             {   
#                 "id":"1234",
#                 "no_rekening":"1234567890",
#                 "username":"test",
#                 "pin":"4321",
#                 "saldo":0
#             },
#             {   
#                 "id":"4321",
#                 "no_rekening":"0987654321",
#                 "username":"test2",
#                 "pin":"1234",
#                 "saldo":25000000
#             }
#         ]
# status_login = False
# pakai_atm = "y"
 
# def cek_login(p):
#     for us in user:
#         if us['pin'] == p:
#             return us
#     return False       
     
# def cek_user(id):
#     for i in range(len(user)):
#         if user[i]['id'] == str(id):
#             return int(i)
#     return -1
 
# def cek_rekening(no):
#     for i in range(len(user)):
#         if str(user[i]['no_rekening']) == str(no):
#             return int(i)
#     return -1
 
# def tranfer_uang(uang,no_rekening):
#     index1 = cek_user(user_id)
#     index2 = cek_rekening(no_rekening)
#     if index1 >= 0:
#         if user[index1]['saldo'] >= int(uang):
#             user[index1]['saldo'] =user[index1]['saldo'] - int(uang)
#             user[index2]['saldo'] =user[index2]['saldo'] + int(uang)
#             print("Anda berhasil mentransfer uang Rp."+str(uang)+" ke Rekening "+no_rekening)
#             print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
#         else:
#             print("Ops saldo anda tidak cukup")
             
# def ambil_uang(uang):
#     index1 = cek_user(user_id)
#     if index1 >= 0:
#         if user[index1]['saldo'] >= int(uang):
#             user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
#             print("Anda berhasil menarik uang Rp."+str(uang))
#             print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
#         else:
#             print("Ops saldo anda tidak cukup")
 
 
# while pakai_atm == "y":
#     while status_login == False:
#         print("SELAMAT DATANG DI ATM BANK BAGOOD")
#         print("Silahkan masukan pin anda")
#         pin = input("Masukan PIN : ")
     
#         cl = cek_login(pin)
#         if cl != False:
#             print("selamat data "+cl['username'])
#             user_id = cl['id']
#             status_login = True
#             loop = "y"
#         else:
#             print("")
#             print("Ops PIN anda salah")
#             print("")
#             print("")
     
#     while loop == "y" and status_login == True:
#         u = user[cek_user(user_id)]
#         print("SELAMAT DATANG DI ATM BANK BAGOOD")
#         print("1.Cek Saldo")
#         print("2.Transfer Uang")
#         print("3.Ambil Uang")
#         print("4.Logout")
#         print("5.Keluar ATM")
#         a = int(input("Silahkan pilih menu : "))
#         if a == 1:
#             print("")
#             print("Sisa Saldo anda adalah Rp.",u['saldo'])
#             print("")
#             print("")
#             loop = "n"
#         elif a == 2:
#             print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
#             no_rek = input("Masukan No Rekening Tujuan : ")
#             cnk = cek_rekening(no_rek)
             
#             if cnk >= 0:
#                 print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
#                 nominal = input("Nominal Yang Akan Di Transfer : ")
#                 tranfer_uang(nominal,no_rek)
#                 print("")
#                 loop = "n"
#             else:
#                 print("")
#                 print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
#                 print("")
#                 loop = "n"
                 
#         elif a == 3:
#             nominal = input("Nominal Yang Akan Di Tarik : ")
#             ambil_uang(nominal)
#             print("")
#             loop = "n"
#         elif a == 4:
#             status_login = False
             
#         elif a == 5:
#             status_login = False
#             loop = "n"
#             pakai_atm = "n"
#         else:
#             print("pilihan tidak tersedia")
#         if status_login == True:
             
#             input("kembali Ke menu (Enter) ")
#             print("")
#             loop = "y"


















# def k(i+%X):

# return i+%X

# m=int(input("masukan saldo : "))
# i=int(input("pengeuaran : "))
# k=int(i+i+i+i+i+i)
# s=(m-k)
# #diskon 5% tiap pembelian di atas Rp.100rb
# while k>m:
#     break
# elif k<m:
#     print("Total Harga = ", "Rp.",s)
# else:
#     print ("saldo anda tidak cukup")
















# masuk=int(input("masukan uang : "))
# keluar1=int(input("uang keluar : "))
# keluar2=int(input("uang keluar : "))
# jumlahk=(keluar1+keluar2)
# total=(masuk-jumlahk)
# if (jumlahk>masuk):
#     print("anda tidak mempunyai saldo ")
# else:
#     print("sisa saldo " +str(total))





# 



# masuk=int(input("masukan uang : "))
# keluar1=int(input("uang keluar : "))
# h=(keluar+%)

# while keluar1 != masuk:
#     # Ask the user for a name.
#     new = input("uang keluar : ")

#     # Add the new name to our list.
# name=(keluar+new)

# # Show that the name has been added to the list.
# print(name)
    
# nomor = int(input("saldo "))
# saldo = int(input("keluar "))
# while %:
#     print(saldo)
#     saldo1 = saldo + saldo
# else:
#     while (saldo > nomor):
#         print("saldo anda" )
#         no = nomor - saldo1
#     print('Nomor Sekarang:')



# saldo=int(input("saldo "))
# keluar=int(input("pengeluaran "))
# while  saldo - keluar :
#     keluar1=int(input("pengeluaran "))
#     keluar2=int(input("pengeluaran "))
#     keluar3=int(input("pengeluaran "))
#     keluar4=int(input("pengeluaran "))
#     if (keluar + keluar1+keluar2 + keluar3 +keluar4):
#      break
# else:
#     print("saldo tidak cukup" + saldo-keluar)
    
     












# https://drive.google.com/drive/folders/16Cef43QJn61CVZJlnf1R1EZs-KgcEQAy





# b = int(input('Masukkan saldo: '))
# a = int(input('Pengeluaran(-1 ): '))
# while   a <+ (b):
#       a +=  int(input('Pengeluaran(-1 ): '))
#       if a >= b and a < b:
#         print(' ')
#       else:
#         print("Sisa saldo",(b-a)) 
#         break
# print('saldo anda habis' "Sisa saldo",(b-a))



# i = -1
# while i < len(listKota):
#   i += 1
#   if i % 2 == 0 and i > 0:
#     print('skip')
#     continue

#   # tidak dieksekusi ketika continue dipanggil
#   print(listKota[i])




# import turtle
# # turtle.color(yellow)
# skk = turtle.Turtle()
# skk2 = turtle.Turtle()
# star = turtle.Turtle()

# for i in range(30):
 
# 	skk.forward(60)
# 	skk.right(30)
	
# for y in range(34):
     
# 	skk2.forward(60)
# 	skk2.right(50)
	
	
# star.right(75)
# star.forward(100)
 
# for x in range(4):
#     star.right(144)
#     star.forward(100)
     
# turtle.done()
	


# import turtle   #Outside_In
# wn = turtle.Screen()
# wn.bgcolor("blue")
# wn.title("Turtle")
# skk = turtle.Turtle()
# skk.color("yellow")
 
# def sqrfunc(size):
#     for i in range(4):
#         skk.fd(size)
#         skk.right(90)
#         size = size-5
 
# sqrfunc(246)
# sqrfunc(226)
# sqrfunc(206)
# sqrfunc(186)
# sqrfunc(166)
# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)



# Python program to user input pattern
# using Turtle Programming
# import turtle #Outside_In
# import turtle
# import time
# import random

# print ("This program draws shapes based on the number you enter in a uniform pattern.")
# num_str = input("Enter the side number of the shape you want to draw: ")
# if num_str.isdigit():
# 	squares = int(num_str)

# angle = 180 - 180*(squares-2)/squares

# turtle.up

# x = 0
# y = 0
# turtle.setpos(x, y)


# numshapes = 8
# for x in range(numshapes):
# 	turtle.color(random.random(), random.random(), random.random())
# 	x += 5
# 	y += 5
# 	turtle.forward(x)
# 	turtle.left(y)
# 	for i in range(squares):
# 		turtle.begin_fill()
# 		turtle.down()
# 		turtle.forward(40)
# 		turtle.left(angle)
# 		turtle.forward(40)
# 		print (turtle.pos())
# 		turtle.up()
# 		turtle.end_fill()

# time.sleep(11)
# turtle.bye()



# Python program to draw
# Rainbow Benzene
# using Turtle Programming
# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
# 	t.pencolor(colors[x%6])
# 	t.width(x//100 + 1)
# 	t.forward(x)
# 	t.left(59)


# Python program to draw
# Spiral  Helix Pattern
# using Turtle Programming
 
# import turtle
# loadWindow = turtle.Screen()
# turtle.speed(2)
 
# for i in range(100):
#     turtle.circle(5*i)
#     turtle.circle(-5*i)
#     turtle.left(i)
 
# turtle.exitonclick()


# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput


# class LoginScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)


# class MyApp(App):

#     def build(self):
#         return LoginScreen()


# if __name__ == '__main__':
#     MyApp().run()



# temp=int(input('masukan'))
# if not (temp >= 0 and temp <= 30):
#     print('temp is good')
# elif  (temp<0 or temp >30):
#     print('temp kurang bagus')
# i=100
# while 1==1:
#     print(i)
#     i+=10
#     print(i)

# saldo=int(input("masukan saldo : "))
# keluar= None
# while not keluar:
#     keluar=input(" saldo keluar : ")

# print('saldo anda '+keluar)


