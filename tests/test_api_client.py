import requests
import pytest
from pytest_mock import MockerFixture
from unittest.mock import patch, MagicMock



def test_api_client_pyt(omnicart_classes, mocker: MockerFixture):

    mock_get = mocker.patch('pipeline.api_client.requests.get')
    mock_get.return_value.json.side_effect  = [{
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        "rating": {"rate": 3.9, "count": 120}
        },
        {}
    ]
    

 
   
    product_data = list(omnicart_classes[0].get_all_products('products',
        'https://fakestoreapi.com/',
        '1'
    ))
 
    print(product_data)
    assert len(product_data) == 1
    assert product_data[0]['title'] == "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"
    assert mock_get.call_count == 2


@patch("pipeline.api_client.requests.get")
def test_api_client_unt(mock_get, omnicart_classes ):
    mock_response_1 = MagicMock()
    mock_response_1.status_code = 200
    mock_response_1.json.return_value = [
        {"address": {"geolocation": {"lat": "-37.3159", "long": "81.1496"}, "city": "kilcoole", "street": "new road", "number": 7682, "zipcode": "12926-3874"},
         "id": 1, 
         "email": "john@gmail.com", 
         "username": "johnd", 
         "password": "m38rmF$", 
         "name": {"firstname": "john", "lastname": "doe"}, 
         "phone": "1-570-236-7033", 
         "__v": 0}
    ]

    mock_response_2 = MagicMock()
    mock_response_2.status_code = 200
    mock_response_2.json.return_value = []

    mock_get.side_effect = [mock_response_1,mock_response_2 ]
 
    user_data = list(omnicart_classes[0].get_all_users( 'users',
        'https://fakestoreapi.com/',
        '1'
    ))
    assert len(user_data) ==  1
    assert user_data[0][0]["id"] == 1
    assert mock_get.call_count == 2



