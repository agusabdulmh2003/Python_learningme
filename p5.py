
'''


w = mode menulis dan menghapus data
r = hanya membaca
a = menambahkan data di akhir baris
r+ = membaca dan menulis
splitline = membuat kata menjadi list tanpa \n
line.strip = menghilangkan spasi di depan dan ekor 


'''


# membuat atau menambah file
# file = open("pp.txt", 'w')
# file.write("ini adalah teks yang di buat dengan py")
# file.write("\n ini baris kedua")
# file.write("\n ini baris tiga")
# file.close()




# membaca file 
# baca=open("pp.txt",'a')
# baca.write("\nnama kamu ")
# print(baca.readLine())
# baca.close()

# with  open('note.txt') as file:  #membaca file dalam satu directory 
#     print(file.read())


# f = open("note.txt","r") #r hanya untuk membaca
# # print(f.read())
# print(f.readline(baris ke berapa)) # hanya baris pertama
# print(f.close()) # menutup/menghapus
# splitline di gunakan sebagai penganti \n


# with  open("D:\web\pyton lat 1/fileku.txt","r") as file:  #membaca file dalam directory berbeda 
#     print(file.read())


# membuat atau menambah file
# from turtle import update
# from ast import Str

# us3=(input("masuka nama file yang ingin anda buat : "))
# us1=(input("masuka nama anda  : "))
# # us2=(input("masuka kelas anda : "))
# file = open(us3, 'a')

# file.write(us1)
# # file.write("\n"+ us2)
# # print(baca.readLine())
# if us3=='C:/praktikum python':
#     update(us3)
# file.close()





# from ast import Str
# while True:
#     fname= Str(input('masukan nama file: '))
#     try:
      
#         fread=open(fname,'r')
#         print(fread)
#         break
#     except:
#         print('file yang anda masukan tidak ada')

# nama=[]
# for line in fread:
#     nama.append(line.strip())

# nama=sorted(nama)
# fwrite = open('output_' + fname,'w')
# for item in nama:
#     fwrite.write(item + '\n')

# fwrite.close()





# menampilkan file dengan jenis txt
# import os

# files = [file for file in os.listdir() if file.split(".")[-1] == "txt"]

# for file in files:
#     print(file)
#     input = open(file,"r")
#     output = open(file,"w")

#     for line in input:
#         print(line)
#         # if line is good, write it to output

#     input.close()
#     output.close()








# mengappus file
# import os
# if os.path.exists(“file.txt”):
# os.remove(“file.txt”)
 
# print(“File deleted successfully”)
# else:
# print(“The file does not exist”)