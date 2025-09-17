import pytest
import os
import sys

# Add the parent directory to the Python path so we can import the app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(scope="session")
def app_config():
    """Application configuration for testing."""
    return {
        'TESTING': True,
        'DEBUG': False,
        'PORT': 5000
    }
