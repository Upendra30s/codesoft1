import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import Calendar

def add_task():
    task_name = entry.get()
    if task_name:
        due_date = calendar.get_date()
        days_to_complete = simpledialog.askinteger("Days to Complete", f"Enter the number of days to complete '{task_name}':", minvalue=1)
        if due_date and days_to_complete:
            task = {
                "Task": task_name,
                "Due Date": due_date,
                "Days to Complete": days_to_complete,
                "Completion Percentage": 0
            }
            tasks_list.insert(tk.END, task["Task"])
            tasks.append(task)
            entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task name.")

def update_task():
    selected_task = tasks_list.curselection()
    if selected_task:
        task_name = tasks_list.get(selected_task)
        updated_name = entry.get()
        if updated_name:
            tasks_list.delete(selected_task)
            tasks_list.insert(selected_task, updated_name)
            for task in tasks:
                if task["Task"] == task_name:
                    task["Task"] = updated_name
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task name.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def remove_task():
    selected_task = tasks_list.curselection()
    if selected_task:
        task_name = tasks_list.get(selected_task)
        task = None
        for t in tasks:
            if t["Task"] == task_name:
                task = t
                break

        if task is None:
            messagebox.showwarning("Warning", "Task not found in the list.")
        elif task_name in pending_tasks:
            pending_tasks_list.delete(pending_tasks_list.get(0, tk.END).index(task_name))
            tasks_list.delete(selected_task)
            tasks.remove(task)
            pending_tasks.remove(task_name)
            update_task_counts()
        elif task_name in completed_tasks:
            completed_tasks_list.delete(completed_tasks_list.get(0, tk.END).index(task_name))
            tasks_list.delete(selected_task)
            tasks.remove(task)
            completed_tasks.remove(task_name)
            update_task_counts()
        else:
            tasks_list.delete(selected_task)
            tasks.remove(task)
            update_task_counts()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def complete_task():
    selected_task = tasks_list.curselection()
    if selected_task:
        task_name = tasks_list.get(selected_task)
        completion = simpledialog.askinteger("Completion Percentage", f"Enter completion percentage for '{task_name}':", minvalue=0, maxvalue=100)
        if completion is not None:
            for task in tasks:
                if task["Task"] == task_name:
                    task["Completion Percentage"] = completion
                    if completion < 100:
                        if task_name not in pending_tasks:
                            pending_tasks.append(task_name)
                            pending_tasks_list.insert(tk.END, task_name)
                            messagebox.showwarning("Warning", f"'{task_name}' is now pending.")
                        if task_name in completed_tasks:
                            completed_tasks.remove(task_name)
                    else:
                        if task_name in pending_tasks:
                            pending_tasks.remove(task_name)
                            pending_tasks_list.delete(pending_tasks_list.get(0, tk.END).index(task_name))
                        if task_name not in completed_tasks:
                            completed_tasks.append(task_name)
                            completed_tasks_list.insert(tk.END, task_name)
                            messagebox.showwarning("Warning", f"'{task_name}' is now completed.")
                    update_task_counts()
            tasks_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

def update_task_counts():
    pending_label.config(text=f"Pending Tasks: {len(pending_tasks)}")
    completed_label.config(text=f"Completed Tasks: {len(completed_tasks)}")

def display_tasks(tab):
    task_list = None
    if tab == "To-Do List":
        task_list = tasks_list
    elif tab == "Completed":
        task_list = completed_tasks_list
    elif tab == "Pending":
        task_list = pending_tasks_list

    task_list.delete(0, tk.END)
    for task in tasks:
        if tab == "To-Do List":
            task_list.insert(tk.END, task["Task"])
        elif tab == "Completed" and task["Completion Percentage"] == 100:
            task_list.insert(tk.END, task["Task"])
        elif tab == "Pending" and task["Completion Percentage"] < 100:
            task_list.insert(tk.END, task["Task"])

root = tk.Tk()
root.title("To-Do List")

notebook = ttk.Notebook(root)
notebook.pack(pady=10)

to_do_tab = ttk.Frame(notebook)
completed_tab = ttk.Frame(notebook)
pending_tab = ttk.Frame(notebook)

notebook.add(to_do_tab, text="To-Do List")
notebook.add(completed_tab, text="Completed")
notebook.add(pending_tab, text="Pending")

entry = tk.Entry(to_do_tab, width=40)
entry.pack(pady=10)

tasks_list = tk.Listbox(to_do_tab, height=10, width=40)
tasks_list.pack(padx=10, pady=10)

calendar = Calendar(to_do_tab, selectmode="day", date_pattern='yyyy-mm-dd')
calendar.pack(pady=10)

add_button = tk.Button(to_do_tab, text="Add Task", command=add_task)
update_button = tk.Button(to_do_tab, text="Update Task", command=update_task)
remove_button = tk.Button(to_do_tab, text="Remove Task", command=remove_task)
complete_button = tk.Button(to_do_tab, text="Complete or Not", command=complete_task)
add_button.pack(pady=10)
update_button.pack(pady=10)
remove_button.pack(pady=10)
complete_button.pack(pady=10)

completed_tasks_list = tk.Listbox(completed_tab, height=5, width=40)
completed_tasks_list.pack(padx=10, pady=10)

pending_tasks_list = tk.Listbox(pending_tab, height=5, width=40)
pending_tasks_list.pack(padx=10, pady=10)

pending_label = tk.Label(to_do_tab, text="Pending Tasks: 0")
completed_label = tk.Label(to_do_tab, text="Completed Tasks: 0")
pending_label.pack(pady=5)
completed_label.pack(pady=5)

tasks = []
completed_tasks = []
pending_tasks = []

display_tasks("To-Do List")
display_tasks("Completed")
display_tasks("Pending")

update_task_counts()

root.mainloop()
