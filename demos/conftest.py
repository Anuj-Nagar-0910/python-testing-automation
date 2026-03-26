#conftest.py

import sys
import os
import logging
import pytest
import pytest_html
from pytest_html import extras

sys.path.append(os.path.abspath("."))

# ---------------- LOGGING SETUP ----------------
log_file = "logs/test_log.txt"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Enable log display in pytest report
def pytest_configure(config):
    config.option.log_cli = True
    config.option.log_cli_level = "INFO"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        extra = getattr(report, "extras", [])

        if hasattr(item, "test_data"):
            data = item.test_data

            formatted = f"""
            <div style="padding:10px; border:1px solid #ccc; border-radius:5px;">
                <h4 style="color:blue;">Test Data</h4>
                <b>Input:</b> {data['Input']}<br>
                <b>Expected:</b> {data['Expected']}<br>
                <b>Actual:</b> {data['Actual']}<br>
            </div>
            """

            extra.append(pytest_html.extras.html(formatted))

        report.extras = extra