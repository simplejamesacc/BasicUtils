import tkinter as tk
from tkinter import messagebox
import pickle

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Improved To-Do App")
        self.root.geometry("400x500")
        self.root.configure(bg="#f4f4f4")

        self.tasks = self._load_tasks()

        # Header
        tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"),
                 bg="#f4f4f4", fg="#333").pack(pady=10)

        # Task entry
        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=25, bd=2, relief="groove")
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", lambda event=None: self.add_task())

        # Add button
        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12),
                                    bg="#4caf50", fg="white", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task listbox with scrollbar
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(list_frame, font=("Helvetica", 14),
                                       height=15, selectmode=tk.SINGLE,
                                       bg="#fff", fg="#333", bd=2, relief="groove",
                                       yscrollcommand=scrollbar.set)
        self.task_listbox.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)

        # Action buttons
        button_frame = tk.Frame(root, bg="#f4f4f4")
        button_frame.pack(pady=10)

        self.done_button = tk.Button(button_frame, text="Mark as Done", font=("Helvetica", 12),
                                     bg="#2196f3", fg="white", command=self.mark_done)
        self.done_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(button_frame, text="Delete Task", font=("Helvetica", 12),
                                       bg="#f44336", fg="white", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=10)

        self._update_listbox()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def _load_tasks(self):
        """Loads tasks from a file if it exists."""
        try:
            with open("todo_tasks.dat", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def _save_tasks(self):
        """Saves tasks to a file."""
        with open("todo_tasks.dat", "wb") as file:
            pickle.dump(self.tasks, file)

    def _update_listbox(self):
        """Refreshes the Listbox with the current tasks."""
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            self.task_listbox.insert(tk.END, task)
            if "✔" in task:
                self.task_listbox.itemconfig(index, fg="gray", selectforeground="gray")
        self.task_listbox.selection_clear(0, tk.END)

    def add_task(self):
        """Adds a new task from the entry field."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self._update_listbox()
            self._save_tasks()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def mark_done(self):
        """Marks a selected task as done."""
        try:
            index = self.task_listbox.curselection()[0]
            if "✔" not in self.tasks[index]:
                self.tasks[index] = f"✔ {self.tasks[index]}"
            self._update_listbox()
            self._save_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def delete_task(self):
        """Deletes a selected task."""
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self._update_listbox()
            self._save_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def on_closing(self):
        """Handles the window closing event to save tasks."""
        self._save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
