from tkinter import *
import tkinter.ttk as ttk
from turtle import left
fields = ('Capital', 'Taxa Selic', 'Taxa CDI', 'Rentabilidade', 'Meses')
def monthly_payment(entries):
   # period rate:
   #r = (float(entries['Annual Rate'].get()) / 100) / 12
   #print("r", r)
   # principal loan:
   #loan = float(entries['Loan Principle'].get())
   #n = float(entries['Number of Payments'].get())
   #remaining_loan = float(entries['Remaining Loan'].get())
   #q = (1 + r)** n
   #monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
   #monthly = ("%8.2f" % monthly).strip()
   #entries['Monthly Payment'].delete(0,END)
   #entries['Monthly Payment'].insert(0, monthly )
   #print("Monthly Payment: %f" % float(monthly))
    return None

def final_balance(entries):
   # period rate:
   #r = (float(entries['Annual Rate'].get()) / 100) / 12
   #print("r", r)
   # principal loan:
   #loan = float(entries['Loan Principle'].get())
   #n = float(entries['Number of Payments'].get())
   #q = (1 + r)** n
   #monthly = float(entries['Monthly Payment'].get())
   #q = (1 + r)** n
   #remaining = q * loan - ( (q - 1) / r) * monthly
   #remaining = ("%8.2f" % remaining).strip()
   #entries['Remaining Loan'].delete(0,END)
   #entries['Remaining Loan'].insert(0, remaining )
   #print("Remaining Loan: %f" % float(remaining))
    return None

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0,"0")
        row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
        lab.pack(side = LEFT)
        ent.pack(side = RIGHT, expand = YES, fill = X)
        entries[field] = ent
    return entries

def selection():
   selected = "You have selected " + str(radio.get())
   label.config(text=selected)

if __name__ == '__main__':
    root = Tk()
    lab = Label(text="CDBs, LCIs e LCAs indexadas por \nCertificados de Depósitos Interbancários", anchor='w')
    lab.pack(side = TOP)
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e = ents: fetch(e)))

    framedisp = Frame(root)
    framedisp.configure(height=20, width=20)
    lab = Label(framedisp)
    lab.configure(text=("Alíquota IR"))
    lab.pack(side = LEFT)
    framedisp.pack(side=TOP,  anchor="w")
    
    frame1 = Frame(None)
    frame1.configure(height=200, width=200)
    
    radio = IntVar()
    radiobutton11 = Radiobutton(frame1)
    radiobutton11.configure(text=("0.0 (LCA ou LCI)"), variable=radio, value=0, command=selection)
    radiobutton11.pack(side="top",  anchor="w")
    radiobutton12 = Radiobutton(frame1)
    radiobutton12.configure(text=("15.0 (acima de 721 dias)"), variable=radio, value=1, command=selection)
    radiobutton12.pack(side="top",  anchor="w")
    radiobutton13 =Radiobutton(frame1)
    radiobutton13.configure(text=("17.5 (de 361 até 720 dias)"), variable=radio, value=2, command=selection)
    radiobutton13.pack(side="top",  anchor="w")
    radiobutton14 = Radiobutton(frame1)
    radiobutton14.configure(text=("20.0 (de 181 até 360 dias)"), variable=radio, value=3, command=selection)
    radiobutton14.pack(side="top",  anchor="w")
    radiobutton15 = Radiobutton(frame1)
    radiobutton15.configure(text=("22.5 (até 180 dias)"), variable=radio, value=4, command=selection)
    radiobutton15.pack(side="top",  anchor="w")
    frame1.pack(side="top",  anchor="w")
    b1 = Button(root, text = 'Calcular',
        command=(lambda e = ents: final_balance(e)))
    b1.pack(side = TOP, padx = 5, pady = 5)


    root.mainloop()


