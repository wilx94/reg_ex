from tkinter import Tk, Label, Button, Entry, Canvas


class UI:
    def __init__(self, master):
        self.master = master

        # title
        master.title("RegEx Analyzer")

        # label
        self.label = Label(
            master, text='Insert your string characters.\n RegEx considered: [ab]*(c|d)+e?f.h')
        self.label.pack()

        # entry
        self.entry = Entry(master)
        self.entry.pack()

        # verify button
        self.verify_button = Button(master, text='Verify', command=self.verify)
        self.verify_button.pack()

        # canvas
        self.canvas = Canvas(master, width=225, height=35, bg='white')
        self.canvas.pack()

        # close button
        self.close_button = Button(master, text='Close', command=master.quit)

    def verify(self):
        states = {
            -1: {'a': 0, 'b': 0, 'c': 1, 'd': 1},
            0: {'a': 0, 'b': 0, 'c': 1, 'd': 1},
            1: {'c': 1, 'd': 1, 'e': 2, 'f': 3},
            2: {'f': 3},
            3: 4,
            4: {'h': 5}
        }

        value = self.entry.get()

        state = -1
        reg_ex = True

        for ix, value in enumerate(value):
            try:
                state = states[state][value] if type(
                    states[state]) == dict else states[state]
            except Exception as ex:
                reg_ex = False
                self.label['text'] = "Your string does not match the regular expression.\n Insert another."
                break

        if reg_ex:
            self.label['text'] = "This string match with regular.\n You can try it again."

        if state != 5:
            self.label['text'] = "Your string does not match the regular expression.\n Insert another."
        self.draw(state)

    def draw(self, state):
        self.canvas.delete('all')

        # drawing circle
        for i in range(0, state + 1):
            self.canvas.create_oval(
                0 + i * 40, 0, 25 + i * 40, 25, fill='green')
        # drawing line
        for i in range(0, state):
            self.canvas.create_line(25 + i * 40, 12.5, 40 + i * 40, 12.5)


root = Tk()
ui = UI(root)
root.mainloop()
