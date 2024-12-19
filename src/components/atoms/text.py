import flet as ft
from styles.colors import PRIMARY_COLOR

def h1(text: str):
    return ft.Container(
        content=ft.Text(
            text,
            font_family="Alegreya",
            weight='Bold',
            size=75,
            color=PRIMARY_COLOR
        ),
        padding=ft.padding.only(top=50, left=50, right=50)
    )

def h2(text: str):
    return ft.Container(
        content=ft.Text(
            text,
            font_family="Alegreya",
            weight='Medium',
            size=50,
            color=PRIMARY_COLOR
        ),
        padding=ft.padding.only(top=30,left=50, right=50)
    )

def h3(text: str):
    return ft.Container(
        content=ft.Text(
            text,
            font_family="Alegreya",
            weight='Medium',
            size=35,
            color=PRIMARY_COLOR
        ),
        padding=ft.padding.only(top=20, left=50, right=50)
    )

def h4(text: str):
    return ft.Container(
        content=ft.Text(
            text,
            font_family="Alegreya",
            weight='Medium',
            size=25,
            color=PRIMARY_COLOR
        ),
        padding=ft.padding.only(top=18, left=50, right=50)
    )

def p1(text: str):
    return ft.Container(
        content=ft.Text(
            text,
            font_family="Roboto-Slab",
            weight='Regular',
            size=18,
            color=PRIMARY_COLOR
        ),
        padding=ft.padding.only(top=18, left=50, right=50)
    )

def p2(text: str):
    return ft.Container(
        content=ft.Text(
            text,
            font_family="Roboto-Slab",
            weight='Regular',
            size=15,
            color=PRIMARY_COLOR
        ),
        padding=ft.padding.only(top=15, left=50, right=50)
    )