from tkinter import *
 
def calculateDiscountedPrice():
    price = float(priceInput.get())
    discount = float(discountInput.get())
    discountedPrice=price-price*discount/100
    output.set(discountedPrice)
 
window = Tk()
output=StringVar()
Label(window, text="Price ($)").grid(row=0, sticky=W)
Label(window, text="Discount (%)").grid(row=1, sticky=W)
Label(window, text="Discounted Price ($):").grid(row=3, sticky=W)
Label(window, text="", textvariable=output).grid(row=3,column=1, sticky=W)
 
priceInput = Entry(window)
discountInput = Entry(window)
 
priceInput.grid(row=0, column=1)
discountInput.grid(row=1, column=1)
 
button = Button(window, text="Calculate", command=calculateDiscountedPrice)
button.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
mainloop()