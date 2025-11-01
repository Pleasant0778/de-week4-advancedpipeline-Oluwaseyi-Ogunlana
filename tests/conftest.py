
import pandas as pd
import numpy as np
import pytest
from pipeline.api_client import ApiClient
from pipeline.data_enricher import DataEnricher
from pipeline.data_analyzer import DataAnalyzer

@pytest.fixture
def products_user_df():
    product_data = [
        {"id": 1, "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", "price": 109.95, "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday", "category": "men's clothing", "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png", "rating": {"rate": 3.9, "count": 120}}, 
        {"id": 2, "title": "Mens Casual Premium Slim Fit T-Shirts ", "price": 22.3, "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.", "category": "men's clothing", "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png", "rating": {"rate": 4.1, "count": 259}}, 
        {"id": 3, "title": "Mens Cotton Jacket", "price": 55.99, "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.", "category": "men's clothing", "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png", "rating": {"rate": 4.7, "count": 500}}, 
        {"id": 4, "title": "Mens Casual Slim Fit", "price": 15.99, "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.", "category": "men's clothing", "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_t.png", "rating": {"rate": 2.1, "count": 430}}, 
        {"id": 5, "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet", "price": 695, "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.", "category": "jewelery", "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_t.png", "rating": {"rate": 4.6, "count": 400}}
                    ]

    user_data= [
        {"address": {"geolocation": {"lat": "-37.3159", "long": "81.1496"}, "city": "kilcoole", "street": "new road", "number": 7682, "zipcode": "12926-3874"}, "id": 1, "email": "john@gmail.com", "username": "johnd", "password": "m38rmF$", "name": {"firstname": "john", "lastname": "doe"}, "phone": "1-570-236-7033", "__v": 0},
        {"address": {"geolocation": {"lat": "-37.3159", "long": "81.1496"}, "city": "kilcoole", "street": "Lovers Ln", "number": 7267, "zipcode": "12926-3874"}, "id": 2, "email": "morrison@gmail.com", "username": "mor_2314", "password": "83r5^_", "name": {"firstname": "david", "lastname": "morrison"}, "phone": "1-570-236-7033", "__v": 0},
        {"address": {"geolocation": {"lat": "40.3467", "long": "-30.1310"}, "city": "Cullman", "street": "Frances Ct", "number": 86, "zipcode": "29567-1452"}, "id": 3, "email": "kevin@gmail.com", "username": "kevinryan", "password": "kev02937@", "name": {"firstname": "kevin", "lastname": "ryan"}, "phone": "1-567-094-1345", "__v": 0}, 
        {"address": {"geolocation": {"lat": "50.3467", "long": "-20.1310"}, "city": "San Antonio", "street": "Hunters Creek Dr", "number": 6454, "zipcode": "98234-1734"}, "id": 4, "email": "don@gmail.com", "username": "donero", "password": "ewedon", "name": {"firstname": "don", "lastname": "romer"}, "phone": "1-765-789-6734", "__v": 0}, 
        {"address": {"geolocation": {"lat": "40.3467", "long": "-40.1310"}, "city": "san Antonio", "street": "adams St", "number": 245, "zipcode": "80796-1234"}, "id": 5, "email": "derek@gmail.com", "username": "derek", "password": "jklg*_56", "name": {"firstname": "derek", "lastname": "powell"}, "phone": "1-956-001-1945", "__v": 0}
      ]
    product_data_edge = [
        {"id": 1, "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", "price": 109.95, "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday", "category": "men's clothing", "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png", "rating": {"rate": 3.9, "count": 120}}, 
        {"id": 2, "title": "Mens Casual Premium Slim Fit T-Shirts ", "price": 22.3, "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.", "category": "men's clothing", "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png", "rating": {"rate": 4.1, "count": 259}}, 
        {"id": 3, "title": "Mens Cotton Jacket", "price": 55.99, "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.", "category": "men's clothing", "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png", "rating": {"rate": 4.7, "count": 500}}, 
        {"id": 4, "title": "Mens Casual Slim Fit", "price": 15.99, "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.", "category": "men's clothing", "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_t.png", "rating": {"rate": 2.1, "count": 430}}, 
        {"id": 5, "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet", "price": 695, "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.", "category": "jewelery", "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_t.png", "rating": {"rate": 4.6, "count": 400}},
        {"id": 6, "title": "Solid Gold Petite Micropave ", "price": 168, "description": "Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.", "category": "jewelery", "image": "https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_t.png", "rating": {"rate": 3.9, "count": 70}}            
                    ]
    return [

        pd.DataFrame(product_data), pd.DataFrame(user_data) ,pd.DataFrame(product_data_edge) 
    ]

@pytest.fixture
def omnicart_classes():
    return [ ApiClient() , DataEnricher(), DataAnalyzer()]
