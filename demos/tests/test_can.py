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

@pytest.fixture
def can_bus():
    bus = setup_can()
    yield bus
    bus.shutdown()

@allure.feature("CAN Communication")
@allure.story("Validate CAN Message")
@allure.severity(allure.severity_level.CRITICAL)
def test_can_message(can_bus):
    logging.info("===== TEST STARTED =====")

    with allure.step("Prepare input data"):
        input_msg = {"id": 0x123, "data": [1, 2, 3, 4]}
        allure.attach(
            str(input_msg),
            name="Input Data",
            attachment_type=allure.attachment_type.JSON
        )
        logging.info(f"Input: {input_msg}")

    with allure.step("Send CAN message"):
        send_message(can_bus)
        logging.info(f"Send CAN message: {can_bus}")

    with allure.step("Receive CAN message"):
        msg = receive_message(can_bus)
        logging.info(f"Receive CAN message: {msg}")

    with allure.step("Validate message"):
        assert msg is not None
        # assert msg.arbitration_id == input_msg["id"]
        if msg.arbitration_id == input_msg["id"]:
            logging.info("Verdict: PASS - arbitration_id matches")
        else:
            logging.error(f"Verdict: FAIL - expected {input_msg['id']}, got {msg.arbitration_id}")
            assert False, "arbitration_id mismatch"
        assert list(msg.data) == input_msg["data"]
        allure.attach(
            str(msg),
            name="Validation Evidence",
            attachment_type=allure.attachment_type.JSON
        )
