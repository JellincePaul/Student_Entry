import tkinter
from tkinter import ttk

def showdata():
    tamil = int(tamil_entry.get())
    english = int(english_entry.get())
    math = int(math_entry.get())
    science = int(science_entry.get())
    social = int(social_entry.get())
    tot = tamil + english + math + science + social
    total_label_print.config(text=tot)
    avg = tot/5
    avg_label_print.config(text=avg)



window = tkinter.Tk()
window.title("Student Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving Student Info
student_info_frame = tkinter.LabelFrame(frame, text="Student Information")
student_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(student_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(student_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(student_info_frame)
last_name_entry = tkinter.Entry(student_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

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

button = tkinter.Button(frame, text="Enter data", command=showdata)
button.grid(row=9, column=0, sticky="news", padx=20, pady=10)




window.mainloop()