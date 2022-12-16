import PySimpleGUI as sg
import tkinter as tk
from tkinter import ttk
import time
from plyer import notification

#Skapar fönstret
root = tk.Tk()
root.title("GUI Handler")

#Skapar notifikation knapp
button = ttk.Button(root, text="Behöver du hjälp?")

#Definera funktionen som kallar när knappen trycks
def send_notification():
    #Få meddelande från patienten 
    message = entry.get()

    #Skickar notifikation
    notification.notify(
        title="Notification",
        message=message,
        app_name="Python Notification Example"
    )

#Bifoga funktionen till knappens klickhändelse
button.config(command=send_notification)

#Skapa ett inmatningsfält för meddelandet
entry = ttk.Entry(root, width=100)

#Lägg ut widgetarna i fönstret
button.pack()
entry.pack()

#Starta huvudevenemangsslingan 
root.mainloop()

