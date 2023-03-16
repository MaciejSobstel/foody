from tkinter import Tk, PhotoImage, Scale, HORIZONTAL, Button, Label, Spinbox, StringVar

from foody.generate_menu import generate_message


class Foody():
    def __init__(self, window):
        self.window = window
        window.geometry("800x1200")
        window.title("Foody")

        icon = PhotoImage(file="resources/foodylogo.png")
        # background_photo = PhotoImage(file="/home/ms/Pobrane/background.png")
        # bg_label = Label(window, image=background_photo)
        # bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        window.iconphoto(True, icon)

        self.min_calories = Scale(window, from_=500, to=3000, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Minimum calories", length=300, width=20)
        self.min_calories.set(1000)
        self.min_calories.pack()

        self.max_calories = Scale(window, from_=1000, to=5000, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Maximum calories", length=300, width=20)
        self.max_calories.set(2500)
        self.max_calories.pack()

        self.min_protein = Scale(window, from_=1, to=200, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Minimum protein", length=300, width=20)
        self.min_protein.set(20)
        self.min_protein.pack()

        self.max_protein = Scale(window, from_=1, to=200, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Maximum protein", length=300, width=20)
        self.max_protein.set(50)
        self.max_protein.pack()

        self.min_fat = Scale(window, from_=1, to=200, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Minimum fat", length=300, width=20)
        self.min_fat.set(20)
        self.min_fat.pack()

        self.max_fat = Scale(window, from_=1, to=200, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Maximum fat", length=300, width=20)
        self.max_fat.set(50)
        self.max_fat.pack()

        self.min_sodium = Scale(window, from_=1, to=3000, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Minimum sodium", length=300, width=20)
        self.min_sodium.set(1000)
        self.min_sodium.pack()

        self.max_sodium = Scale(window, from_=1000, to=5000, resolution=1, orient=HORIZONTAL, label=" " * 20 + "Maximum sodium", length=300, width=20)
        self.max_sodium.set(2500)
        self.max_sodium.pack()

        self.breakfast_label = Label(window, text="Number of breakfasts:")
        self.breakfast_label.pack()

        self.num_of_breakfasts = Spinbox(window, from_=1, to=5)

        self.breakfast_increment_button = Button(window, text=">", command=lambda: self.num_of_breakfasts.invoke("buttonup"))
        self.breakfast_decrement_button = Button(window, text="<", command=lambda: self.num_of_breakfasts.invoke("buttondown"))

        self.num_of_breakfasts.pack()
        self.breakfast_increment_button.place(x=500, y=535)
        self.breakfast_decrement_button.place(x=260, y=535)

        self.lunch_label = Label(window, text="Number of lunches:")
        self.lunch_label.pack()

        self.num_of_lunches = Spinbox(window, from_=1, to=5)

        self.lunch_increment_button = Button(window, text=">", command=lambda: self.num_of_lunches.invoke("buttonup"))
        self.lunch_decrement_button = Button(window, text="<", command=lambda: self.num_of_lunches.invoke("buttondown"))

        self.num_of_lunches.pack()
        self.lunch_increment_button.place(x=500, y=580)
        self.lunch_decrement_button.place(x=260, y=580)

        self.dinner_label = Label(window, text="Number of dinners:")
        self.dinner_label.pack()

        self.num_of_dinners = Spinbox(window, from_=1, to=5)

        self.dinner_increment_button = Button(window, text=">", command=lambda: self.num_of_dinners.invoke("buttonup"))
        self.dinner_decrement_button = Button(window, text="<", command=lambda: self.num_of_dinners.invoke("buttondown"))

        self.num_of_dinners.pack()
        self.dinner_increment_button.place(x=500, y=625)
        self.dinner_decrement_button.place(x=260, y=625)

        self.text_menu = StringVar()
        self.text_menu.set("")

        self.start_button = Button(window, text="Generate my menu!", command=self.start_button_command)
        self.start_button.pack()

        self.response_label = Label(window, textvariable=self.text_menu)
        self.response_label.pack()

    def start_button_command(self):
        min_cals = int(self.min_calories.get())
        max_cals = int(self.max_calories.get())
        min_pro = int(self.min_protein.get())
        max_pro = int(self.max_protein.get())
        min_ft = int(self.min_fat.get())
        max_ft = int(self.max_fat.get())
        min_sod = int(self.min_sodium.get())
        max_sod = int(self.max_sodium.get())
        num_breakfasts = int(self.num_of_breakfasts.get())
        num_lunches = int(self.num_of_lunches.get())
        num_dinners = int(self.num_of_dinners.get())
        menu = generate_message(min_cals, max_cals, min_pro, max_pro, min_ft, max_ft, min_sod, max_sod, num_breakfasts, num_lunches, num_dinners)
        self.text_menu.set(menu)


root = Tk()
app = Foody(root)
root.mainloop()
