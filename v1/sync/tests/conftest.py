import pytest
from thenewboston.utils.signed_requests import generate_signed_request


@pytest.fixture
def signed_confirmation_block_history_request(validator, signing_key, initial_block_identifier):
    yield generate_signed_request(
        data={
            'block_identifier': initial_block_identifier
        },
        nid_signing_key=signing_key,
    )
