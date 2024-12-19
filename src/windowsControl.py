from components.molecules.panels import SidePanel, MainPanel
import flet as ft
from components.molecules.windows import Windows

class WindowsControl:

    def __init__ (self, page):

        self.sp = None
        self.sp = SidePanel(self.changeWindows)
        self.mp = MainPanel()
        self.page = page
        self.windows = Windows(self.changeWindows)

        view = ft.Row(
            controls = [self.sp.sp,self.mp.mp],
            expand=True,
            spacing=0,
        )

        self.mp.mp.content = self.windows.inicio

        self.page.add(view)
    
    def changeWindows(self,windowsNumber):
        if (self.sp != None):
            if windowsNumber == 1:
                self.sp.inicio.activate()
                self.sp.analisis.deactivate()
                self.sp.interactivos.deactivate()
                self.sp.conclusiones.deactivate()
                self.sp.proyecto.deactivate()
                self.mp.mp.content = self.windows.inicio
            elif windowsNumber == 2:
                self.sp.inicio.deactivate()
                self.sp.analisis.activate()
                self.sp.interactivos.deactivate()
                self.sp.conclusiones.deactivate()
                self.sp.proyecto.deactivate()
                self.mp.mp.content = self.windows.espera
                self.page.update()
                self.mp.mp.content = self.windows.analisis
            elif windowsNumber == 3:
                self.sp.inicio.deactivate()
                self.sp.analisis.deactivate()
                self.sp.interactivos.activate()
                self.sp.conclusiones.deactivate()
                self.sp.proyecto.deactivate()
                self.mp.mp.content = self.windows.interactivos
            elif windowsNumber == 4:
                self.sp.inicio.deactivate()
                self.sp.analisis.deactivate()
                self.sp.interactivos.deactivate()
                self.sp.conclusiones.activate()
                self.sp.proyecto.deactivate()
                self.mp.mp.content = self.windows.conclusiones
            else:
                self.sp.inicio.deactivate()
                self.sp.analisis.deactivate()
                self.sp.interactivos.deactivate()
                self.sp.conclusiones.deactivate()
                self.sp.proyecto.activate()
                self.mp.mp.content = self.windows.proyecto

            self.page.update()