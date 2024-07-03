import tkinter as tk
import sqlite3

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_task_to_db(task)

def edit_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        new_task = entry_task.get()
        if new_task:
            old_task = listbox_tasks.get(selected_task_index)
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task)
            update_task_in_db(old_task, new_task)
            entry_task.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        delete_task_from_db(task)

def save_task_to_db(task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")
    cursor.execute("INSERT INTO tasks VALUES (?)", (task,))
    conn.commit()
    conn.close()

def update_task_in_db(old_task, new_task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task=? WHERE task=?", (new_task, old_task))
    conn.commit()
    conn.close()

def delete_task_from_db(task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE task=?", (task,))
    conn.commit()
    conn.close()

# Create the main window
todolist = tk.Tk()
todolist.title("To-Do List")
todolist.minsize(width=275,height=400)
# Main Heading
to_do_list = tk.Label(text="To Do List", font=("Arial", 14, "bold"))
to_do_list.grid(row=0, column=0, padx=10, pady=10)

# Entry field for task input
entry_task = tk.Entry(todolist, width=30)
entry_task.grid(row=1, column=0, padx=10, pady=10)

# Add button
btn_add = tk.Button(todolist, text="Add Task", command=add_task)
btn_add.grid(row=2, column=0, padx=10, pady=10)

# Edit button
btn_edit = tk.Button(todolist, text="Edit Task", command=edit_task)
btn_edit.grid(row=3, column=0, padx=10, pady=10)

# Listbox to display tasks
listbox_tasks = tk.Listbox(todolist, height=10, width=40)
listbox_tasks.grid(row=4, column=0, padx=10, pady=10)

# Delete button
btn_delete = tk.Button(todolist, text="Delete Task", command=delete_task)
btn_delete.grid(row=5, column=0, padx=10, pady=10)

todolist.mainloop()
