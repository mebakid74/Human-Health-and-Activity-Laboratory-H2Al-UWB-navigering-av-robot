import PySimpleGUI as sg

#Skapar fönstret
sg.Window(title="Hello World", layout=[[]], margins=(200,150)).read()

layout = [
    [sg.Text("Fall detekterat")],
    [sg.Button("Skicka hjälp")]
    ]

#Skapar fönstret
window = sg.Window("GUI Handler", layout,margins=(100,50))

#Skapar event loop
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()

#30 sek timeout
#inställningar på robot
#patient profil inställning
