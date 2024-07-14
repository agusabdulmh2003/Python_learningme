# # class komputer
# # 	def __init__(self,pabrikan,nama,jenis,harga):
# # 		self.pabrikan= pabrikan
# # 		self.nama =nama
# # 		self.jenis=jenis
# # 		self.harga= harga

# # class prosesor(komputer):
# # 	def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
# # 		super().__init__(pabrikan,nama,'prosesor',harga)
# # 		self.jumlah_core = jumlah_core
# # 		self.speed = speed

# # class ram(komputer):
# # 	def __init__(self,pabrikan,nama,harga,kapasitas):
# # 		super().__init__(pabrikan,nama,'RAM',harga)
# # 		self.kapasitas = kapasitas

# # class hdd(komputer):
# # 	def __init__(self,pabrikan,nama,harga,kapasitas,rpm):
# # 		super().__init__(pabrikan,nama,'SATA',harga)
# # 		self.kapasitas = kapasitas
# #      	self.rpm = rpm

# # p = prosesor('intel','core i7 7740x',435000,4,'4.3GHz')
# # m =ram('vgen','dddr6 SODimm pc',328000,'4GB')
# # h =hdd('seagate','hdd 2.5 inch',290000,'500GB',7200)

# # parts=[p,m,h]
# # for part in parts:
# # 	print('{} {} produksi {}'.format(part.jenis,part.nma,part.pabrikan))




# ## polimorfisme

# # class baca :
# #     def __init__(self,membaca):
# #     self.media=membaca
# # def informasi (self):
# #     print("Anda memilih media " ,self.media)
# # def keterangan(self):
# #     print("media%s belum diketahiu" % self.media)

# # class mediakoran(baca):
# #     def informasikoran(self):
# #         membaca.info(self)
# #     def keterangan(self):
# #         print("koran yang populer di masyarakat : poskota, kompas, reput")
    

# # class mediamajalah(baca):
# #     def informasimajalah(self):
# #         membaca.info(self)
# #     def keterangan(self):
# #         print("majalah yang populer di masyarakat : poskota, kompas, reput")

# # class mediainternet(baca):
# #     def infomasiinternet(self):
# #         membaca.info(self)
# #     def keterangan(self):
# #         print("internet yang populer di masyarakat : poskota, kompas, reput")

# # class mediapamflet(baca):
# #     def infomasipamflet(self):
# #         membaca.info(self)
# #     def keterangan(self):
# #         print("pamflet yang populer di masyarakat : poskota, kompas, reput")




# #class absttrak 

# from abc import ABC, abstrakmethod

# class animal (ABC):
#     @abstrakmethod
#     def move(self):
#         print('animal moves')

# class  cat (animal):
#     def move(self):
#         super().move()
#         print('cat moves ')

# c= cat()
# c.move()



# # eror handling 

# z= 0
# try:
#     x =1/z
#     print(x)
# except ZeroDivisionError:
#     print("tidank bisa dibagi ")

# try:
#     print(x)
# except:
#     print("error")
    