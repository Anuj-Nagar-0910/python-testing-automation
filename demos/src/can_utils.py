#can_utils.py

def validate_message(msg, expected_id, expected_data):
    if msg is None:
        return False

    return (
        msg.arbitration_id == expected_id and
        list(msg.data) == expected_data
    )