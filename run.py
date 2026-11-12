# Einstieg 

import sys 
from pathlib import Path

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from nicegui import ui
from src.pages import erstellen , uebersicht

# Menü erstellen
def create_menu():
    with ui.header().classes('item-center justify-between bg-gray-100 p-4 shadow-md'):
        with ui.row().style('align-items: center;'):
            ui.label('Terminverwaltung').style('font-size: 24px; font-weight: bold; color: black;')
            ui.button('Home', on_click=lambda: ui.navigate.to('/')).style('margin-left: 20px;')
            ui.button("Neuen Termin erstellen", on_click=lambda: ui.navigate.to('/erstellen')).style('margin-left: 10px;')
            ui.button("Übersicht", on_click=lambda: ui.navigate.to('/uebersicht')).style('margin-left: 10px;')
            ui.button("Info", on_click=lambda: ui.navigate.to('/info')).style('margin-left: 10px;')

# Landingpage
@ui.page('/')
def landingpage():
    create_menu()

# Eintrag erstellen-Seite    
@ui.page('/erstellen')
def erstellen_page():
    create_menu()
    with ui.column().classes('w-full p-4'):
        erstellen.erstellen_page()

# Übersicht-Seite
@ui.page('/uebersicht')        
def uebersicht_page():
    create_menu()
    uebersicht.erstellen_page()

# Info-Seite
@ui.page('/info') 
def info_page():
    create_menu()
    with ui.column().classes('w-full items-center justify-center'):
        ui.label('Info-Seite').style('font-size: 24px; font-weight: bold; color: black; margin-bottom: 20px;')
        ui.label('Hier können Sie Informationen über die Anwendung anzeigen.').style('font-size: 16px; color: black;')       

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(title='Terminverwaltung', reload = True, port=8080)    