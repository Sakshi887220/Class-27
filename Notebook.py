from tkinter import * 
"""
root = Tk() 
root.geometry("300x200")  
w = Label(root, text ='CodeVidhya', font = "50")  
w.pack() 
Checkbutton1 = IntVar()   
Checkbutton2 = IntVar()   
 
Button1 = Checkbutton(root, text = "Tutorial", variable = Checkbutton1, 
                      onvalue = 1,  offvalue = 0,height = 2, 
                      width = 10) 
Button2 = Checkbutton(root, text = "Student", variable = Checkbutton2, 
                      onvalue = 1, offvalue = 0, height = 2, 
                      width = 10) 

Button1.pack()   
Button2.pack()   
Button3.pack() 
  
mainloop()  
"""
# Part 2 OPtion menu
master = Tk()


def ok():
    

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
