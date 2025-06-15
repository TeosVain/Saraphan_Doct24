from datetime import datetime
import io

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.authtoken.models import Token
from PIL import Image

from goods.models import Goods, Category, Subcategory


today = datetime.today()
COMMENT_TEXT = 'Текст комментария'


@pytest.fixture
def fake_image():
    file = io.BytesIO()
    image = Image.new('RGB', (100, 100), color='red')
    image.save(file, 'JPEG')
    file.seek(0)
    return SimpleUploadedFile(
        'test.jpg', file.read(), content_type='image/jpeg'
    )


@pytest.fixture(autouse=True)
def temp_media_root(tmp_path, settings):
    """Переназначаем MEDIA_ROOT на временную директорию для всех тестов."""
    settings.MEDIA_ROOT = tmp_path


@pytest.fixture
def author_token(django_user_model):
    user = django_user_model.objects.create_user(
        username='Автор', password='12345678'
    )
    token, _ = Token.objects.get_or_create(user=user)
    return token.key


@pytest.fixture
def author_client(author_token):
    client = Client()
    client.defaults['HTTP_AUTHORIZATION'] = f'Token {author_token}'
    return client


@pytest.fixture
def not_author(django_user_model):
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def one_category(fake_image):
    return Category.objects.create(
        name='Категория',
        slug='cat',
        image=fake_image
    )

@pytest.fixture
def one_subcategory(one_category, fake_image):
    return Subcategory.objects.create(
        name='Подкатегория',
        slug='subcat',
        image=fake_image,
        category=one_category
    )


@pytest.fixture
def goods_objects(one_subcategory, fake_image):

    goods1 = Goods.objects.create(
        name='Товар 1',
        slug='goods-1',
        image=fake_image,
        text='Описание товара 1',
        subcategory=one_subcategory,
        price=100
    )

    goods2 = Goods.objects.create(
        name='Товар 2',
        slug='goods-2',
        image=fake_image,
        text='Описание товара 2',
        subcategory=one_subcategory,
        price=200
    )

    return [goods1, goods2]


@pytest.fixture
def goods_url():
    return reverse('api:goods-list')


@pytest.fixture
def cart_url():
    return reverse('api:cartgoods-list')

@pytest.fixture
def cart_detail_url(pk):
    return reverse('api:cartgoods-detail', args=[pk])