# Import the tkinter module
import tkinter

# Creating the GUI window.
root = tkinter.Tk()
root.title("Welcome to GeekForGeeks")
root.geometry("400x240")

# Creating our text widget.
sample_text = tkinter.Text( root, height = 10)
sample_text.pack()

# Creating a tuple containing
# the specifications of the font.
Font_tuple = ("Comic Sans MS", 20, "bold")

# Parsed the specifications to the
# Text widget using .configure( ) method.
sample_text.configure(font = Font_tuple)
root.mainloop()
