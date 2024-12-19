import flet as ft
from windowsControl import WindowsControl
from styles.colors import BACKGROUND_COLOR


def main(page: ft.Page):

    wc = WindowsControl(page)

    page.padding = 0
    page.margin = 0
    page.spacing = 0
    page.bgcolor = BACKGROUND_COLOR
    page.update()

ft.app(main)
