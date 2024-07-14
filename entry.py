import PySimpleGUI as sg
import pandas as pd

sg.theme('LightBlue')

EXCEL_FILE = 'entry.xlsx'

df = pd.read_excel(EXCEL_FILE)

layout=[
[sg.Text('Masukan Data Kamu: ')],

[sg.Text('Nama',size=(15,2)), sg.InputText(key='Nama')],
[sg.Text('NIM',size=(15,2)), sg.InputText(key='NIm')],
[sg.Text('No Telp',size=(15,2)), sg.InputText(key='Tlp')],
[sg.Text('Alamat',size=(15,2)), sg.InputText(key='Alamat')],
[sg.Text('Tgl Lahir',size=(15,2)), sg.InputText(key='Tgl Lahir'),
                                    sg.CalendarButton('Kalender', target='Tgl Lahir', format=('%d-%M-%Y'))],
[sg.Text('Jenis Kelamin',size=(15,2)), sg.Combo(['pria','wanita'],key='Jekel')],
[sg.Text('Hobi',size=(15,2)), sg.Checkbox('Belajar',key='Belajar'),
                            sg.Checkbox('Menonton',key='Menonton'),
                             sg.Checkbox('Musik',key='Musik')],
[sg.Submit(), sg.Button('clear'), sg.Exit()]

]

window=sg.Window('Form  pendaftaran gabut',layout)

def clear_input():
    for key in values:
        window[key]('  ')
        return sg.Text

while True :
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    elif event == 'Clear':
        clear_input()
    if event == 'Submit':
        df =df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data Berhasil Di Simpan')
        clear_input()

window.close()       