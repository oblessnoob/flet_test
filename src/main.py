import flet as ft
import os


def main(page: ft.Page):
    match page.platform:
        case ft.PagePlatform.WINDOWS:
            platform = ft.Text("Platform: Windows", size=20)
        case ft.PagePlatform.LINUX:
            platform = ft.Text("Platform: Linux", size=20)
        case ft.PagePlatform.MACOS:
            platform = ft.Text("Platform: Mac OS", size=20)
        case ft.PagePlatform.ANDROID:
            platform = ft.Text("Platform: Android", size=20)
        case ft.PagePlatform.ANDROID_TV:
            platform = ft.Text("Platform: Android TV", size=20)
        case ft.PagePlatform.IOS:
            platform = ft.Text("Platform: iOS", size=20)

    datavar = ft.Text("FLET_APP_STORAGE_DATA: "+str(os.getenv("FLET_APP_STORAGE_DATA")), size=20)
    tempvar = ft.Text("FLET_APP_STORAGE_TEMP: "+str(os.getenv("FLET_APP_STORAGE_TEMP")), size=20)
    platformvar = ft.Text("FLET_PLATFORM: "+str(os.getenv("FLET_PLATFORM")), size=20)


    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column(
                    [
                        platform,
                        datavar,
                        tempvar,
                        platformvar
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
