import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")


        # Task List
        self.tasks = []

        # Create Task Entry and Button
        self.task_entry = tk.Entry(root, width=50)
        self.create_button = tk.Button(root, text="Create Task", command=self.create_task)
    
        # Update Task Entry and Button
        self.update_entry = tk.Entry(root, width=50)
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)

        # Archive Button
        self.archive_button = tk.Button(root, text="Archive Task", command=self.archive_task)

        # Place widgets on the grid
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.create_button.grid(row=0, column=1, padx=10, pady=10)
        self.update_entry.grid(row=1, column=0, padx=10, pady=10)
        self.update_button.grid(row=1, column=1, padx=10, pady=10)
        self.task_listbox.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.archive_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        # Initialize the task listbox
        self.update_task_listbox()

    def create_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.") 

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_text = self.update_entry.get()
            if task_text:
                index = selected_index[0]
                self.tasks[index] = task_text
                self.update_task_listbox()
                self.update_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        else:
            messagebox.showwarning("Warning", "Select a task to update.")


    def archive_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            archived_task = self.tasks.pop(index)
            messagebox.showinfo("Task Archived", f"Archived Task: {archived_task}")
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to archive.")               

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()