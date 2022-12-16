import PySimpleGUI as sg
import tkinter as tk
from tkinter import ttk
import time
from plyer import notification

# Create the main window
root = tk.Tk()
root.title("GUI Handler")

# Create the notification button
button = ttk.Button(root, text="Behöver du hjälp?")

# Define the function that will be called when the button is clicked
def send_notification():
    # Get the message from the user
    message = entry.get()

    # Send the notification
    notification.notify(
        title="Notification",
        message=message,
        app_name="Python Notification Example"
    )

# Attach the function to the button's click event
button.config(command=send_notification)

# Create an input field for the message
entry = ttk.Entry(root, width=100)

# Lay out the widgets in the window
button.pack()
entry.pack()

# Start the main event loop
root.mainloop()

