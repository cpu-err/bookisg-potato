def main():
    window()
    porgram()

def window():
    import PySimpleGUI as sg
    layout = [
        [sg.Text('Окно'), sg.InputCombo(('ЛОЛ', 'КЕК'), size = '80x60')],
        [sg.Submit()]

    ]
    window = sg.Window('Окно', layout)
    event, values = window.read()
    window.close()

    sg.popup()


def program():
    pass


main()
