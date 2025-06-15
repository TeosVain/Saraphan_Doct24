import pytest
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_get_goods_list(author_client, goods_objects, goods_url):
    response = author_client.get(goods_url)
    assert isinstance(response.data, dict)
    assert 'results' in response.data
    assert isinstance(response.data['results'], list)
    assert len(response.data['results']) == 2


@pytest.mark.django_db
def test_get_empty_cart(author_client, cart_url):
    response = author_client.get(cart_url)
    assert isinstance(response.data, dict)
    assert response.data['results'] == []
    assert response.data['total_amount'] == 0
    assert response.data['total_price'] == 0


@pytest.mark.django_db
def test_add_to_cart(author_client, goods_objects, cart_url):
    good = goods_objects[0]
    data = {
        'good': good.id,
        'amount': 2
    }

    response = author_client.post(
        cart_url, data=data, content_type='application/json'
    )
    print(response.status_code)
    print(response.json())

    assert response.status_code in (
        status.HTTP_201_CREATED, status.HTTP_200_OK
    )
    assert response.data['good'] == good.id
    assert response.data['amount'] == 2


@pytest.mark.django_db
def test_cart_detail(author_client, goods_objects, cart_url):
    good = goods_objects[0]
    post_response = author_client.post(
        cart_url, data={'good': good.id, 'amount': 3},
        content_type='application/json'
    )

    assert post_response.status_code == status.HTTP_201_CREATED
    cart_id = post_response.data['id']

    detail_url = reverse('api:cartgoods-detail', args=[cart_id])
    get_response = author_client.get(detail_url)

    assert get_response.status_code == status.HTTP_200_OK
    assert get_response.data['good']['name'] == good.name
    assert get_response.data['good']['slug'] == good.slug
    assert get_response.data['good']['price'] == good.price
    assert get_response.data['amount'] == 3


@pytest.mark.django_db
def test_cart_list_with_items(author_client, goods_objects, cart_url):
    good1, good2 = goods_objects
    author_client.post(cart_url, data={'good': good1.id, 'amount': 2},
                       content_type='application/json')
    author_client.post(cart_url, data={'good': good2.id, 'amount': 1},
                       content_type='application/json')
    response = author_client.get(cart_url)
    assert response.status_code == status.HTTP_200_OK
    assert 'results' in response.data
    assert len(response.data['results']) == 2
    item1 = response.data['results'][0]
    item2 = response.data['results'][1]
    product_ids = {item1['good']['slug'], item2['good']['slug']}
    assert product_ids == {good1.slug, good2.slug}
    assert 'total_amount' in response.data
    assert response.data['total_amount'] == 3
    assert 'total_price' in response.data
    assert response.data['total_price'] == good1.price * 2 + good2.price * 1
