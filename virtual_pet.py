from tkinter import HIDDEN, NORMAL, Tk, Canvas

class ScreenPet:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Pet")
        self.c = Canvas(root, width=400, height=400)
        self.c.configure(bg='dark blue', highlightthickness=0)
        self.body_color = 'SkyBlue1'
        self.happy_level = 10
        self.eyes_crossed = False
        self.tongue_out = False

        # Initialize body parts
        self.body = self.c.create_oval(35, 20, 365, 350, outline=self.body_color, fill=self.body_color)
        self.eye_left = self.c.create_oval(130, 110, 160, 170, outline='black', fill='white')
        self.pupil_left = self.c.create_oval(140, 145, 150, 155, outline='black', fill='black')
        # ... (other body parts)

        self.c.pack()
        self.c.bind('<Motion>', self.show_happy)
        self.c.bind('<Leave>', self.hide_happy)
        self.c.bind('<Double-1>', self.cheeky)

        # Start animations
        self.root.after(1000, self.blink)
        self.root.after(5000, self.sad)

    def toggle_eyes(self):
        current_color = self.c.itemcget(self.eye_left, 'fill')
        new_color = self.body_color if current_color == 'white' else 'white'
        current_state = self.c.itemcget(self.pupil_left, 'state')
        new_state = NORMAL if current_state == HIDDEN else HIDDEN
        self.c.itemconfigure(self.pupil_left, state=new_state)
        self.c.itemconfigure(self.pupil_right, state=new_state)
        self.c.itemconfigure(self.eye_left, fill=new_color)
        self.c.itemconfigure(self.eye_right, fill=new_color)

    def blink(self):
        self.toggle_eyes()
        self.root.after(250, self.toggle_eyes)
        self.root.after(3000, self.blink)

    # ... (other methods)

if __name__ == "__main__":
    root = Tk()
    pet = ScreenPet(root)
    root.mainloop()
# De-Bugged and coded with love by Zioles(Dhrruv).
