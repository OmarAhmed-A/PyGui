
import PySimpleGUI as sg
layout = [
    [sg.Input(key= 'input', size= (10,1)), sg.Combo(['km to mile', 'kg to Pound', 'sec to min', 'C to F'], key= 'unit', default_value= 'km to mile', size= (10, 1)),sg.Button('Convert'), sg.Button('Reverse')], 
    [sg.Text('Result = ', size= (10,1)), sg.Text('', key= 'result', size= (10,1))]
]

window = sg.Window('Unit Converter', layout)


#  convert the input to the desired unit
def convert(input, unit):
    if unit == 'km to mile':
        return input * 0.621371
    elif unit == 'kg to Pound':
        return input * 2.20462
    elif unit == 'sec to min':
        return input / 60
    elif unit == 'C to F':
        return input * 1.8 + 32
    
    #convert reveresed
    if unit == 'mile to km':
        return input * 1.60934
    elif unit == 'Pound to kg':
        return input * 0.453592
    elif unit == 'min to sec':
        return input * 60
    elif unit == 'F to C':
        return (input - 32) / 1.8
    
    
#  reverse the unit
def reverse(unit):
    if unit == 'km to mile':
        return 'mile to km'
    elif unit == 'mile to km':
        return 'km to mile'
    elif unit == 'kg to Pound':
        return 'Pound to kg'
    elif unit == 'Pound to kg':
        return 'kg to Pound'
    elif unit == 'sec to min':
        return 'min to sec'
    elif unit == 'min to sec':
        return 'sec to min'
    elif unit == 'C to F':
        return 'F to C'
    elif unit == 'F to C':
        return 'C to F'
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert':
        result = convert(float(values['input']), values['unit'])
        unit = values['unit'].split(" to ")[1]
        window['result'].update("{:.2f} {}".format(result, unit))
    elif event == 'Reverse':
        window['unit'].update(reverse(values['unit']))
        result = convert(float(values['input']), reverse(values['unit']))
        unit = reverse(values['unit']).split(" to ")[1]
        window['result'].update("{:.2f} {}".format(result, unit))

window.close()
