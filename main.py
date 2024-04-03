from tkinter import *
import requests


def kanye_quote():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye\'s Quotes")
window.minsize(height=600, width=400)
window.config(pady=20)
window.maxsize(height=600, width=400)
canvas = Canvas(height=400, width=400)
box_img = PhotoImage(file='background.png')
canvas.create_image(200, 200, image=box_img)
quote_text = canvas.create_text(200, 200, text='Hii!', width=300, font=('Ariel', 20, 'bold'), fill='white')
canvas.pack()

img = PhotoImage(file='kanye.png')
kanye_button = Button(image=img, command=kanye_quote)
kanye_button.pack()
window.mainloop()