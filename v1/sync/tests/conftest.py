import pytest
from faker import Faker
from thenewboston.utils.signed_requests import generate_signed_request


@pytest.fixture
def block_identifier():
    yield Faker().pystr(max_chars=BLOCK_IDENTIFIER_LENGTH)


@pytest.fixture
def signed_confirmation_block_history_request(validator, block_identifier):
    yield generate_signed_request(
        data={
            'block_identifier': block_identifier,
        },
        nid_signing_key=validator.node_identifier,
    )
