from nicegui import ui

from pack import fs
from pack.db import Database

HOME = (43.575, 10.775)
HOME_ZOOM = 13
PRIMARY = "#482880"
SECONDARY = "#4caf50"
ACCENT = "#111B1E"
POSITIVE = "#53B689"
NEGATIVE = "#c10015"
INFO = "#31ccec"
WARNING = "#f2c037"

database = Database("./APPDATA")


@ui.page("/")
def dashboard():
    ui.dark_mode(value=True)
    ui.colors(primary=PRIMARY, secondary=SECONDARY, accent=ACCENT, positive=POSITIVE)
    ui.query(".nicegui-content").classes("absolute top-0 bottom-0 left-0 right-0 p-0")
    ui.add_head_html(
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Monsieur+La+Doulaise&family=Tangerine:wght@400;700&display=swap" rel="stylesheet">'
    )

    config = database.get_config()

    def handle_back_to_home(leaflet):
        leaflet.set_center(HOME)
        leaflet.set_zoom(HOME_ZOOM)

    with ui.dialog() as new_path_dialog, ui.card():
        ui.label("New path").style("font-size: 2em;")
        ui.button("Close", on_click=new_path_dialog.close)

    with ui.dialog() as settings_dialog, ui.card():
        ui.label("Settings").style("font-size: 2em;")
        with ui.grid(columns=2):
            ui.input(
                "Path dir",
                validation={"Not a directory": fs.is_directory},
                value=config.get("pathdir", ""),
                on_change=lambda value: database.set_config("pathdir", value.value),
            )
        ui.separator()
        with ui.element().classes("flex flex-row w-full"):
            ui.space()
            ui.button("Close", on_click=settings_dialog.close)

    with ui.dialog() as filters_dialog, ui.card():
        ui.label("Filters").style("font-size: 2em;")
        ui.button("Close", on_click=filters_dialog.close)

    with ui.header().classes("items-center justify-between"):
        ui.label("Enyalie").style(
            'font-family: "Tangerine", Arial, sans-serif; font-size: 80px;'
            "position: absolute; bottom: -0.45em; left: 0.06125em;"
            "text-shadow: 1px 1px 1px black;"
        )
        ui.space()

        connected = database.is_connected()
        with ui.icon(
            "power" if connected else "power_off",
            size="1.2em",
            color="positive" if connected else "negative",
        ):
            ui.tooltip("Connected to db" if connected else "Disconnected from db")

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

    for path in database.get_all_paths():
        leaflet.generic_layer(
            name="polyline",
            args=[fs.get_trkpts_from_file(path["file"]), {"color": "red"}],
        )


def main():
    ui.run(title="Enyalie")


if __name__ in {"__main__", "__mp_main__"}:
    main()
