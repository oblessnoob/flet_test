import flet as ft


def main(page: ft.Page):
    match page.platform:
        case ft.PagePlatform.WINDOWS:
            platform = ft.Text("Windows")
        case ft.PagePlatform.LINUX:
            platform = ft.Text("Linux")
        case ft.PagePlatform.MACOS:
            platform = ft.Text("MacOS")
        case ft.PagePlatform.ANDROID:
            platform = ft.Text("Android")
        case ft.PagePlatform.ANDROID_TV:
            platform = ft.Text("Android TV")
        case ft.PagePlatform.IOS:
            platform = ft.Text("iOS")
    page.add(
        ft.SafeArea(
            ft.Container(
                platform,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
