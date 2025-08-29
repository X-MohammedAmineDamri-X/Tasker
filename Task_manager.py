import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os
from datetime import datetime

class ModernTaskManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("✨ DAMRI TASKER")
        self.root.geometry("1400x900")
        self.root.configure(bg='#f0f2f5')
        
        # Variables
        self.tasks = []
        self.task_id = 1
        self.save_folder = r"C:\Users\mdamri\Desktop\PYTHON_2025\tasker\tasks"
        
        # Ensure folder exists
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
        
        # Colors and styles
        self.colors = {
            'primary': '#4A90E2',
            'secondary': '#7ED321',
            'danger': '#D0021B',
            'warning': '#F5A623',
            'dark': '#2C3E50',
            'light': '#ECF0F1',
            'white': '#FFFFFF',
            'gray': '#BDC3C7',
            'success': '#27AE60',
            'background': '#f0f2f5',
            'card': '#FFFFFF',
            'shadow': '#E8EAED'
        }
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        # Configure ttk styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Custom button styles
        self.style.configure('Primary.TButton',
                           background=self.colors['primary'],
                           foreground='white',
                           borderwidth=0,
                           focuscolor='none',
                           relief='flat',
                           padding=(20, 10))
        
        self.style.configure('Success.TButton',
                           background=self.colors['success'],
                           foreground='white',
                           borderwidth=0,
                           focuscolor='none',
                           relief='flat',
                           padding=(20, 10))
        
        self.style.configure('Danger.TButton',
                           background=self.colors['danger'],
                           foreground='white',
                           borderwidth=0,
                           focuscolor='none',
                           relief='flat',
                           padding=(15, 8))
        
        # Combobox style
        self.style.configure('Modern.TCombobox',
                           fieldbackground=self.colors['white'],
                           background=self.colors['white'],
                           borderwidth=1,
                           relief='solid')
    
    def create_widgets(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Content area with two columns
        content_frame = tk.Frame(main_container, bg=self.colors['background'])
        content_frame.pack(fill='both', expand=True, pady=20)
        
        # Left column - Input form
        self.create_input_section(content_frame)
        
        # Right column - Task list
        self.create_task_list_section(content_frame)
    
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.colors['primary'], height=80)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, 
                              text="🚀 DAMRI TASKER", 
                              font=('Helvetica', 24, 'bold'),
                              bg=self.colors['primary'],
                              fg='white')
        title_label.pack(side='left', padx=30, pady=20)
        
        # Stats
        stats_frame = tk.Frame(header_frame, bg=self.colors['primary'])
        stats_frame.pack(side='right', padx=30, pady=15)
        
        self.total_tasks_label = tk.Label(stats_frame,
                                         text="Total: 0",
                                         font=('Helvetica', 12, 'bold'),
                                         bg=self.colors['primary'],
                                         fg='white')
        self.total_tasks_label.pack(side='right', padx=10)
    
    def create_input_section(self, parent):
        # Left column frame
        left_frame = tk.Frame(parent, bg=self.colors['card'], relief='solid', bd=1)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Card header
        card_header = tk.Frame(left_frame, bg=self.colors['primary'], height=50)
        card_header.pack(fill='x')
        card_header.pack_propagate(False)
        
        header_label = tk.Label(card_header,
                               text="➕ Ajouter une nouvelle tâche",
                               font=('Helvetica', 14, 'bold'),
                               bg=self.colors['primary'],
                               fg='white')
        header_label.pack(pady=15)
        
        # Form content
        form_frame = tk.Frame(left_frame, bg=self.colors['card'])
        form_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Module Name
        tk.Label(form_frame, 
                text="📁 Nom du Module", 
                font=('Helvetica', 12, 'bold'),
                bg=self.colors['card'],
                fg=self.colors['dark']).pack(anchor='w', pady=(0, 5))
        
        self.module_entry = tk.Entry(form_frame,
                                   font=('Helvetica', 11),
                                   relief='solid',
                                   bd=1,
                                   bg=self.colors['white'])
        self.module_entry.pack(fill='x', pady=(0, 20), ipady=8)
        
        # Task Description
        tk.Label(form_frame, 
                text="📝 Description de la tâche", 
                font=('Helvetica', 12, 'bold'),
                bg=self.colors['card'],
                fg=self.colors['dark']).pack(anchor='w', pady=(0, 5))
        
        self.task_text = tk.Text(form_frame,
                               height=4,
                               font=('Helvetica', 11),
                               relief='solid',
                               bd=1,
                               bg=self.colors['white'],
                               wrap=tk.WORD)
        self.task_text.pack(fill='x', pady=(0, 20))
        
        # Status
        tk.Label(form_frame, 
                text="⚡ Statut", 
                font=('Helvetica', 12, 'bold'),
                bg=self.colors['card'],
                fg=self.colors['dark']).pack(anchor='w', pady=(0, 5))
        
        self.status_var = tk.StringVar(value="Pending")
        status_combo = ttk.Combobox(form_frame,
                                  textvariable=self.status_var,
                                  values=["Done", "Pending", "Rejected", "No Responsible Yet"],
                                  state="readonly",
                                  font=('Helvetica', 11),
                                  style='Modern.TCombobox')
        status_combo.pack(fill='x', pady=(0, 30), ipady=5)
        
        # Buttons
        buttons_frame = tk.Frame(form_frame, bg=self.colors['card'])
        buttons_frame.pack(fill='x', pady=10)
        
        add_btn = ttk.Button(buttons_frame,
                           text="➕ Ajouter la tâche",
                           command=self.add_task,
                           style='Primary.TButton')
        add_btn.pack(fill='x', pady=5)
        
        export_btn = ttk.Button(buttons_frame,
                              text="💾 Exporter vers CSV",
                              command=self.export_to_csv,
                              style='Success.TButton')
        export_btn.pack(fill='x', pady=5)
        
        quit_btn = ttk.Button(buttons_frame,
                            text="❌ Quitter",
                            command=self.quit_app,
                            style='Danger.TButton')
        quit_btn.pack(fill='x', pady=5)
    
    def create_task_list_section(self, parent):
        # Right column frame
        right_frame = tk.Frame(parent, bg=self.colors['card'], relief='solid', bd=1)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Card header
        card_header = tk.Frame(right_frame, bg=self.colors['secondary'], height=50)
        card_header.pack(fill='x')
        card_header.pack_propagate(False)
        
        header_label = tk.Label(card_header,
                               text="📋 Liste des tâches",
                               font=('Helvetica', 14, 'bold'),
                               bg=self.colors['secondary'],
                               fg='white')
        header_label.pack(pady=15)
        
        # Scrollable task list
        list_container = tk.Frame(right_frame, bg=self.colors['card'])
        list_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_container)
        scrollbar.pack(side='right', fill='y')
        
        # Canvas for scrolling
        self.canvas = tk.Canvas(list_container,
                               bg=self.colors['card'],
                               highlightthickness=0,
                               yscrollcommand=scrollbar.set)
        self.canvas.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.canvas.yview)
        
        # Frame inside canvas
        self.task_list_frame = tk.Frame(self.canvas, bg=self.colors['card'])
        self.canvas_window = self.canvas.create_window(0, 0, anchor='nw', window=self.task_list_frame)
        
        # Bind canvas resize
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        self.task_list_frame.bind('<Configure>', self._on_frame_configure)
    
    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)
    
    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def add_task(self):
        module_name = self.module_entry.get().strip()
        task_description = self.task_text.get("1.0", tk.END).strip()
        status = self.status_var.get()
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        if module_name and task_description and status:
            task_id_str = f"{module_name}-task-{str(self.task_id).zfill(4)}"
            self.tasks.append({
                "ID": task_id_str,
                "Task": task_description,
                "Status": status,
                "Date": current_date
            })
            self.task_id += 1
            self.update_task_list()
            self.clear_inputs()
        else:
            messagebox.showwarning("Erreur de saisie", "Veuillez remplir tous les champs.")
    
    def clear_inputs(self):
        self.module_entry.delete(0, tk.END)
        self.task_text.delete("1.0", tk.END)
        self.status_var.set("Pending")
    
    def update_task_list(self):
        # Clear existing widgets
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        
        # Update stats
        self.total_tasks_label.config(text=f"Total: {len(self.tasks)}")
        
        if not self.tasks:
            no_tasks_label = tk.Label(self.task_list_frame,
                                    text="🤔 Aucune tâche pour le moment\nAjoutez votre première tâche !",
                                    font=('Helvetica', 12),
                                    bg=self.colors['card'],
                                    fg=self.colors['gray'],
                                    justify='center')
            no_tasks_label.pack(pady=50)
            return
        
        # Create task cards
        for i, task in enumerate(self.tasks):
            self.create_task_card(task, i)
    
    def create_task_card(self, task, index):
        # Status colors
        status_colors = {
            'Done': self.colors['success'],
            'Pending': self.colors['warning'],
            'Rejected': self.colors['danger'],
            'No Responsible Yet': self.colors['gray']
        }
        
        # Main card frame
        card_frame = tk.Frame(self.task_list_frame, 
                            bg=self.colors['white'],
                            relief='solid',
                            bd=1)
        card_frame.pack(fill='x', pady=5, padx=10)
        
        # Left border for status
        status_border = tk.Frame(card_frame,
                               bg=status_colors.get(task['Status'], self.colors['gray']),
                               width=4)
        status_border.pack(side='left', fill='y')
        
        # Content frame
        content_frame = tk.Frame(card_frame, bg=self.colors['white'])
        content_frame.pack(side='left', fill='both', expand=True, padx=15, pady=10)
        
        # Header with ID and date
        header_frame = tk.Frame(content_frame, bg=self.colors['white'])
        header_frame.pack(fill='x', pady=(0, 5))
        
        id_label = tk.Label(header_frame,
                          text=f"🆔 {task['ID']}",
                          font=('Helvetica', 10, 'bold'),
                          bg=self.colors['white'],
                          fg=self.colors['primary'])
        id_label.pack(side='left')
        
        date_label = tk.Label(header_frame,
                            text=f"📅 {task['Date']}",
                            font=('Helvetica', 9),
                            bg=self.colors['white'],
                            fg=self.colors['gray'])
        date_label.pack(side='right')
        
        # Task description
        task_label = tk.Label(content_frame,
                            text=task['Task'],
                            font=('Helvetica', 11),
                            bg=self.colors['white'],
                            fg=self.colors['dark'],
                            wraplength=400,
                            justify='left')
        task_label.pack(anchor='w', pady=(0, 5))
        
        # Status badge
        status_frame = tk.Frame(content_frame, bg=self.colors['white'])
        status_frame.pack(fill='x')
        
        status_label = tk.Label(status_frame,
                              text=task['Status'],
                              font=('Helvetica', 9, 'bold'),
                              bg=status_colors.get(task['Status'], self.colors['gray']),
                              fg='white',
                              padx=8,
                              pady=2)
        status_label.pack(side='left')
        
        # Delete button
        delete_btn = ttk.Button(card_frame,
                              text="🗑️",
                              command=lambda t=task: self.delete_task(t),
                              style='Danger.TButton',
                              width=3)
        delete_btn.pack(side='right', padx=10)
    
    def delete_task(self, task):
        if messagebox.askyesno("Confirmer la suppression", 
                              f"Êtes-vous sûr de vouloir supprimer cette tâche ?\n\n{task['ID']}"):
            self.tasks.remove(task)
            self.update_task_list()
    
    def export_to_csv(self):
        if self.tasks:
            existing_files = [f for f in os.listdir(self.save_folder) if f.startswith("tasks")]
            file_count = len(existing_files) + 1
            file_name = f"tasks_{file_count}.csv"
            file_path = os.path.join(self.save_folder, file_name)
            
            try:
                df = pd.DataFrame(self.tasks)
                df.to_csv(file_path, index=False)
                messagebox.showinfo("Export réussi", 
                                  f"✅ Les tâches ont été exportées avec succès !\n\nFichier: {file_path}")
                
                # Clear tasks after saving
                self.tasks.clear()
                self.update_task_list()
            except Exception as e:
                messagebox.showerror("Erreur d'export", 
                                   f"❌ Erreur lors de l'export:\n{str(e)}")
        else:
            messagebox.showwarning("Aucune tâche", 
                                 "🤷‍♂️ Aucune tâche à exporter.")
    
    def quit_app(self):
        if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter ?"):
            self.root.quit()
    
    def run(self):
        self.root.mainloop()

# Launch the application
if __name__ == "__main__":
    app = ModernTaskManager()
    app.run()