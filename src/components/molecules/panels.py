import flet as ft
from components.atoms.buttons import MenuButton
from styles.colors import PRIMARY_COLOR, BACKGROUND_COLOR

class SidePanel:

    def __init__ (self, changeWindows):
        self.inicio = MenuButton("Inicio", None, ft.Icons.HOME, True, changeWindows, 1)
        self.analisis = MenuButton("Analisis", None, ft.Icons.ANALYTICS, False, changeWindows, 2)
        self.interactivos = MenuButton("Gráficos Interactivos", None, ft.Icons.AUTO_GRAPH, False, changeWindows, 3)
        self.conclusiones = MenuButton("Conclusiones", None, ft.Icons.MENU_BOOK, False, changeWindows, 4)
        self.proyecto = MenuButton("Nuestro Proyecto", None, ft.Icons.EMOJI_PEOPLE, False, changeWindows, 5)

        self.sp = ft.Container(
        content = ft.Column(
            controls=[
                ft.Container(
                    height=300,
                    content = ft.Image(src="C:\\Users\\Tessa\\Documents\\SIC-proyecto1\\CAF-CCH\\src\\assets\\lg.png")
                ),
                self.inicio.btn,
                self.analisis.btn,
                self.conclusiones.btn,
                self.proyecto.btn
            ],
            expand = True,
        ),
        bgcolor = PRIMARY_COLOR,
        width=300
        )

class MainPanel:

    def __init__ (self):
        
        self.mp = ft.Container(
            bgcolor=BACKGROUND_COLOR,
            expand=True
        )