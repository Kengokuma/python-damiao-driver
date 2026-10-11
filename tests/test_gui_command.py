"""CLI GUI routing tests; no server or CAN interface is opened."""

from types import SimpleNamespace
from unittest.mock import patch

from damiao_motor.cli.commands import cmd_gui


def test_gui_command_launches_legacy_control_ui():
    args = SimpleNamespace(
        host="127.0.0.1", port=5000, debug=False, production=False
    )

    with patch("damiao_motor.gui.web_gui.run_server") as run_server:
        cmd_gui(args)

    run_server.assert_called_once_with(
        host="127.0.0.1", port=5000, debug=False, production=False
    )
