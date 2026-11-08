import cProfile
import tkinter as tk
from tkinter import ttk

import widgets.list_view as lv
from row_state import RowState, Severity

profiler = cProfile.Profile()

root = tk.Tk()

root.title("Tkinter")
root.geometry("600x400")
root.configure(padx=10, pady=10)

style = ttk.Style(root)
style.configure("B.TFrame", background="blue")
style.configure("Y.TFrame", background="yellow")

image = tk.PhotoImage(file="C:\\tmp\\家のアイコン素材.png")

paned_windows = ttk.PanedWindow(root, orient="horizontal")
menu_frame = ttk.Frame(paned_windows, style="Y.TFrame", padding=10)
list_view = lv.ListView(paned_windows, image)



def w_full_reload():
    profiler.enable(subcalls=False, builtins=False)
    list_view.full_reload()
    profiler.disable()
    profiler.print_stats()

def w_detach_and_reattach():
    profiler.enable(subcalls=False, builtins=False)
    list_view.detach_and_reattach()
    profiler.disable()
    profiler.print_stats()
    

ttk.Button(menu_frame, text="test data", command=list_view.insert_test_data).pack()
ttk.Button(menu_frame, text="Fullreload", command=w_full_reload).pack()
ttk.Button(menu_frame, text="De-Reatacch", command=w_detach_and_reattach).pack()
ttk.Button(menu_frame, text="kair", command=list_view.insert_test_data2).pack()
ttk.Button(menu_frame, text="Delete", command=list_view.delete_all).pack()
ttk.Button(menu_frame, text="Error test", command=list_view.insert_test_error).pack()



paned_windows.add(menu_frame)
paned_windows.add(list_view)
paned_windows.pack(expand=True, fill="both")


root.mainloop()
