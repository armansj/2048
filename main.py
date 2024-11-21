import random
from tkinter import *

lst = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, ""]

root = Tk()
root.title("2048 Game")
root.geometry("400x400")

buttons = []


def change_button_with_cursor(event=None):
    clicked_button = event.widget
    label = clicked_button["text"]

    for btn in buttons:
        if btn != clicked_button and btn["text"] == label:

            x1, y1 = clicked_button.winfo_x(), clicked_button.winfo_y()
            x2, y2 = btn.winfo_x(), btn.winfo_y()


            new_x = (x1 + x2) // 2
            new_y = (y1 + y2) // 2


            clicked_button.place(x=new_x, y=new_y)
            btn.place(x=new_x, y=new_y)
            return


    x = random.randint(0, 300)
    y = random.randint(0, 300)
    clicked_button.place(x=x, y=y)


for i in range(1, 5):
    for j in range(1, 5):
        l = random.choice(lst)
        btn = Button(root, text=f"{l}", width=5, height=2)
        buttons.append(btn)
        btn.place(x=50 * j, y=50 * i)
        btn.bind("<Button-1>", change_button_with_cursor)

root.mainloop()
