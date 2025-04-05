from tkinter import *

medicine = {
    "Medicine A": 10,
    "Medicine B": 20,
    "Medicine C": 25,
    "Medicine D": 15,
}

invoice_medicine = []

def add_medicine():
    selected_med = medicine_listbox.get(ANCHOR)
    amount = int(quantity_entry.get())
    price = medicine[selected_med]
    total = amount * price
    invoice_medicine.append((selected_med, amount, total))
    total_amount_entry.delete(0, END)
    total_amount_entry.insert(END, str(calculate_total()))
    update_invoice_text()

def calculate_total():
    total = 0.0
    for item in invoice_medicine:
        total += item[2]
        
    return total


def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_medicine:
        invoice_text.insert(END, f"Medicine: {item[0]}, Amount: {item[1]}, Price: {item[2]}\n")

window = Tk()
window.title("Invoice Generator")

medicine_label = Label(window, text="Medicine: ")
medicine_label.pack()

medicine_listbox = Listbox(window, selectmode=SINGLE)
for med in medicine:
    medicine_listbox.insert(END, med)
medicine_listbox.pack()

quantity_label = Label(window, text="Quantity")
quantity_label.pack()
quantity_entry = Entry(window)
quantity_entry.pack()

add_button = Button(window, text="Add medicine", command=add_medicine)
add_button.pack()

total_amount_label = Label(window, text="Total Amount")
total_amount_label.pack()
total_amount_entry = Entry(window)
total_amount_entry.pack()

customer_label = Label(window, text="Customer Name: ")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(window, text="Generate Invoive")
generate_button.pack()

invoice_text = Text(window, height=10, width=50)
invoice_text.pack()

window.mainloop()