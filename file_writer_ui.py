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

