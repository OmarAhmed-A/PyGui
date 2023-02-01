import PySimpleGUI as sg



def create_window(theme):
    sg.theme(theme)   # Add a touch of color
    sg.set_options(font=('Helvetica', 12), button_element_size=(
        6, 3), auto_size_buttons=False, element_padding=(4, 4))
    # All the stuff inside your window.
    button_size = (6, 3)
    layout = [[sg.Push(), sg.Text('', font=("Helvetica", 25), pad=(10, 20), right_click_menu=theme_menu, key='out')],
              [sg.Button('clear', expand_x=True),
               sg.Button('Enter', expand_x=True)],
              [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button(
                  '9', size=button_size), sg.Button('/', size=button_size)],
              [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button(
                  '6', size=button_size), sg.Button('*', size=button_size)],
              [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button(
                  '3', size=button_size), sg.Button('-', size=button_size)],
              [sg.Button('0', expand_x=True), sg.Button(
                  '.', size=button_size), sg.Button('+', size=button_size)]
              ]
    return sg.Window('Calculator', layout, finalize=True)



theme_menu = ['menu', ['Black', 'Reddit', 'Python',
                       'DarkAmber', 'SystemDefault', 'random']]
current_num = []
full_expression = []
# Create the window
window = create_window('DarkAmber')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    if event in '1234567890.':
        current_num.append(event)
        num_string = ''.join(current_num)
        cfexp = full_expression.copy() + [num_string]
        window['out'].update(' '.join(cfexp))
    if event in '+-*/':
        full_expression.append(num_string)
        full_expression.append(event)
        current_num = []
        window['out'].update(' '.join(full_expression))
    if event == '=':
        full_expression.append(num_string)
        full_expression.append(event)
        current_num = []
        window['out'].update(''.join(full_expression))
        window['out'].update(eval(''.join(full_expression)))
        full_expression = []
    if event == 'Enter':
        full_expression.append(num_string)
        current_num = []
        window['out'].update(''.join(full_expression))
        window['out'].update(eval(''.join(full_expression)))
        full_expression = []
    if event == 'clear':
        current_num = []
        full_expression = []
        window['out'].update('')


window.close()
