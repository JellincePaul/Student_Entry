import tkinter
from tkinter import ttk

def getdata():
    name = name_entry.get()
    register = register_entry.get()
    standard = class_combobox.get()
    section = section_combobox.get()
    tamil = int(tamil_entry.get())
    english = int(english_entry.get())
    math = int(math_entry.get())
    science = int(science_entry.get())
    social = int(social_entry.get())
    if(tamil>100 or english>100 or math >100 or science>100 or social>100 or tamil<0 or english<0 or math<0 or science<0 or social<0):
        print("Wrong  subject mark")
        error_print.config(text="ERROR : Wrong  subject mark")
    else:
        tot = tamil + english + math + science + social
        total_label_print.config(text=tot)
        avg = tot/5
        avg_label_print.config(text=avg)
        print(name, register, standard, section)


window = tkinter.Tk()
window.title("Student Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving Student Info
student_info_frame = tkinter.LabelFrame(frame, text="Student Information")
student_info_frame.grid(row=0, column=0, padx=20, pady=10)

name_label = tkinter.Label(student_info_frame, text="Name")
name_label.grid(row=0, column=0)
register_label = tkinter.Label(student_info_frame, text="Register Number")
register_label.grid(row=0, column=1)

name_entry = tkinter.Entry(student_info_frame)
register_entry = tkinter.Entry(student_info_frame)
name_entry.grid(row=1, column=0)
register_entry.grid(row=1, column=1)

class_label = tkinter.Label(student_info_frame, text="Class")
class_combobox = ttk.Combobox(student_info_frame, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
class_label.grid(row=2, column=0)
class_combobox.grid(row=3, column=0)

section_label = tkinter.Label(student_info_frame, text="Section")
section_combobox = ttk.Combobox(student_info_frame, values=["A", "B", "C", "D"])
section_label.grid(row=2, column=1)
section_combobox.grid(row=3, column=1)

#student_mark
student_mark_frame = tkinter.LabelFrame(frame, text="Marks")
student_mark_frame.grid(row=4, column=0, padx=20, pady=10)

tamil_label = tkinter.Label(student_mark_frame, text="Tamil")
tamil_label.grid(row=1, column=0)
tamil_entry = tkinter.Entry(student_mark_frame)
tamil_entry.grid(row=1, column=1)


english_label = tkinter.Label(student_mark_frame, text="English")
english_label.grid(row=2, column=0)
english_entry=tkinter.Entry(student_mark_frame)
english_entry.grid(row=2,column=1)


math_label = tkinter.Label(student_mark_frame, text="Math")
math_label.grid(row=3, column=0)
math_entry = tkinter.Entry(student_mark_frame)
math_entry.grid(row=3, column=1)


science_label = tkinter.Label(student_mark_frame, text="Science")
science_label.grid(row=4, column=0)
science_entry=tkinter.Entry(student_mark_frame)
science_entry.grid(row=4,column=1)


social_label = tkinter.Label(student_mark_frame, text="Social")
social_label.grid(row=5, column=0)
social_entry = tkinter.Entry(student_mark_frame)
social_entry.grid(row=5, column=1)


#total and avg
totavg = tkinter.LabelFrame(frame, text="Calculation")
totavg.grid(row=6, column=0, padx=20, pady=10)

total_label = tkinter.Label(totavg, text="Total")
total_label.grid(row=7, column=0,  padx=20, pady=10)
total_label_print = tkinter.Label(totavg, text="")
total_label_print.grid(row=7, column=1,  padx=20, pady=10)

avg_label = tkinter.Label(totavg, text="Average")
avg_label.grid(row=8, column=0,  padx=20, pady=10)
avg_label_print = tkinter.Label(totavg)
avg_label_print.grid(row=8, column=1,  padx=20, pady=10)

submit = tkinter.Button(frame, text="Enter data", command=getdata)
submit.grid(row=9, column=0,  padx=20, pady=10)


error_print = tkinter.Label(frame)
error_print.grid(row=10, column=0)
def reset():
   name_entry.set("")
    #register = register_entry.get()
    #standard = class_combobox.get()
    #section = section_combobox.get()

adddata = tkinter.Button(frame, text="Add Data", command=reset)
adddata.grid(row=9, column=1, padx=20, pady=10)




window.mainloop()