import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from dash.testing.application_runners import import_app


def test_header_exists(dash_duo):
    app = import_app("data.app")
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Sales Dashboard"


def test_graph_exists(dash_duo):
    app = import_app("data.app")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_radio_buttons_exist(dash_duo):
    app = import_app("data.app")
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None