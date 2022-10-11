from distutils.command.config import config
from tkinter import *
import tkinter.ttk as ttk
from turtle import left
import tkinter.font as font
from cdi import CDB

def get_aliquota_ir():
    selected =  str(radio.get())
    if selected == '0':
        aliquota_ir=0
    elif selected == '1':
        aliquota_ir=15
    elif selected == '2':
        aliquota_ir=17.5
    elif selected == '3':
        aliquota_ir=20
    elif selected == '4':
        aliquota_ir=22.5
    return aliquota_ir

def call_function():
    capital_value = float(capital.get())
    tx_selic_value = float(tx_selic.get())*0.01
    tx_cdi_value = float(tx_cdi.get())*0.01
    rentabilidade_value = float(rentabilidade.get())
    meses_value = float(meses.get())
    aliquota_ir_value = get_aliquota_ir()

    #CDB(capital_value, tx_cdi_value,tx_selic_value,rentabilidade_value,aliquota_ir_value,meses_value)

    root = Tk()

    frame1  = Frame(root, highlightbackground="green", highlightthickness=4,background='gainsboro')
    frame1.pack(padx=20, pady=20,side=LEFT)    
    for i in CDB(capital_value, tx_cdi_value,tx_selic_value,rentabilidade_value,aliquota_ir_value,meses_value)['first_block']:
        lab = Label(frame1, text=i,justify=LEFT, anchor='w',background='gainsboro')
        lab.pack(padx=5, pady=5)

    frame2  = Frame(root, highlightbackground="blue", highlightthickness=4,background='gainsboro')
    frame2.pack(padx=20, pady=20,side=RIGHT)    
    for i in CDB(capital_value, tx_cdi_value,tx_selic_value,rentabilidade_value,aliquota_ir_value,meses_value)['second_block']:
        lab = Label(frame2, text=i,background='gainsboro')
        lab.pack(padx=5, pady=5)

    frame3  = Frame(root, highlightbackground="red", highlightthickness=4,background='gainsboro')
    frame3.pack(padx=20, pady=20,side=BOTTOM)    
    for i in CDB(capital_value, tx_cdi_value,tx_selic_value,rentabilidade_value,aliquota_ir_value,meses_value)['third_block']:
        lab = Label(frame3, text=i, anchor='w',background='gainsboro')
        lab.pack(padx=5, pady=5)



