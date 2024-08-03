                                               # Project-2 [ BMI( BODY MASS INDEX CALCULATOR)] , Level-1

# Import the tkinter library for creating the GUI
import tkinter as tk
# Import messagebox from tkinter for showing error messages
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get height and weight from entry fields and convert to float
        height = float(height_entry.get())   # This tries to get the height and weight values from the entry fields and convert them to floats (decimal numbers).
        weight = float(weight_entry.get())
        
        # Check if height and weight are positive
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        
        # Calculate BMI: weight (kg) / (height (m))^2
        bmi = weight / ((height/100) ** 2)
        # Round BMI to 2 decimal places
        bmi = round(bmi, 2)
        # Get the BMI category
        category = get_bmi_category(bmi)
        
        # Update the text property of the result label using the config method
        # This dynamically changes the displayed text to show the calculated BMI and its category
        result_label.config(text=f"Your BMI: {bmi}\nCategory: {category}")

    except ValueError as e:
        # Show error message if input is invalid
        '''
         messagebox.showerror() is a Tkinter function that displays an error message box.

         The first argument "Input Error" is the title of the error box.
         str(e) converts the exception object to a string, which becomes the content of the error message.
        '''
        messagebox.showerror("Input Error", str(e))

# Function to determine BMI category
def get_bmi_category(bmi):
    if bmi < 16:
        return "Severely Underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Create the main window
root = tk.Tk()
# Set the title of the window
root.title("BMI Calculator")
# Set the size of the window (width x height)
root.geometry("300x250")        # This sets the initial size of the window to 300 pixels wide and 250 pixels tall

# Create and place a label for height
tk.Label(root, text="Height (cm):").pack(pady=5) # This creates a text label saying "Height (cm):" and places it in the window. pady=5 adds 5 pixels of vertical padding.
# Create an entry field for height
height_entry = tk.Entry(root)
# Place the height entry field in the window
height_entry.pack() 

# Create and place a label for weight
tk.Label(root, text="Weight (kg):").pack(pady=5)
# Create an entry field for weight
weight_entry = tk.Entry(root)   # This creates an input field (entry widget) where the user can type their height.
# Place the weight entry field in the window
weight_entry.pack()   # This places the height entry field in the window, below the "Height (cm):" label

# Create a button that will call the calculate_bmi function when clicked
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
# Place the calculate button in the window
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
# Place the result label in the window
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
'''
 This starts the main event loop of the application. 
 It keeps the window open and responsive to user interactions until the user closes the window.
'''