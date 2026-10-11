"""DM-S3519 preset and safety policy tests (no CAN interface is opened)."""

import pytest

from damiao_motor.core.motor import DaMiaoMotor, MOTOR_TYPE_PRESETS


def _motor():
    return DaMiaoMotor(
        motor_id=1,
        feedback_id=0,
        bus=None,
        motor_type="DM3519",
    )


def test_dm3519_mapping_limits_match_read_registers():
    assert MOTOR_TYPE_PRESETS["DM3519"] == {
        "p_min": -12.5,
        "p_max": 12.5,
        "v_min": -200,
        "v_max": 200,
        "t_min": -10,
        "t_max": 10,
    }


def test_dm3519_supports_only_documented_modes():
    assert _motor().supported_control_modes() == ("MIT", "POS_VEL", "VEL")


def test_dm3519_force_pos_is_rejected_before_bus_access():
    with pytest.raises(ValueError, match="not documented"):
        _motor().send_cmd_force_pos()


def test_dm3519_mit_encoder_uses_full_mapping_ranges():
    motor = _motor()
    assert motor.encode_cmd_msg(12.5, 200, 10, 500, 5) == b"\xff\xff\xff\xff\xff\xff\xff\xff"
