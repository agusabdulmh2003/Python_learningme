# class segitiga:

#     def __init__(self, alas, tinggi) :
#         self.alas=alas
#         self.tinggi=tinggi
#         self.luas= 0.5 * alas * tinggi
# segitiga_besar=segitiga(100,80)

# print(f'alas: {segitiga_besar.alas}')
# print(f'tinggi: {segitiga_besar.tinggi}')
# print(f'luas: {segitiga_besar.luas}')




# class mobil :
#     def __init__(self,merk):
#         self._merk = merk
# sedan= mobil('toyota')
# print(f'merk: {sedan._merk}')
        




# class mobil :
#     def __init__(self,merk):
#         self.__merk = merk

#     def tampilkan_merk(self):
#         print(f'merk: {self.__merk}')


# jip= mobil('jeep')
# jip.tampilkan_merk()




# import cv2 
# gb = cv2.imread("rsttttt.png")
# print(gb)


import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write  code python mysql \n",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)





