from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

window = Tk()

window.title("Image Watermarking")
window.config(padx=50, pady=50)


def add_watermark():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(
                                              ("jpeg files", "*.jpg"), ("png files", "*.png"), ("gif files", "*.gif"),
                                              ("other files", "*.*")))

    im = Image.open(filename)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    text = watermark_text.get()

    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    destination = filedialog.askdirectory()
    im.show()

    # Save watermarked image
    im.save(f"{destination}/watermark.jpg")


canvas = Canvas(width=700, height=359)

title = canvas.create_text(350, 30, text="Welcome to the image watermarking desktop app!", width=6000,
                           font=("Arial", 20, "bold"))
subtitle = canvas.create_text(350, 55, text="Get started by pressing the button below!", width=6000, font=("Arial", 15),
                              fill="gray")
canvas.pack()

entry_label = Label(window, text="Watermark text:")
entry_label.pack()

spacing = Canvas(width=10, height=10)

watermark_text = Entry(window)
watermark_text.pack()

spacing.pack()

button = Button(text="Get started", height=2, width=20, command=add_watermark)
button.pack()

window.mainloop()
