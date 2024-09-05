import customtkinter

text = "Welcome to lapis mining press the button on the bottom to mine lapis"
potato = 5000  # Initialize potato globally
level = 1

def op_button():
    global potato
    potato -= potato - 1
    button.configure(text=str(potato))  # Update the button text

def button_callback():
    global text
    global potato
    global level
    funny = 0

    potato -= 1

    print(potato)

    if potato == 4999 + funny:
        text = "Good job you did it now when you get at 48000 i have a suprise for you"
    elif potato == 4800 + funny:
        text = "Good job again here is a buddy to help you out when you reach 40000 you will get a better buddy"
        potato = potato - 100 * level
    elif potato == 4000 + funny:
        text = "Wow you actually did it here have another buddy try to get 30000"
        potato = potato - 100 * level
    elif potato == 3000 + funny:
        text = "Im suprised you have a good atention span here have upgrades for your buddy come back at 20000"
        potato = potato - 400 * level
    elif potato == 2000 + funny:
        text = "Get a life here have 5 more buddies wait until 10000"
        potato = potato - 500 * level
    elif potato == 1000 + funny:
        text = "So close have another 3 buddies"
        potato = potato - 300 * level
    elif potato == 900 + funny:
        text = "Only 500 more"
    elif potato == 500 + funny:
        text = "500 only more"
    elif potato == 1 + funny:
        text = "One more!"
    elif potato == 0 + funny:
        text = "Wow good job!!!! I will rebirth you so when you get upgrades again they are stronger but it will be harder"
        level += 1
        funny = 7000 * level
        potato = 5000 * level - 6000
        text = "Yo wassup again lil bro i gotchu with my skibidi rizz"
        funnything = str(level)

    button.configure(text=str(potato))  # Update the button text
    button2.configure(text=str(text))  # Update the button text
    button3.configure(text=f"Your at level {funnything}. Every time you win you get better buddies but stronger lapis")

app = customtkinter.CTk()
app.geometry("1700x800")

button2 = customtkinter.CTkButton(app, text=text)
button2.pack(padx=80, pady=50, ipady=70, ipadx=50, side="top")

button3 = customtkinter.CTkButton(app, text="Your at level 1. Every time you win you get better buddies but stronger lapis")
button3.pack(padx=40, pady=40, ipady=40, ipadx=800, side="bottom")

button4 = customtkinter.CTkButton(app, text="Press to set health to 1", command=op_button)
button4.pack(padx=20, pady=20, ipady=40, ipadx=800, side="bottom")

button = customtkinter.CTkButton(app, text=str(potato), command=button_callback)
button.pack(padx=20, pady=20, ipady=600, ipadx=600)

app.mainloop()
