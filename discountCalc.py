from pathlib import Path
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Window
window = Tk()
window.geometry("869x578")
window.configure(bg="#FFFFFF")

# Canvas
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=578,
    width=869,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

# Avatar
avatarImage = PhotoImage(file=assets("avatar.png"))
avatar = canvas.create_image(435.0, 60.0, image=avatarImage)

# Half Circle
halfCircleImage = PhotoImage(file=assets("halfCircle.png"))
halfCircle = canvas.create_image(418.0, 260.0, image=halfCircleImage)
canvas.create_rectangle(0.0, 239.0, 869.0, 578.0, fill="#403F3F", outline="")

# Red Banner
redBannerImage = PhotoImage(file=assets("redBanner.png"))
canvas.create_image(434.0, 263.0, image=redBannerImage)

# Input Backgrounds
canvas.create_rectangle(75.0, 261.0, 428.0, 501.0, fill="#C4C4C4", outline="")
canvas.create_rectangle(510.0, 261.0, 804.0, 409.0, fill="#C4C4C4", outline="")

# Inputs
entryImage = PhotoImage(file=assets("entry.png"))
canvas.create_image(332.5, 308.5, image=entryImage)
canvas.create_image(332.5, 356.5, image=entryImage)
priceInput = Entry(bd=0, bg="#F3F1F1", highlightthickness=0)
priceInput.place(x=277.0, y=293.0, width=111.0, height=29.0)
discountInput = Entry(bd=0, bg="#F3F1F1", highlightthickness=0)
discountInput.place(x=277.0, y=341.0, width=111.0, height=29.0)

# Output
output = StringVar()
outputLabel = Label(window, text="", textvariable=output)
outputLabel.place(x=602.0, y=332.0, width=111.0, height=29.0)

# Calculation Function
def calculateDiscountedPrice():
    price = float(priceInput.get())
    discount = float(discountInput.get())
    discountedPrice = price - price * discount / 100
    output.set(discountedPrice)


# Button
calculateButtonImage = PhotoImage(file=assets("calculateButton.png"))
calculateButton = Button(
    image=calculateButtonImage,
    borderwidth=0,
    highlightthickness=0,
    command=calculateDiscountedPrice,
    relief="flat",
)
calculateButton.place(x=162.0, y=422.0, width=180.0, height=34.0)

# Text
canvas.create_text(
    169.0,
    153.0,
    anchor="nw",
    text="Whats the Discount Bruh?",
    fill="#2E2E2E",
    font=("ReemKufi Regular", 48 * -1),
)
canvas.create_text(
    412.0,
    527.0,
    anchor="nw",
    text="\nKoding With Khanh",
    fill="#EEE9E9",
    font=("ReemKufi Regular", 13 * -1),
)
canvas.create_text(
    108.0,
    341.0,
    anchor="nw",
    text="Discount (%): ",
    fill="#575555",
    font=("Roboto", 24 * -1),
)
canvas.create_text(
    108.0,
    293.0,
    anchor="nw",
    text="Price ($):",
    fill="#575454",
    font=("Roboto", 24 * -1),
)
canvas.create_text(
    546.0,
    287.0,
    anchor="nw",
    text="Discounted Price ($): ",
    fill="#575555",
    font=("Roboto", 24 * -1),
)

window.resizable(False, False)
window.mainloop()
