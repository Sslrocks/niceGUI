from nicegui import ui
from datetime import datetime 

def erstellen_page():
    ui.label('Neuen Termin erstellen').classes('text 3xl font-bold mb-4')


    with ui.card().classes('w-full max-w-md p-6 bg-white rounded-lg shadow-md'):
        #ui.label('Bitte geben Sie die Details für den neuen Termin ein:').style('font-size: 16px; color: black; margin-bottom: 10px;')
        titel_inpput = ui.input(label='Titel', placeholder='Titel des Termins').classes('w-full')
        with ui.row().classes('w-full gap-4'):
            datum_input = ui.date(value='today').classes('flex-1')
            uhrzeit_input = ui.time(value='09:00').classes('flex-1')
            
        dauer_input = ui.number('Dauer (in Minuten)', value=60, min =15).classes('w-full')    
        beschreibung_input =ui.textarea(label='Beschreibung', placeholder='Beschreibung des Termins').classes('w-full')
        ui.button('Termin erstellen', on_clicgitk=lambda: termin_einstellen).classes('w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors duration-300')

        def termin_einstellen():
            if not titel_inpput.value or not datum_input.value or not uhrzeit_input.value:
                ui.notify('Bitte füllen Sie alle erforderlichen Felder aus.', type='error', position='top-right', timeout=3000)
                return
            
            # Hier können Sie die Logik implementieren, um den Termin zu speichern oder weiterzuverarbeiten
            str = titel_inpput.value + " " + datum_input.value + " " + uhrzeit_input.value + " " + beschreibung_input.value
            ui.notify('Termin erfolgreich erstellt!' + str , type='success', position='top-right', timeout=3000)
    