import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk  # Import ThemedTk from ttkthemes

def add_task():
    task_string = task_field.get()
    category_string = category_combobox.get()

    if len(task_string) == 0 or category_string == "":
        messagebox.showinfo('Error', 'Task or category field is empty.')
    else:
        tasks.append((task_string, category_string))
        list_update()
        task_field.delete(0, 'end')
        category_combobox.set("")  # Clear the category selection
        guiWindow.after(10000, show_reminder, task_string)

def list_update():
    clear_list()
    for task, category in tasks:
        task_listbox.insert('end', f"{category}: {task}")

def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        task, category = selected_task.split(": ", 1)
        if (task, category) in tasks:
            tasks.remove((task, category))
            list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while len(tasks) != 0:
            tasks.pop()
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def show_reminder(task_string):
    messagebox.showinfo('Reminder', f"Don't forget: {task_string}")

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Simulate authentication (replace with your actual authentication logic)
    if username == "user" and password == "password":
        show_task_organizer()
    else:
        messagebox.showinfo('Login Failed', 'Invalid username or password.')

def show_task_organizer():
    login_frame.pack_forget()
    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

if __name__ == "__main__":
    # Use ThemedTk instead of Tk
    guiWindow = ThemedTk(theme="plastik")
    guiWindow.title("To-Do List Manager - No Database")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#FAEBD7")

    tasks = []

    login_frame = ttk.Frame(guiWindow, padding=(10, 10, 10, 10))  # Adjust padding
    login_frame.pack(fill="both")

    username_label = ttk.Label(login_frame, text="Username:")
    username_label.pack(pady=10)
    username_entry = ttk.Entry(login_frame)
    username_entry.pack(pady=10)

    password_label = ttk.Label(login_frame, text="Password:")
    password_label.pack(pady=10)
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.pack(pady=10)

    login_button = ttk.Button(login_frame, text="Login", command=login)
    login_button.pack(pady=10)

    header_frame = ttk.Frame(guiWindow, padding=(10, 10, 10, 10))  # Adjust padding
    functions_frame = ttk.Frame(guiWindow, padding=(10, 10, 10, 10))  # Adjust padding
    listbox_frame = ttk.Frame(guiWindow, padding=(10, 10, 10, 10))  # Adjust padding

    header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Brush Script MT", 30),
        background="#FAEBD7",
        foreground="#8B4513"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Consolas", 11, "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Consolas", 12),
        width=18,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    task_field.place(x=30, y=80)

    category_label = ttk.Label(
        functions_frame,
        text="Select Category:",
        font=("Consolas", 11, "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )
    category_label.place(x=30, y=120)

    categories = ["", "Work", "Personal", "Shopping"]  # Add more categories as needed
    category_combobox = ttk.Combobox(
        functions_frame,
        values=categories[1:],
        font=("Consolas", 11),
        width=15,
        state="readonly"
    )
    category_combobox.place(x=30, y=160)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )

    add_button.place(x=30, y=200)
    del_button.place(x=30, y=240)
    del_all_button.place(x=30, y=280)
    exit_button.place(x=30, y=320)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    guiWindow.mainloop()
