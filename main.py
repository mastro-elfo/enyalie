from nicegui import app, ui

app.add_static_files("/assets", "./assets")

HOME = (43.575, 10.775)
HOME_ZOOM = 13
PRIMARY = "#482880"
SECONDARY = "#4caf50"
ACCENT = "#111B1E"
POSITIVE = "#53B689"


@ui.page("/")
def dashboard():
    ui.dark_mode(value=True)
    ui.colors(primary=PRIMARY, secondary=SECONDARY, accent=ACCENT, positive=POSITIVE)
    ui.query(".nicegui-content").classes("absolute top-0 bottom-0 left-0 right-0 p-0")
    ui.add_head_html(
        "<style>@font-face { font-family: 'Elfic-Cursive'; src: url('/assets/fonts/"
        "Tangerine-Regular.ttf'); font-weight: normal; font-style: normal;"
        " }</style>"
    )

    def handle_back_to_home(leaflet):
        leaflet.set_center(HOME)
        leaflet.set_zoom(HOME_ZOOM)

    with ui.dialog() as new_path_dialog, ui.card():
        ui.label("New path").style("font-size: 2em;")
        ui.button("Close", on_click=new_path_dialog.close)

    with ui.dialog() as settings_dialog, ui.card():
        ui.label("Settings").style("font-size: 2em;")
        ui.button("Close", on_click=settings_dialog.close)

    with ui.dialog() as filters_dialog, ui.card():
        ui.label("Filters").style("font-size: 2em;")
        ui.button("Close", on_click=filters_dialog.close)

    with ui.header().classes("items-center justify-between"):
        ui.label("Enyalie").style(
            "font-family: 'Elfic-Cursive', sans-serif; font-size: 80px;"
            "position: absolute; bottom: -0.45em; left: 0.06125em;"
            "text-shadow: 1px 1px 1px black;"
        )
        ui.space()
        with ui.button_group().props("outline"):
            ui.button(
                "Home",
                icon="home",
                color="inherit",
                on_click=lambda: handle_back_to_home(leaflet),
            ).props("outline")
            with ui.button(
                "Filters",
                icon="filter_list",
                color="inherit",
                on_click=filters_dialog.open,
            ).props("outline"):
                # ui.badge("0", color="secondary").props("floating")
                pass
            ui.button(
                "Settings",
                icon="settings",
                color="inherit",
                on_click=settings_dialog.open,
            ).props("outline")
            ui.button(
                "New path", icon="add", color="inherit", on_click=new_path_dialog.open
            ).props("outline")

    leaflet = ui.leaflet(
        center=HOME, zoom=HOME_ZOOM, options={"zoomControl": False}
    ).classes("flex-auto")


ui.run()
