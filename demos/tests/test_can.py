#test_can.py
"""Reporting with Allure"""
import pytest
import allure

from ..src.can_interface import setup_can, send_message, receive_message
from ..src.allure_helper import allure_step, attach_json, log_info


@pytest.fixture
def can_bus():
    bus = setup_can()
    yield bus
    bus.shutdown()


@allure.story("Multiple CAN Messages")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("input_msg", [
    {"id": 0x123, "data": [1, 2, 3, 4]},
    {"id": 0x200, "data": [3, 4]},
    {"id": 0x300, "data": [9, 5, 6]},
    {"id": 0x400, "data": [11, 5, 6]},
    {"id": 0x312, "data": [5, 2, 6]},
    {"id": 0x3C1, "data": [1, 5, 6]},
    {"id": 0x3B2, "data": [5, 7, 6]},
    {"id": 0x3A3, "data": [56, 6, ]},
    {"id": 0x400, "data": [5, 65, "0xf"]},
    {"id": 0x110, "data": [5, 64]},
    {"id": 0x310, "data": [5, 36]},
    {"id": 0x392, "data": [52, 6]},
    {"id": 0xfff, "data": [15, 6]},
])
def test_multiple_messages(can_bus, input_msg):

    prepare_input(input_msg)
    send_can(can_bus, input_msg)
    msg = receive_can(can_bus)
    validate(msg, input_msg)

# ---------- STEPS (REUSABLE) ----------

@allure_step("Prepare input data")
def prepare_input(input_msg):
    attach_json("Input Data", input_msg)
    log_info(f"Input: {input_msg}")


@allure_step("Send CAN message")
def send_can(bus, input_msg):
    send_message(bus, input_msg["id"], input_msg["data"])
    log_info("Message sent")


@allure_step("Receive CAN message")
def receive_can(bus):
    msg = receive_message(bus)
    log_info(f"Received: {msg}")
    return msg


@allure_step("Validate CAN message")
def validate(msg, expected):

    assert msg is not None, "No message received"

    if msg.arbitration_id == expected["id"]:
        log_info("PASS: arbitration_id matches")
    else:
        log_info("FAIL: arbitration_id mismatch")
        assert False, "arbitration_id mismatch"

    assert list(msg.data) == expected["data"]

    attach_json("Validation Result", {
        "message": str(msg)
    })