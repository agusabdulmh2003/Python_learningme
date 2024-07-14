import numpy as np

# lis= ["apel","pisang","semangka","jeruk","pir","salak","manga","jambu","tebu"]
# lis.remove("apel")
# print(lis) #semua list

# print(lis[1]) # print index no 1

# print(lis[-1]) # print index no -1

# print(lis[2:5]) # print index no 2-5

# print(lis[:4]) # print index no 1-4

# print(lis[4:]) # print index no 4-selesai

# print(lis[:4]) # print index no 1-4

# print(lis[4::2]) #menambahkan loncat 2 angka

# print(lis[4::-2]) 


# lis1=[1,2,3,4,5,6]
# lis1.insert(6,7)  #menambahkan di index yang di pilih
# lis1.reverse()  #membalikan dari belakang
# print(lis1)






# /



#looping
# x= ("apel","pisang","semangka","jeruk")
# y= (1,2,3,4)
# for g in x:
#     print(g)



# if "apel" in x:  # cek isi list
#     print("ya buah itu ada")

# print(len(x)) # cek panjang 
# print("jeruk" in x) # cek isi dengan true/false

x= ("apel","pisang","semangka","jeruk")
# x.add("jambu ir")# menambahkan 1 item
# x.update("jambu""pir","salak","manga")# menambahkan banyak item
# x.remove("jambu")# menghapus
# print(x)
# x.discard("jambu")# menghapus


# menagabung item
# d=x.union(y) # 2-1 2-1
# d=x.update(y) # 2-1 2-1



#Dictionaries membuat nama dan isi
# a={  
#     "nama" : "adi",
#     "nim" : "1212",
#     "kelas" : "if21"
# }
# a["umur"] = "17"
# b=a["nama"] #akses item atau bisa mengunakan "GET" 
# c=a["nama"] = hamas # mengubah isi
# a.pop(nim) #menghapus "POPITEM"
# a.del[nim]
# for r,t in a.items():
#     print(r,t)




# 	Multidimensional Array
# arrku=np.array([[1,2,3,4,5],[2,4,6,8,9]])
# print(type(arrKU))
# arr = np.array(42)



#  operasi aritmatika 
# a=np.array([1,2,3,4,5])
# b=np.array([2,4,6,8,3])

# print("tambah", a +b)
# print("kurang", a-b)
# print("kali", a *b)
# print("bagi", a /b)
# print("pangkat", a **b)


# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim) 