import PySimpleGUI as sg

sg.theme('DarkAmber')
TITLE = 'File Writer'
window = sg.Window(TITLE)

layout_choose_file = [
    [sg.Text('', size=(20,1)), sg.Text(TITLE, font=('Any 20'), auto_size_text=True, justification='center'), sg.Text('', size=(20,1))],
    [sg.Text('Select File To Write Into: ')],
    [sg.Input(key='open_file'), sg.FileBrowse()],
    [sg.Text('...or Create A New File: '), sg.Input(key='new_file')],
    [sg.Button('Choose File'), sg.Button('Quit')]
]

layout_add_text = [
    [sg.Text('', size=(20,1)), sg.Text(TITLE, font=('Any 20'), auto_size_text=True, justification='center'), sg.Text('', size=(20,1))],
    [sg.Text('Input To Add: '), sg.Input()],
    [sg.Button('Add Text'), sg.Button('Quit')]
]

window.layout(layout_choose_file)

while True:
    event, values = window.read()

    if(event == sg.WIN_CLOSED or event == 'Quit'):
        break

    if(event == 'Choose File'):
        window.close()
        window = sg.Window(TITLE)
        window.layout(layout_add_text)

window.close()