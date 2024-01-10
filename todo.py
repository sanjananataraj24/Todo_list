import tkinter as tk

class ToDoListApp:
    def _init_(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("400x300")

        self.tasks = []  # List to store task information (text, checkbox, delete button)
        self.task_frame = tk.Frame(self.master)
        self.task_frame.pack(expand=True, fill=tk.BOTH)

        self.task_input = tk.Entry(self.master, font=('Arial', 12))
        self.task_input.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        add_button = tk.Button(self.master, text="Add Task", command=self.add_task, font=('Times New Roman', 12))
        add_button.pack(side=tk.RIGHT)

    def add_task(self):
        task_text = self.task_input.get().strip()
        if task_text:
            task_frame = tk.Frame(self.task_frame)

            checkbox = tk.Checkbutton(task_frame)
            checkbox.pack(side=tk.LEFT)

            task_label = tk.Label(task_frame, text=f"{task_text}", font=('Times New Roman', 12))
            task_label.pack(side=tk.LEFT, fill=tk.BOTH)

            delete_button = tk.Button(task_frame, text="Delete", command=lambda: self.delete_task(task_frame))
            delete_button.pack(side=tk.RIGHT)

            task_frame.pack(expand=True, fill=tk.BOTH)

            self.tasks.append({
                'text': task_text,
                'checkbox': checkbox,
                'label': task_label,
                'delete_button': delete_button,
                'frame': task_frame
            })

            self.task_input.delete(0, tk.END)

    def delete_task(self, task_frame):
        for task in self.tasks:
            if task['frame'] == task_frame:
                task['frame'].destroy()
                self.tasks.remove(task)
                break

if _name_ == "_main_":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()