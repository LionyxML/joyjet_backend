import unittest
from app import app, carts_totalize, carts_apply_delivery
import json


class PriceCase(unittest.TestCase):
    """ Test case for the application """

    def test_calculate_carts_plus_delivery(self):
        msg1 = json.loads(
            """{
              "articles": [
                { "id": 1, "name": "water", "price": 100 },
                { "id": 2, "name": "honey", "price": 200 },
                { "id": 3, "name": "mango", "price": 400 },
                { "id": 4, "name": "tea", "price": 1000 },
                { "id": 5, "name": "ketchup", "price": 999 },
                { "id": 6, "name": "mayonnaise", "price": 999 },
                { "id": 7, "name": "fries", "price": 378 },
                { "id": 8, "name": "ham", "price": 147 }
              ],
              "carts": [
                {
                  "id": 1,
                  "items": [
                    { "article_id": 1, "quantity": 6 },
                    { "article_id": 2, "quantity": 2 },
                    { "article_id": 4, "quantity": 1 }
                  ]
                },
                {
                  "id": 2,
                  "items": [
                    { "article_id": 2, "quantity": 1 },
                    { "article_id": 3, "quantity": 3 }
                  ]
                },
                {
                  "id": 3,
                  "items": [
                    { "article_id": 5, "quantity": 1 },
                    { "article_id": 6, "quantity": 1 }
                  ]
                },
                {
                  "id": 4,
                  "items": [
                    { "article_id": 7, "quantity": 1 }
                  ]
                },
                {
                  "id": 5,
                  "items": [
                    { "article_id": 8, "quantity": 3 }
                  ]
                }
              ],
              "delivery_fees": [
                {
                  "eligible_transaction_volume": {
                    "min_price": 0,
                    "max_price": 1000
                  },
                  "price": 800
                },
                {
                  "eligible_transaction_volume": {
                    "min_price": 1000,
                    "max_price": 2000
                  },
                  "price": 400
                },
                {
                  "eligible_transaction_volume": {
                    "min_price": 2000,
                    "max_price": null
                  },
                  "price": 0
                }
              ],
              "discounts": [
                { "article_id": 2, "type": "amount", "value": 25 },
                { "article_id": 5, "type": "percentage", "value": 30 },
                { "article_id": 6, "type": "percentage", "value": 30 },
                { "article_id": 7, "type": "percentage", "value": 25 },
                { "article_id": 8, "type": "percentage", "value": 10 }
              ]
            }"""
        )
        resp1 = {
            "carts": [
                {"id": 1, "total": 2350},
                {"id": 2, "total": 1775},
                {"id": 3, "total": 1798.6},
                {"id": 4, "total": 1083.5},
                {"id": 5, "total": 1196.9},
            ]
        }

        msg2 = json.loads(
            """{
              "articles": [
                { "id": 1, "name": "water", "price": 100 },
                { "id": 2, "name": "honey", "price": 200 },
                { "id": 3, "name": "mango", "price": 400 },
                { "id": 4, "name": "tea", "price": 1000 },
                { "id": 5, "name": "ketchup", "price": 999 },
                { "id": 6, "name": "mayonnaise", "price": 999 },
                { "id": 7, "name": "fries", "price": 378 },
                { "id": 8, "name": "ham", "price": 147 }
              ],
              "carts": [
                {
                  "id": 1,
                  "items": [
                    { "article_id": 1, "quantity": 63 },
                    { "article_id": 2, "quantity": 21 },
                    { "article_id": 4, "quantity": 1 }
                  ]
                },
                {
                  "id": 2,
                  "items": [
                    { "article_id": 2, "quantity": 10 },
                    { "article_id": 4, "quantity": 32 }
                  ]
                },
                {
                  "id": 3,
                  "items": [
                    { "article_id": 5, "quantity": 1 },
                    { "article_id": 6, "quantity": 1 }
                  ]
                },
                {
                  "id": 4,
                  "items": [
                    { "article_id": 7, "quantity": 53 }
                  ]
                },
                {
                  "id": 5,
                  "items": [
                    { "article_id": 8, "quantity": 3 }
                  ]
                }
              ],
              "delivery_fees": [
                {
                  "eligible_transaction_volume": {
                    "min_price": 0,
                    "max_price": 1000
                  },
                  "price": 800
                },
                {
                  "eligible_transaction_volume": {
                    "min_price": 1000,
                    "max_price": 2000
                  },
                  "price": 400
                },
                {
                  "eligible_transaction_volume": {
                    "min_price": 2000,
                    "max_price": null
                  },
                  "price": 0
                }
              ],
              "discounts": [
                { "article_id": 2, "type": "amount", "value": 25 },
                { "article_id": 5, "type": "percentage", "value": 30 },
                { "article_id": 6, "type": "percentage", "value": 30 },
                { "article_id": 7, "type": "percentage", "value": 25 },
                { "article_id": 8, "type": "percentage", "value": 10 }
              ]
            }"""
        )

        resp2 = {
            "carts": [
                {"id": 1, "total": 10975},
                {"id": 2, "total": 33750},
                {"id": 3, "total": 1798.6},
                {"id": 4, "total": 15025.5},
                {"id": 5, "total": 1196.9},
            ]
        }

        self.assertEqual(
            carts_apply_delivery(carts_totalize(msg1), msg1["delivery_fees"]), resp1
        )
        self.assertEqual(
            carts_apply_delivery(carts_totalize(msg2), msg2["delivery_fees"]), resp2
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
