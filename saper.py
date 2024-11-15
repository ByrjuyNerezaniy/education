#Import__________________________________________________________________________________
from tkinter import *
from tkinter import ttk
import random
#Tkinter_Python____________________________________________________________________________
root = Tk()
root.title('САПЁР')
root.geometry("240x250") 
btn = ttk.Button(text=' ')
btn.place(x= 0, y = 0, width=30, height=30)
btn1 = ttk.Button(text=' ')
btn1.place(x= 30, y = 0, width=30, height=30)
btn2 = ttk.Button(text=' ')
btn2.place(x= 60, y = 0, width=30, height=30)
btn3 = ttk.Button(text=' ')
btn3.place(x= 90, y = 0, width=30, height=30)
btn4 = ttk.Button(text=' ')
btn4.place(x= 120, y = 0, width=30, height=30)
btn5 = ttk.Button(text=' ')
btn5.place(x= 150, y = 0, width=30, height=30)
btn6 = ttk.Button(text=' ')
btn6.place(x= 180, y = 0, width=30, height=30)
btn7 = ttk.Button(text=' ')
btn7.place(x= 210, y = 0, width=30, height=30)
# строка 2
btn_s2 = ttk.Button(text=' ')
btn_s2.place(x= 0, y = 30, width=30, height=30)
btn1_s2 = ttk.Button(text=' ')
btn1_s2.place(x= 30, y = 30, width=30, height=30)
btn2_s2 = ttk.Button(text=' ')
btn2_s2.place(x= 60, y = 30, width=30, height=30)
btn3_s2 = ttk.Button(text=' ')
btn3_s2.place(x= 90, y = 30, width=30, height=30)
btn4_s2 = ttk.Button(text=' ')
btn4_s2.place(x= 120, y = 30, width=30, height=30)
btn5_s2 = ttk.Button(text=' ')
btn5_s2.place(x= 150, y = 30, width=30, height=30)
btn6_s2 = ttk.Button(text=' ')
btn6_s2.place(x= 180, y = 30, width=30, height=30)
btn7_s2 = ttk.Button(text=' ')
btn7_s2.place(x= 210, y = 30, width=30, height=30)
# строка 3
btn_s3 = ttk.Button(text=' ')
btn_s3.place(x= 0, y = 60, width=30, height=30)
btn1_s3 = ttk.Button(text=' ')
btn1_s3.place(x= 30, y = 60, width=30, height=30)
btn2_s3 = ttk.Button(text=' ')
btn2_s3.place(x= 60, y = 60, width=30, height=30)
btn3_s3 = ttk.Button(text=' ')
btn3_s3.place(x= 90, y = 60, width=30, height=30)
btn4_s3 = ttk.Button(text=' ')
btn4_s3.place(x= 120, y = 60, width=30, height=30)
btn5_s3 = ttk.Button(text=' ')
btn5_s3.place(x= 150, y = 60, width=30, height=30)
btn6_s3 = ttk.Button(text=' ')
btn6_s3.place(x= 180, y = 60, width=30, height=30)
btn7_s3 = ttk.Button(text=' ')
btn7_s3.place(x= 210, y = 60, width=30, height=30)
# строка 4
btn_s4 = ttk.Button(text=' ')
btn_s4.place(x= 0, y = 90, width=30, height=30)
btn1_s4 = ttk.Button(text=' ')
btn1_s4.place(x= 30, y = 90, width=30, height=30)
btn2_s4 = ttk.Button(text=' ')
btn2_s4.place(x= 60, y = 90, width=30, height=30)
btn3_s4 = ttk.Button(text=' ')
btn3_s4.place(x= 90, y = 90, width=30, height=30)
btn4_s4 = ttk.Button(text=' ')
btn4_s4.place(x= 120, y = 90, width=30, height=30)
btn5_s4 = ttk.Button(text=' ')
btn5_s4.place(x= 150, y = 90, width=30, height=30)
btn6_s4 = ttk.Button(text=' ')
btn6_s4.place(x= 180, y = 90, width=30, height=30)
btn7_s4 = ttk.Button(text=' ')
btn7_s4.place(x= 210, y = 90, width=30, height=30)
# root.mainloop()
#Python_Code_Dicts
cell_stat = {#словарь по занятости клеток(если клетка открыта или ан ней флажок то True иначе False)
    0:False,
    1:False,
    2:False,
    3:False,
    4:False,
    5:False,
    6:False,
    7:False,
    8:False,
    9:False,
    10:False,
    11:False,
    12:False,
    13:False,
    14:False,
    15:False,
    16:False,
    17:False,
    18:False,
    19:False,
    20:False,
    21:False,
    22:False,
    23:False,
    24:False,
    25:False,
    26:False,
    27:False,
    28:False,
    29:False,
    30:False,
    31:False
}

