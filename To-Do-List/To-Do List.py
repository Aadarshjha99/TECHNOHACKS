from tkinter import *
from tkinter import messagebox
import sqlite3 as sq


def addTask():
    word = txt_input.get()
    if len(word) == 0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        cur.execute('insert into tasks values (?)', (word,))
        listUpdate()
        txt_input.delete(0, 'end')


def listUpdate():
    clearList()
    for i in task:
        lb_tasks.insert('end', i)


def delOne():
    try:
        val = lb_tasks.get(lb_tasks.curselection())
        if val in task:
            task.remove(val)
            listUpdate()
            cur.execute('delete from tasks where title = ?', (val,))
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')


def deleteAll():
    mb = messagebox.askyesno('Delete All', 'Are you sure?')
    if mb == True:
        while(len(task) != 0):
            task.pop()
        cur.execute('delete from tasks')
        listUpdate()


def clearList():
    lb_tasks.delete(0, 'end')


def retrieveDB():
    while(len(task) != 0):
        task.pop()
    for row in cur.execute('select title from tasks'):
        task.append(row[0])



if __name__ == "__main__":

    root = Tk()
    root.configure(bg="#1B262C")
    root.title('To-Do List App')

    root.geometry("250x450")

    root.resizable(False, False)


    photo = PhotoImage(file="icon.png")
    root.iconphoto(False, photo)


    conn = sq.connect('todo.db')
    cur = conn.cursor()


    cur.execute('create table if not exists tasks (title text)')


    task = []


    lbl_title = Label(root, text='To-Do List', font=('Helvetica', 18, 'bold'), fg="#BBE1FA", bg="#1B262C")
    lbl_task_show = Label(root, text='Enter task below :',
                          font=('Helvetica', 10), fg="#BBE1FA", bg="#1B262C")
    txt_input = Entry(root, width=25, bd="2", font="18", fg="#BBE1FA", bg="#3282B8")
    lb_tasks = Listbox(root, width=24, height=10,
                       selectmode='SINGLE', relief=RIDGE, bd="4", font="14", fg="#BBE1FA", bg="#3282B8")
    btn_add_task = Button(root, text='Add task', width=20,
                          command=addTask, relief=RIDGE, fg="#BBE1FA", bg="#0F4C75")
    btn_del_one = Button(root, text='Delete', width=20,
                         relief=RIDGE, command=delOne, fg="#BBE1FA", bg="#0F4C75")
    btn_del_all = Button(root, text='Delete all', width=20,
                         relief=RIDGE, command=deleteAll, fg="#BBE1FA", bg="#0F4C75")
    btn_exit = Button(root, text='Exit', width=20, relief=RIDGE, command=exit, fg="#BBE1FA", bg="#0F4C75")
    retrieveDB()
    lbl_title.place(x=60, y=5)
    lbl_task_show.place(x=70, y=45)
    txt_input.place(x=10, y=80)
    btn_add_task.place(x=50, y=115)
    btn_del_one.place(x=50, y=145)
    btn_del_all.place(x=50, y=175)
    btn_exit.place(x=50, y=205)
    lb_tasks.place(x=12, y=240)
    root.mainloop()
    conn.commit()
    cur.close()
