print("Hello, Omantel DevSecops Foundations Class!")


#!/usr/bin/env python3
"""
To-Do List App with a GUI — single file, uses only the standard library (tkinter).
Tasks are saved to tasks.json in the same folder so they persist between runs.
"""
 
import json
import os
import tkinter as tk
from tkinter import font as tkfont
 
TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")
 
 
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []
 
 
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
 
 
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("420x520")
        self.root.configure(bg="#f4f4f5")
 
        self.tasks = load_tasks()
 
        self.strike_font = tkfont.Font(family="Helvetica", size=12, overstrike=1)
        self.normal_font = tkfont.Font(family="Helvetica", size=12, overstrike=0)
 
        # --- Input row ---
        input_frame = tk.Frame(root, bg="#f4f4f5", pady=12, padx=12)
        input_frame.pack(fill="x")
 
        self.entry = tk.Entry(input_frame, font=self.normal_font)
        self.entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.entry.bind("<Return>", lambda e: self.add_task())
 
        add_btn = tk.Button(input_frame, text="Add", command=self.add_task,
                             bg="#4f46e5", fg="white", relief="flat", padx=14)
        add_btn.pack(side="left", padx=(8, 0))
 
        # --- Task list (scrollable) ---
        list_container = tk.Frame(root, bg="#f4f4f5")
        list_container.pack(fill="both", expand=True, padx=12)
 
        canvas = tk.Canvas(list_container, bg="#f4f4f5", highlightthickness=0)
        scrollbar = tk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
        self.list_frame = tk.Frame(canvas, bg="#f4f4f5")
 
        self.list_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.list_frame, anchor="nw", width=380)
        canvas.configure(yscrollcommand=scrollbar.set)
 
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
 
        # --- Footer ---
        footer = tk.Label(root, text="", bg="#f4f4f5", fg="#71717a", font=("Helvetica", 10))
        footer.pack(pady=(0, 10))
        self.footer = footer
 
        self.render_tasks()
 
    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.tasks.append({"text": text, "done": False})
        save_tasks(self.tasks)
        self.entry.delete(0, tk.END)
        self.render_tasks()
 
    def toggle_task(self, index):
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        save_tasks(self.tasks)
        self.render_tasks()
 
    def remove_task(self, index):
        self.tasks.pop(index)
        save_tasks(self.tasks)
        self.render_tasks()
 
    def render_tasks(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
 
        if not self.tasks:
            tk.Label(self.list_frame, text="No tasks yet — add one above.",
                     bg="#f4f4f5", fg="#a1a1aa", font=("Helvetica", 11)).pack(pady=20)
        else:
            for i, task in enumerate(self.tasks):
                row = tk.Frame(self.list_frame, bg="white", pady=8, padx=10)
                row.pack(fill="x", pady=4)
 
                var = tk.BooleanVar(value=task["done"])
                cb = tk.Checkbutton(
                    row, variable=var, bg="white",
                    command=lambda i=i: self.toggle_task(i)
                )
                cb.pack(side="left")
 
                label_font = self.strike_font if task["done"] else self.normal_font
                label_fg = "#a1a1aa" if task["done"] else "#18181b"
                lbl = tk.Label(row, text=task["text"], bg="white", fg=label_fg,
                                font=label_font, anchor="w", justify="left", wraplength=260)
                lbl.pack(side="left", fill="x", expand=True, padx=(6, 0))
 
                del_btn = tk.Button(row, text="✕", command=lambda i=i: self.remove_task(i),
                                     bg="white", fg="#ef4444", relief="flat", bd=0,
                                     font=("Helvetica", 11))
                del_btn.pack(side="right")
 
        remaining = sum(1 for t in self.tasks if not t["done"])
        self.footer.config(text=f"{remaining} task(s) remaining")
 
 
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