cells_contact={
#первая строка:
   'btn': ['btn1', 'btn1_s2', 'btn_s2'],
   'btn1': ['btn', 'btn1_s2', 'btn_s2', 'btn2', 'btn2_s2'],
   'btn2': ['btn3', 'btn1_s2', 'btn3_s2', 'btn1', 'btn2_s2'],
   'btn3': ['btn4', 'btn4_s2', 'btn3_s2', 'btn2', 'btn2_s2'],
   'btn4': ['btn3', 'btn3_s2', 'btn4_s2', 'btn5', 'btn5_s2'],
   'btn5': ['btn4', 'btn4_s2', 'btn5_s2', 'btn6', 'btn6_s2'],
   'btn6': ['btn5', 'btn5_s2', 'btn6_s2', 'btn7', 'btn7_s2'],
   'btn7': ['btn6', 'btn6_s2', 'btn7_s2'],
#вторaя строка:
    'btn_s2': ['btn', 'btn1', 'btn1_s2', 'btn_s3', 'btn1_s3'],
    'btn1_s2': ['btn', 'btn1', 'btn2_s2', 'btn2', 'btn_s3', 'btn1_s3', 'btn2_s3', 'btn_s2'],
    'btn2_s2': ['btn1', 'btn1_s2', 'btn1_s3', 'btn2', 'btn3', 'btn3_s2', 'btn3_s3', 'btn2_s3'],
    'btn3_s2': ['btn2', 'btn2_s2', 'btn2_s3', 'btn3', 'btn3_s3', 'btn4', 'btn4_s2', 'btn4_s3'],
    'btn4_s2': ['btn3', 'btn3_s2', 'btn3_s3', 'btn4', 'btn4_s3', 'btn5', 'btn5_s2', 'btn5_s3'],
    'btn5_s2': ['btn4', 'btn4_s2', 'btn4_s3', 'btn5', 'btn5_s3', 'btn6', 'btn6_s2', 'btn6_s3'],
    'btn6_s2': ['btn5', 'btn5_s2', 'btn5_s3', 'btn6', 'btn6_s3', 'btn7', 'btn7_s2', 'btn7_s3'],
    'btn7_s2': ['btn6', 'btn6_s2', 'btn6_s3', 'btn7', 'btn7_s3'],
#третья строка
    'btn_s3': ['btn_s2', 'btn1_s2', 'btn1_s3', 'btn_s4', 'btn1_s4'],
    'btn1_s3': ['btn_s2', 'btn1_s2', 'btn2_s2', 'btn3_s3', 'btn_s3', 'btn_s4', 'btn1_s4', 'btn2_s4'],
    'btn2_s3': ['btn1_s2', 'btn2_s2', 'btn3_s2', 'btn4_s3', 'btn1_s3', 'btn1_s4', 'btn2_s4', 'btn3_s4'],
    'btn3_s3': ['btn2_s2', 'btn3_s2', 'btn4_s2', 'btn5_s3', 'btn2_s3', 'btn2_s4', 'btn3_s4', 'btn4_s4'],
    'btn4_s3': ['btn3_s2', 'btn4_s2', 'btn5_s2', 'btn6_s3', 'btn3_s3', 'btn3_s4', 'btn4_s4', 'btn5_s4'],
    'btn5_s3': ['btn4_s2', 'btn5_s2', 'btn6_s2', 'btn7_s3', 'btn4_s3', 'btn4_s4', 'btn5_s4', 'btn6_s4'],
    'btn6_s3': ['btn5_s2', 'btn6_s2', 'btn7_s2', 'btn5_s3', 'btn7_s3', 'btn5_s4', 'btn6_s4', 'btn7_s4'],
    'btn7_s3': ['btn6_s2', 'btn7_s2', 'btn6_s3', 'btn6_s4', 'btn7_s4'],
#четвёртая строка
    'btn_s4': ['btn_s3', 'btn1_s3', 'btn1_s4'],
    'btn1_s4': ['btn_s4', 'btn_s3', 'btn1_s3', 'btn2_s3', 'btn2_s4'],
    'btn2_s4': ['btn1_s4', 'btn1_s3', 'btn2_s3', 'btn3_s3', 'btn3_s4'],
    'btn3_s4': ['btn2_s4', 'btn2_s3', 'btn3_s3', 'btn4_s3', 'btn4_s4'],
    'btn4_s4': ['btn3_s4', 'btn3_s3', 'btn4_s3', 'btn5_s3', 'btn5_s4'],
    'btn5_s4': ['btn4_s4', 'btn4_s3', 'btn5_s3', 'btn6_s3', 'btn6_s4'],
    'btn6_s4': ['btn5_s4', 'btn5_s3', 'btn6_s3', 'btn7_s3', 'btn7_s4'],
    'btn7_s4': ['btn6_s4', 'btn6_s3', 'btn7_s3']
}
#Python_Code_____________________________________________________________________________
all_variants = [' ', 1, 2, 3, 4, 5, 6, 7, 8, '|"', '*']#все варианты оболочки клетки
all_btns = ['btn', 'btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6', 'btn7', 'btn_s2', 'btn1_s2', 'btn2_s2', 'btn3_s2', 'btn4_s2', 'btn5_s2', 'btn6_s2', 'btn7_s2', 'btn_s3', 'btn1_s3', 'btn2_s3', 'btn3_s3', 'btn4_s3', 'btn5_s3', 'btn6_s3', 'btn7_s3', 'btn_s4', 'btn1_s4', 'btn2_s4', 'btn3_s4', 'btn4_s4', 'btn5_s4', 'btn6_s4', 'btn7_s4']
count_int = 0#счётная переменная'
for i_b in range(1):
    rand_generation= random.randint(0, 1)#######рандоманая
    cell_stat.update({rand_generation: 'BOMB'})#генирация бомб
    d = cells_contact.get(all_btns[rand_generation])#обращаемся к клеткам занятым бомбами
    for i in d:#цикл по ктонтактирующми с бомбой клетками
        wer = cells_contact.get(i)#обращаемся к клеткам, которые контактируют с клеткой, которая контактирует с бомбой
        for iq in wer:#цикл по вышеназванным клеткам
            lisst = []
            if cell_stat.get(all_btns.index(iq)) not in lisst:
                lisst.append(cell_stat.get(all_btns.index(iq)))
                print(lisst)
            if lisst == 'BOMB':
                count_int+=1

print(wer)
print(count_int)
print(i)
print(d)

