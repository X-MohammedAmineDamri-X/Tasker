import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from datetime import datetime

root = tk.Tk()
root.title("Task Manager")

root.geometry("1920x1080")
root.attributes('-fullscreen', True)

tasks = []
task_id = 1
save_folder = r"C:\Users\mdamri\Desktop\PYTHON_2025\tasker\tasks"

# Ensure the 'tasks' folder exists
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

def add_task():
    global task_id
    module_name = module_input.get().strip()  # Get the module name
    task_name = task_input.get("1.0", tk.END).strip()  # Get the task name
    status = status_var.get()  # Get the status
    current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date
    
    if module_name and task_name and status:
        task_id_str = f"{module_name}-task-{str(task_id).zfill(4)}"
        tasks.append({"ID": task_id_str, "Task": task_name, "Status": status, "Date": current_date})
        task_id += 1
        update_task_list()
        task_input.delete("1.0", tk.END)  # Clear the input field
        module_input.delete(0, tk.END)  # Clear the input field
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def update_task_list():
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    for task in tasks:
        task_frame = tk.Frame(task_list_frame)
        task_frame.pack(pady=5, fill="x")

        task_label = tk.Label(task_frame, text=f"{task['ID']} - {task['Task']} - {task['Status']} - {task['Date']}", font=("Arial", 12))
        task_label.pack(side="left", padx=10)

        delete_button = tk.Button(task_frame, text="Delete", command=lambda t=task: delete_task(t))
        delete_button.pack(side="right", padx=10)

def delete_task(task):
    tasks.remove(task)  # Remove task from the list
    update_task_list()  # Refresh the UI to reflect the changes

def export_to_csv():
    if tasks:
        # Check existing files and create a unique filename
        existing_files = [f for f in os.listdir(save_folder) if f.startswith("tasks")]
        file_count = len(existing_files) + 1
        file_name = f"tasks_{file_count}.csv"
        file_path = os.path.join(save_folder, file_name)
        
        print(f"Saving CSV file to: {file_path}")
        
        # Create DataFrame and write to CSV
        df = pd.DataFrame(tasks)
        
        try:
            # Save to CSV using default comma separator
            df.to_csv(file_path, index=False)  # Default comma separator
            root.update()
            messagebox.showinfo("Export Successful", f"L'achghal t3addo l'CSV fi {file_path}")
            
            # Clear tasks after saving
            tasks.clear()
            update_task_list()  # Refresh the task list UI
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Export Failed", "Kayn mouchkil f t7fiz l'CSV.")
    else:
        messagebox.showwarning("No Tasks", "Ma kaynach l'achghal bach tsift.")

def quit_app():
    root.quit()

# Module Name Input with Placeholder
def on_module_input_click(event):
    if module_input.get() == "Enter Module Name":
        module_input.delete(0, tk.END)
        module_input.config(fg='black')

def on_module_input_focusout(event):
    if module_input.get() == "":
        module_input.insert(0, "Enter Module Name")
        module_input.config(fg='gray')

module_input_label = tk.Label(root, text="Module Name:", font=("Arial", 12))
module_input_label.pack(pady=5)
module_input = tk.Entry(root, width=40, font=("Arial", 12), fg='gray')
module_input.insert(0, "Enter Module Name")  # Placeholder text
module_input.bind("<FocusIn>", on_module_input_click)
module_input.bind("<FocusOut>", on_module_input_focusout)
module_input.pack(pady=10)

# Task Input Field with Placeholder
def on_task_input_click(event):
    if task_input.get("1.0", "end-1c") == "Enter Task Description":
        task_input.delete("1.0", "end-1c")
        task_input.config(fg='black')

def on_task_input_focusout(event):
    if task_input.get("1.0", "end-1c") == "":
        task_input.insert("1.0", "Enter Task Description")
        task_input.config(fg='gray')

task_input_label = tk.Label(root, text="Task Description:", font=("Arial", 12))
task_input_label.pack(pady=5)
task_input = tk.Text(root, width=60, height=4, font=("Arial", 12), wrap=tk.WORD, fg='gray')
task_input.insert("1.0", "Enter Task Description")  # Placeholder text
task_input.bind("<FocusIn>", on_task_input_click)
task_input.bind("<FocusOut>", on_task_input_focusout)
task_input.pack(pady=20, padx=20, expand=True)

# Status Dropdown
status_label = tk.Label(root, text="Status:", font=("Arial", 12))
status_label.pack(pady=5)
status_var = tk.StringVar(value="Pending")
status_menu = tk.OptionMenu(root, status_var, "Done", "Pending", "Rejected", "No Responsible Yet")
status_menu.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12), height=2)
add_button.pack(pady=10)

export_button = tk.Button(root, text="Export to CSV", command=export_to_csv, font=("Arial", 12), height=2)
export_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_app, font=("Arial", 12), height=2)
quit_button.pack(pady=10)

# Task List Frame
task_list_frame = tk.Frame(root)
task_list_frame.pack(pady=10, padx=20, expand=True, fill="both")

root.mainloop()
