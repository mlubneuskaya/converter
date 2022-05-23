import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def make_gui(currencies):
    window = tk.Tk()
    window.geometry("500x100")
    window.minsize(500, 100)
    window.maxsize(500, 100)
    frame = tk.Frame(window)
    frame.pack()
    tk.Label(frame, text="waluta źródłowa").grid(row=0, column=0)
    source_box = ttk.Combobox(frame, values=list(currencies.keys()), state='readonly')
    source_box.grid(row=1, column=0)
    source_text = tk.Entry(frame, width=10)
    source_text.grid(row=2, column=0)
    tk.Label(frame, text="waluta docelowa").grid(row=0, column=2)
    target_box = ttk.Combobox(frame, values=list(currencies.keys()), state='readonly')
    target_box.grid(row=1, column=2)
    target_text = tk.Entry(frame, width=10, state='disabled')
    target_text.grid(row=2, column=2)
    calculate_button = tk.Button(frame, text='oblicz', command=lambda: calculate(currencies, source_box, source_text,
                                                                                 target_box, target_text))
    calculate_button.grid(row=3, column=1)
    window.mainloop()


def calculate(currencies, source_box, source_text, target_box, target_text):
    source_currency = source_box.get()
    target_currency = target_box.get()
    source_value = source_text.get()
    if source_currency == "" or target_currency == "" or source_value == '':
        messagebox.showerror(title="błąd", message='wypełnij wszystkie pola')
        return
    if not source_value.isdigit():
        messagebox.showerror(title="błąd", message='niepoprawna liczba')
        return
    source_value = eval(source_value)
    result = round(source_value * currencies[source_currency] / currencies[target_currency], 4)
    target_text.configure(state='normal')
    target_text.delete(0, 'end')
    target_text.insert(0, string=str(result))
    target_text.configure(state='disabled')
