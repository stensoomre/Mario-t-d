import csv
import tkinter as tk
from tkinter import ttk, filedialog
from ttkbootstrap import Style

def open_file():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=[("CSV files", "*.csv")]
    )
    if filename:
        with open(filename, "r") as file:
            csvreader = csv.reader(file)
            l1 = next(csvreader)  # column headers as first row
            r_set = [row for row in csvreader]

            # Clear the existing treeview
            for i in trv.get_children():
                trv.delete(i)

            # Add new data to treeview
            trv["columns"] = l1
            for i in l1:
                trv.column(i, width=100, anchor="c")
                trv.heading(i, text=i)

            for dt in r_set:
                v = [r for r in dt]  # creating a list from each row
                trv.insert("", "end", iid=v[0], values=v)
# Create root window
root = tk.Tk()
root.geometry("800x600")
root.title("CSV Viewer")

# Create style object
style = Style(theme='darkly')

# Create file selection frame
file_frame = ttk.Frame(root, padding=20)
file_frame.pack(fill='x')
file_button = ttk.Button(file_frame, text="Open", command=open_file)
file_button.pack(side='left')

# Create treeview
trv_frame = ttk.Frame(root, padding=20)
trv_frame.pack(fill='both', expand=True)
trv = ttk.Treeview(trv_frame)
trv.pack(side='left', fill='both', expand=True)

# Create scrollbar
scrollbar = ttk.Scrollbar(trv_frame, orient='vertical', command=trv.yview)
scrollbar.pack(side='right', fill='y')
trv.configure(yscrollcommand=scrollbar.set)

# Start event loop
root.mainloop()
