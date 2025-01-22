# import flet as ft

# ft.app(target=main, view=ft.AppView.WEB_BROWSER)

# def main(page: ft.Page):
#     t = ft.Text(value="Hello, world!", color="green")
#     page.controls.append(t)
#     page.update()

# ft.app(target=main)
# def main(page):
#     page.title = "Zodiac"
# main()

d = 0
import flet as ft
def couunt(p):
    global d
    d+=1
    print(d)
    return d
def main(page):
    global d
    # t = ft.Text(value="Hello, world!")
    t = ft.Button(text=f'{d}', on_click=couunt)
    print('-', d)
    page.controls.append(t)
    page.update()

ft.app(target=main)