if __name__ == '__main__':
    root = Tk()
    
    # Title

    framedisp = Frame(root,highlightbackground='SkyBlue', highlightthickness=4)
    lab = Label(framedisp,text="CDBs, LCIs e LCAs indexadas por \nCertificados de Depósitos Interbancários", anchor='w', font='Helvetica 11 bold')
    lab.configure(background='#EF6945')
    lab.pack(side = TOP)
    framedisp.pack(side=TOP)

    general_frame_0 = Frame(root,highlightbackground='black', highlightthickness=1,background='#b8b894')
    general_frame_0.pack(padx = 5 , pady = 5)

    general_frame = Frame(general_frame_0,highlightbackground='SkyBlue', highlightthickness=4,background='#F9EBB9')
    general_frame.pack(padx = 5 , pady = 5)
    # Capital
    framedisp = Frame(general_frame)
    framedisp.configure(height=20, width=20,background='#F9EBB9')    
    w = Label(framedisp, width=22,text ='Capital: $', anchor='w',background='#F9EBB9') 
    w.pack(side = LEFT)
    capital = Spinbox(framedisp, from_= 0, increment=0.01)
    capital.pack(side = RIGHT, expand = YES)
    framedisp.pack(side=TOP,  anchor="w", padx = 5 , pady = 5)
    
    # Taxa Selic
    framedisp = Frame(general_frame)
    framedisp.configure(height=20, width=20,background='#F9EBB9')    
    w = Label(framedisp, width=22,text ='Taxa Selic', anchor='w',background='#F9EBB9') 
    w.pack(side = LEFT)
    tx_selic = Spinbox(framedisp, from_= 0, to=1000,increment=0.01)
    tx_selic.pack(side = LEFT)
    text_percent = Label(framedisp, width=22,text =f'% ano', anchor='w',background='#F9EBB9') 
    text_percent.pack(side=RIGHT)
    framedisp.pack(side=TOP,  anchor="w", padx = 5 , pady = 5)
    
    # Taxa CDI
    framedisp = Frame(general_frame)
    framedisp.configure(height=20, width=20,background='#F9EBB9')    
    w = Label(framedisp, width=22,text ='Taxa CDI', anchor='w',background='#F9EBB9') 
    w.pack(side = LEFT)
    tx_cdi = Spinbox(framedisp, from_= 0,  increment=0.01)
    tx_cdi.pack(side = LEFT)
    text_percent = Label(framedisp, width=22,text =f'% ano', anchor='w',background='#F9EBB9') 
    text_percent.pack(side=RIGHT)
    framedisp.pack(side=TOP,  anchor="w", padx = 5 , pady = 5)
    
    # Rentabilidade
    framedisp = Frame(general_frame)
    framedisp.configure(height=20, width=20,background='#F9EBB9')    
    w = Label(framedisp, width=22,text ='Rentabilidade', anchor='w',background='#F9EBB9') 
    w.pack(side = LEFT)
    rentabilidade = Spinbox(framedisp, from_= 0,  increment=0.01)
    rentabilidade.pack(side = LEFT, expand = YES, fill = X)
    text_percent = Label(framedisp, width=22,text =f'% CDI', anchor='w',background='#F9EBB9') 
    text_percent.pack(side=RIGHT)
    framedisp.pack(side=TOP,  anchor="w",fill = X, padx = 5 , pady = 5)
    
    # Meses
    framedisp = Frame(general_frame)
    framedisp.configure(height=20, width=20,background='#F9EBB9')    
    w = Label(framedisp, width=22,text ='Meses', anchor='w',background='#F9EBB9') 
    w.pack(side = LEFT)
    meses = Spinbox(framedisp, from_= 0)
    meses.pack(side = LEFT)
    framedisp.pack(side=TOP,  anchor="w",fill = X, padx = 5 , pady = 5)
    
    # Alíquota IR text
    framedisp = Frame(general_frame)
    framedisp.configure(height=20, width=20,background='#F9EBB9')
    lab = Label(framedisp)
    lab.configure(text=("Alíquota IR"),background='#F9EBB9')
    lab.pack(side = LEFT)
    framedisp.pack(side=TOP,  anchor="w", padx = 5 , pady = 5)

    frame1 = Frame(general_frame)
    frame1.configure(height=200, width=200,background='#F9EBB9')
    radio = IntVar()
    radiobutton11 = Radiobutton(frame1)
    radiobutton11.configure(text=("0.0 (LCA ou LCI)"), variable=radio, value=0,background='#F9EBB9')
    radiobutton11.pack(side="top",  anchor="w", padx = 5)
    radiobutton12 = Radiobutton(frame1)
    radiobutton12.configure(text=("15.0 (acima de 721 dias)"), variable=radio, value=1,background='#F9EBB9')
    radiobutton12.pack(side="top",  anchor="w", padx = 5)
    radiobutton13 =Radiobutton(frame1)
    radiobutton13.configure(text=("17.5 (de 361 até 720 dias)"), variable=radio, value=2,background='#F9EBB9')
    radiobutton13.pack(side="top",  anchor="w", padx = 5)
    radiobutton14 = Radiobutton(frame1)
    radiobutton14.configure(text=("20.0 (de 181 até 360 dias)"), variable=radio, value=3,background='#F9EBB9')
    radiobutton14.pack(side="top",  anchor="w", padx = 5)
    radiobutton15 = Radiobutton(frame1)
    radiobutton15.configure(text=("22.5 (até 180 dias)"), variable=radio, value=4,background='#F9EBB9')
    radiobutton15.pack(side="top",  anchor="w", padx = 5)
    frame1.pack(side="top",  anchor="w", padx = 5 , pady = 5)
    
    # "Calcular" button
    b1 = Button(general_frame_0, text = 'Calcular', command=call_function,background='#F9EBB9', fg='red')
    b1.pack(side = TOP, padx = 5, pady = 5)

    # Arraste-me para reposicionar a tela
    framedisp = Frame(general_frame_0)
    framedisp.configure(height=20, width=20)
    lab = Label(framedisp)
    lab.configure(text=("(arraste-me para reposicionar a janela)"),background='#b8b894')
    lab.pack(side = TOP)
    framedisp.pack(side=TOP, padx = 5, pady = 5)

    general_frame.pack()
    root.mainloop()


