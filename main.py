from tkinter import *
from backend import Database

database=Database("books.db")


def get_selected_row(event):

    global selected_id
    if list1.size() != 0:
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        selected_id=selected_tuple[0]
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END,selected_tuple[4])


def view_command():
    list1.delete(0,END)
    for record in database.view():
        list1.insert(END,record)


def search_command():
    list1.delete(0,END)
    for record in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,record)


def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()
    list1.selection_set(END)


def delete_command():
    database.delete(selected_id)
    view_command()


def update_command():
    database.update(selected_id,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()


window=Tk()
window.geometry('400x100')
window.wm_title("Book Store")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=3)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=4)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=4)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=4)

b2=Button(window,text="Search Entry",width=12, command=search_command)
b2.grid(row=3,column=4)

b3=Button(window,text="Add Entry",width=12, command=add_command)
b3.grid(row=4,column=4)

b4=Button(window,text="Update Selected",width=12, command=update_command)
b4.grid(row=5,column=4)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=4)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=4)

window.mainloop()
