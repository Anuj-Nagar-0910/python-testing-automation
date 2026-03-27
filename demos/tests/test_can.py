# import pytest
# import logging
# from ..src.can_interface import setup_can, send_message, receive_message
#
# @pytest.fixture
# def can_bus():
#     bus = setup_can()
#     yield bus
#     bus.shutdown()
#
# def test_can_message(can_bus, request):
#     logging.info("===== TEST STARTED =====")
#
#     # INPUT
#     input_msg = {"id": 0x123, "data": [1, 2, 3, 4]}
#     logging.info(f"Input: {input_msg}")
#
#     # EXPECTED
#     expected = input_msg
#     logging.info(f"Expected: {expected}")
#
#     # ACTION
#     send_message(can_bus)
#     msg = receive_message(can_bus)
#
#     # ACTUAL
#     actual = None
#     if msg:
#         actual = {"id": msg.arbitration_id, "data": list(msg.data)}
#
#     logging.info(f"Actual: {actual}")
#
#     # 👉 Attach structured data for report
#     request.node.test_data = {
#         "Input": input_msg,
#         "Expected": expected,
#         "Actual": actual
#     }
#
#     # ASSERTIONS
#     assert msg is not None
#     assert msg.arbitration_id == expected["id"]
#     if msg.arbitration_id == expected["id"]:
#         logging.info("Verdict: PASS - arbitration_id matches")
#     else:
#         logging.error(f"Verdict: FAIL - expected {expected['id']}, got {msg.arbitration_id}")
#         assert False, "arbitration_id mismatch"
#     assert list(msg.data) == expected["data"]
#
#     logging.info("Verdict: PASS")

"""Reporting with Allure"""
import pytest
import logging
import allure

from ..src.can_interface import setup_can, send_message, receive_message
from ..src.allure_helper import allure_step, attach_json, log_info


@pytest.fixture
def can_bus():
    bus = setup_can()
    yield bus
    bus.shutdown()


@allure.feature("CAN Communication")
@allure.story("Validate CAN Message")
@allure.severity(allure.severity_level.CRITICAL)
def test_can_message(can_bus):

    input_msg = {"id": 0x123, "data": [1, 2, 3, 4]}

    prepare_input(input_msg)
    send_can(can_bus, input_msg)
    msg = receive_can(can_bus)
    validate(msg, input_msg)

@allure.story("Multiple CAN Messages")
@pytest.mark.parametrize("input_msg", [
    {"id": 0x100, "data": [1, 2]},
    {"id": 0x200, "data": [3, 4]},
    {"id": 0x300, "data": [5, 6]},
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