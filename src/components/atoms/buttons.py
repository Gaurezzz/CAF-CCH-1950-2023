import flet as ft
from .text import p1
from styles.colors import SECONDARY_COLOR, PRIMARY_COLOR, BACKGROUND_COLOR


class MenuButton:

    def activate(self):
        self.selected = True
        self.bgcolor = SECONDARY_COLOR
        self.color = PRIMARY_COLOR
        self.btn.bgcolor = self.bgcolor
        self.btn.color = self.color
        self.btn.icon_color = self.color

    def deactivate(self):
        self.selected = False
        self.bgcolor = PRIMARY_COLOR
        self.color = BACKGROUND_COLOR
        self.btn.bgcolor = self.bgcolor
        self.btn.color = self.color
        self.btn.icon_color = self.color

    def clickAction(self, changeWindows):
        print("click")
        changeWindows(self.wn)
    
        

    def __init__(self, Text, Page, Icono, Selected, changeWindows, windowsNumber):
        self.text = Text
        self.page = Page
        self.icon = Icono
        self.selected = Selected
        self.bgcolor = PRIMARY_COLOR
        self.color = BACKGROUND_COLOR
        self.wn = windowsNumber

        if self.selected:
            self.bgcolor=SECONDARY_COLOR
            self.color=PRIMARY_COLOR

        self.btn = ft.FilledButton(
        text=self.text,
        icon = self.icon,
        on_click=lambda e: self.clickAction(changeWindows),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),
            text_style=ft.TextStyle(
            font_family="Roboto-Slab",
            weight='Bold',
            size=16
        )
        ),
        width=300,
        height=50,
        bgcolor=self.bgcolor,
        icon_color=self.color,
        color = self.color
    )

