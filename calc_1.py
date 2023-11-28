# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *
from tkinter import messagebox
import decimal
import re
# globally declare the expression variable

def eval_op(op, a, b):
  if op == 0:
    return a + b
  elif op == 1:
    return a - b
  elif op == 2:
    return a*b
  elif op == 3:
    return a/b


def calc(a,b,c,d, firs_op, second_op, third_op, q):
  a.set(a.get().lower())
  b.set(b.get().lower())
  c.set(c.get().lower())
  d.set(d.get().lower())
  ## regexp
  ## ((\d\s{0,1})|(\d{3}\s))(\d{3}\s{0,1})[\.\,]{0,1}.*
  part = re.compile('\-{0,1}(\d{0,3}\s{0,1}){1}(\d{3}\s{0,1})*([\.\,]\d*){0,1}')
  if "e" in a.get() or "e" in b.get() or "e" in c.get() or "e" in d.get() :
    messagebox.showerror("Input error", "Not valid input(exponential form)")
    return
  if not re.fullmatch(part,a.get()) and re.fullmatch(part,b.get()) and re.fullmatch(part,c.get()) and re.fullmatch(part,d.get()):
    print(re.fullmatch(part,a.get()))
    messagebox.showerror("Input error", "Not valid input(extra spaces)")
    return
  print(re.fullmatch(part,a.get()))  
  try:
    a = decimal.Decimal(a.get().replace(" ","").replace(",","."))
    b = decimal.Decimal(b.get().replace(" ","").replace(",","."))
    c = decimal.Decimal(c.get().replace(" ","").replace(",","."))
    d = decimal.Decimal(d.get().replace(" ","").replace(",","."))
  except:
    messagebox.showerror("Input error", "Not valid input(letters or symbols)")
    return
  print(a,b,c,d, firs_op.get(), second_op.get(),
        third_op.get())
  
  res = eval_op(second_op.get(), b,c)
  if firs_op.get() > second_op.get():
    res = eval_op(firs_op.get(), a,res)
    res = eval_op(third_op.get(), res, d)
  else:
    res = eval_op(third_op.get(), res, d)
    res = eval_op(firs_op.get(), a,res)  
  res = res.quantize(decimal.Decimal("1.0000000000")) 
  result.set(res)
  print(q.get())
  if q.get() == 1:
    q_result.set(res.quantize(decimal.Decimal("1")))
  elif q.get() == 0:
    tmp  = res.quantize(decimal.Decimal("1"))
    if tmp % 2 == 0:
      q_result.set(tmp)
    else:
      q_result.set(tmp+1) 
  else:
    q_result.set(res//1)
    
  print(res)
  




if __name__ == "__main__":
  gui = Tk()

  gui.configure(background="light blue")

  gui.title("Calculator lab1 Stavitskaya")

  gui.geometry("1200x400")
  
  num1 = StringVar()
  num2 = StringVar()
  num3 = StringVar()
  num4 = StringVar()

  num1.set(0)
  num2.set(0)
  num3.set(0)
  num4.set(0)
  
  # create the text entry box for
  # showing the expression .
  num1_field = Entry(gui, textvariable=num1)
  num2_field = Entry(gui, textvariable=num2)
  num3_field = Entry(gui, textvariable=num3)
  num4_field = Entry(gui, textvariable=num4)
  result = StringVar()
  q_result = StringVar()
  result.set(0)
  q_result.set(0)
  result_field = Entry(gui, textvariable=result)
  q_result_field = Entry(gui, textvariable=q_result)
  f_op_var = IntVar()
  f_op_var.set(0)
  f_op1 = Radiobutton(text='+',
                 variable=f_op_var, value=0, indicatoron=0)
  f_op2 = Radiobutton(text='-',
                 variable=f_op_var, value=1, indicatoron=0)
  f_op3 = Radiobutton(text='*',
                 variable=f_op_var, value=2, indicatoron=0)
  f_op4 = Radiobutton(text='\\',
                 variable=f_op_var, value=3, indicatoron=0)

  s_op_var = IntVar()
  s_op_var.set(0)
  s_op1 = Radiobutton(text='+',
                 variable=s_op_var, value=0, indicatoron=0)
  s_op2 = Radiobutton(text='-',
                 variable=s_op_var, value=1, indicatoron=0)
  s_op3 = Radiobutton(text='*',
                 variable=s_op_var, value=2, indicatoron=0)
  s_op4 = Radiobutton(text='\\',
                 variable=s_op_var, value=3, indicatoron=0)
  
  t_op_var = IntVar()
  t_op_var.set(0)
  t_op1 = Radiobutton(text='+',
                 variable=t_op_var, value=0, indicatoron=0)
  t_op2 = Radiobutton(text='-',
                 variable=t_op_var, value=1, indicatoron=0)
  t_op3 = Radiobutton(text='*',
                 variable=t_op_var, value=2, indicatoron=0)
  t_op4 = Radiobutton(text='\\',
                 variable=t_op_var, value=3, indicatoron=0)


  
  l1 = Label(text="(",
           font="Arial 32")
 
  l2 = Label(text=")",
           font=("Arial",
                 24, "bold")) 

  l3 = Label(text="Ставицкая Ксения Андреевна 3 курс 12 группа 2023",
           font=("Times New Roman",
                 28, "bold")) 


  q_var = IntVar()
  q_var.set(0)
  q_op1 = Radiobutton(text='Бухгалтерское',
                 variable=q_var, value=0, indicatoron=0)
  q_op2 = Radiobutton(text='Математическое',
                 variable=q_var, value=1, indicatoron=0)
  q_op3 = Radiobutton(text='Усечение',
                 variable=q_var, value=2, indicatoron=0)
  
  equal = Button(gui, text=' = ', fg='grey', bg='pink',
        command=lambda:calc(num1,num2,num3,num4,f_op_var,s_op_var,t_op_var,q_var), height=1, width=7)
  
  


  num1_field.grid(row = 0, rowspan = 4, column = 0)
  f_op1.grid(row=0, column = 1)
  f_op2.grid(row=1, column = 1)
  f_op3.grid(row=2, column = 1)
  f_op4.grid(row=3, column = 1)
  l1.grid(row = 0, rowspan = 4,column =2 )
  num2_field.grid(row = 0,rowspan = 4, column = 3)
  s_op1.grid(row=0, column = 4)
  s_op2.grid(row=1, column = 4)
  s_op3.grid(row=2, column = 4)
  s_op4.grid(row=3, column = 4)
  num3_field.grid(row = 0, rowspan = 4,column = 5)
  l2.grid(row = 0,rowspan = 4 ,column = 6)
  t_op1.grid(row=0, column = 7)
  t_op2.grid(row=1, column = 7)
  t_op3.grid(row=2, column = 7)
  t_op4.grid(row=3, column = 7)
  num4_field.grid(row = 0,rowspan = 4, column = 8)
  result_field.grid(row = 0,rowspan = 4, column = 10)  
  equal.grid(row=0, rowspan = 4, column=9)

  q_op1.grid(row = 5, column = 0)
  q_op2.grid(row = 6, column = 0)
  q_op3.grid(row = 7, column = 0)
  q_result_field.grid(row = 6, rowspan = 3, column=1, columnspan=4)

  l3.grid(row=9, column = 0, columnspan=10)
  # start the GUI
  gui.mainloop()
