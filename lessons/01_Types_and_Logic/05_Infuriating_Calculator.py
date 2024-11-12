"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk

window = Tk()

window.withdraw()
 
numberone = simpledialog.askinteger("Number", "What is the first number")

numbertwo= simpledialog.askinteger("Number", "What is the second number") 

operation=simpledialog.askstring("Operation", "Which operation? multiply,divide,add,subtract")
if operation=="add":
   sum=numberone+numbertwo
   messagebox.showinfo('Adder', "the sum is " + str(sum))   

elif operation=="subtract":
   difference=numberone-numbertwo
   messagebox.showinfo('Subtracter', "the difference is " + str(difference))   

elif operation=="multiply":
   product=numberone*numbertwo
   messagebox.showinfo('Multiplier', "the product is " + str(product))   

elif operation=="divide": 
   quotient=numberone/numbertwo
   messagebox.showinfo('Divider', "the quotient is " + str(quotient))   

else:
   messagebox.showerror("You have entered an unsupported operation")


# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
