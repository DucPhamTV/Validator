from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK


def test_confirmation_block_history_post(client, signed_confirmation_block_history_request):
    response = client.post_json(
        reverse('confirmation_block_history-list'),
        signed_confirmation_block_history_request,
        expected=HTTP_200_OK,
    )
    assert response == signed_confirmation_block_history_request
