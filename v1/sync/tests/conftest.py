import pytest
from thenewboston.utils.signed_requests import generate_signed_request


@pytest.fixture
def signed_confirmation_block_history_request(validator, signing_key, confirmation_validator_configuration):
    yield generate_signed_request(
        data={
            'block_identifier': confirmation_validator_configuration.root_account_file_hash,
        },
        nid_signing_key=signing_key,
    )
