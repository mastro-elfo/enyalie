from nicegui import ui

HOME = (43.575, 10.775)
HOME_ZOOM = 13
PRIMARY = "#482880"
SECONDARY = "#4caf50"
ACCENT = "#111B1E"
POSITIVE = "#53B689"
NEGATIVE = "#c10015"
INFO = "#31ccec"
WARNING = "#f2c037"


def edit_path():
    ui.dark_mode(value=True)
    ui.colors(primary=PRIMARY, secondary=SECONDARY, accent=ACCENT, positive=POSITIVE)
    ui.query(".nicegui-content").classes("absolute top-0 bottom-0 left-0 right-0 p-0")
    ui.add_head_html(
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Monsieur+La+Doulaise&family=Tangerine:wght@400;700&display=swap" rel="stylesheet">'
    )

    with ui.header().classes("items-center justify-between"):
        ui.label("Enyalie").style(
            'font-family: "Tangerine", Arial, sans-serif; font-size: 80px;'
            "position: absolute; bottom: -0.45em; left: 0.06125em;"
            "text-shadow: 1px 1px 1px black;"
        )
        ui.space()
        with ui.button_group().props("outline"):
            ui.button(
                "Home",
                icon="home",
                color="inherit",
                on_click=ui.navigate.back,
            ).props("outline")
