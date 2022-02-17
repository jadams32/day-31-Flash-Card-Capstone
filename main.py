from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
word_data_dict = data.to_dict(orient="records")

# ------------------------ Functions ---------------------- #
def word_gen():
    random_word = random.choice(word_data_dict)
    canvas.itemconfig(language_title, text=f'French')
    canvas.itemconfig(word, text=f'{random_word["French"]}')


def known_phrase():
    pass


def needs_study():
    pass

# ---------------------------- UI --------------------------- #
window = Tk()
window.title("Flash Card Study")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=520, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
language_title = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))

# ------------------------ Buttons ------------------------- #
yes_image = PhotoImage(file="images/wrong.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=word_gen)
yes_button.grid(column=0, row=1)

no_image = PhotoImage(file="images/right.png")
no_button = Button(image=no_image, highlightthickness=0, command=word_gen)
no_button.grid(column=1, row=1)

# TODO: Build button functions "needs_study", and known_phrase
# TODO: categorize known and unknown phrases
# TODO: Flip card after some time, then wait for user input
word_gen()
window.mainloop()
