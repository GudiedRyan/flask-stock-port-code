import pytest
from flask import current_app
from project import create_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask appl config made for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            current_app.logger.info('In the test_client() fixture...')
        
        yield testing_client