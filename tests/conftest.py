from datetime import datetime

import pytest
import json
from pathlib import Path

from requests import session

from utils.auth_helper import *
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def config():
    path = Path(__file__).resolve().parent.parent / "config/config.json"
    with open (path) as f:
        return json.load(f)

@pytest.fixture(scope="session")
def check_inDate():
    return get_checkIndate()

@pytest.fixture(scope="session")
def check_outDate():
    return get_checkOutdate()

@pytest.fixture(scope="session")
def get_Token(config):
    return get_authentication(config)

@pytest.fixture(scope="session")
def api_client(config):
    return APIClient(config['base_url'])


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

