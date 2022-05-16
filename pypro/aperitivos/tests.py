import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('u2',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1>Video Aperitivo: U2</h1>')


def test_conteu_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/710132185?h=c8686e2489"')
