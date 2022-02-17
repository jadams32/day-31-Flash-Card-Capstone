from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


def known_phrase():
    pass


def needs_study():
    pass


window = Tk()
window.title("Flash Card Study")

canvas_front = Canvas()
front_logo = PhotoImage(file="images/card_front.png")
canvas_front.create_image(200, 200, image=front_logo)
canvas_front.grid(column=1, row=1)


yes_image = PhotoImage(file="images/wrong.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=known_phrase)
yes_button.grid(column=2, row=2)

no_image = PhotoImage(file="images/right.png")
no_button = Button(image=no_image, highlightthickness=0, command=needs_study)
no_button.grid(column=0, row=2)


# TODO: Build the UI
# TODO: Build button functions "needs_study", and known_phrase
# TODO: import data from the csv
# TODO: categorize known and unknown phrases
window.mainloop()
