import tkinter

window = tkinter.Tk()
window.title("Мое первое приложение Tkinter")
window.geometry("300x200")

label = tkinter.Label(window, text="Привет, мир!")
label.pack()

window.mainloop()