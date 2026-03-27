import allure
import logging
from functools import wraps

# 🔹 Step decorator (AUTO step creation)
def allure_step(step_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with allure.step(step_name):
                return func(*args, **kwargs)
        return wrapper
    return decorator


# 🔹 Attach JSON safely
def attach_json(name, data):
    allure.attach(
        str(data),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )


# 🔹 Logging wrapper
def log_info(message):
    logging.info(message)