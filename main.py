from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


def known_phrase():
    pass


def needs_study():
    pass


window = Tk()
window.title("Flash Card Study")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas_front = Canvas(width=800, height=520, bg=BACKGROUND_COLOR, highlightthickness=0)
front_logo = PhotoImage(file="images/card_front.png")
canvas_front.create_image(405, 265, image=front_logo)
canvas_front.grid(column=0, row=0, columnspan=2)
language_title = canvas_front.create_text(400, 150, text="French", font=("ariel", 40, "italic"))
word = canvas_front.create_text(400, 263, text="Word", font=("ariel", 60, "bold"))


yes_image = PhotoImage(file="images/wrong.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=known_phrase)
yes_button.grid(column=1, row=1)

no_image = PhotoImage(file="images/right.png")
no_button = Button(image=no_image, highlightthickness=0, command=needs_study)
no_button.grid(column=0, row=1)

# TODO: Build button functions "needs_study", and known_phrase
# TODO: import data from the csv
# TODO: categorize known and unknown phrases
window.mainloop()
