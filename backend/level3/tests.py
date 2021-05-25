import unittest
from app import app, carts_totalize, carts_apply_delivery


class PriceCase(unittest.TestCase):
    """ Test case for the application """
    def test_calculate_carts_plus_delivery(self):
        msg1 = {
              "articles": [
                { "id": 1, "name": "water", "price": 100 },
                { "id": 2, "name": "honey", "price": 200 },
                { "id": 3, "name": "mango", "price": 400 },
                { "id": 4, "name": "tea", "price": 1000 }
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
                  "items": []
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
                    "max_price": None
                  },
                  "price": 0
                }
              ]
            }
        resp1 = {
              "carts": [
                {
                  "id": 1,
                  "total": 2000
                },
                {
                  "id": 2,
                  "total": 1800
                },
                {
                  "id": 3,
                  "total": 800
                }
              ]
            }

        msg2 = {
        "articles": [
                { "id": 1, "name": "water", "price": 100 },
                { "id": 2, "name": "honey", "price": 200 },
                { "id": 3, "name": "mango", "price": 400 },
                { "id": 4, "name": "tea", "price": 1000 }
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
                  "items": []
                }
              ],
              "delivery_fees": [
                {
                  "eligible_transaction_volume": {
                    "min_price": 0,
                    "max_price": 500
                  },
                  "price": 80
                },
                {
                  "eligible_transaction_volume": {
                    "min_price": 500,
                    "max_price": 2000
                  },
                  "price": 40
                },
                {
                  "eligible_transaction_volume": {
                    "min_price": 2000,
                    "max_price": 20200
                  },
                  "price": 30
                }
              ]
            }

        resp2 = {
              "carts": [
                {
                  "id": 1,
                  "total": 2030
                },
                {
                  "id": 2,
                  "total": 1440
                },
                {
                  "id": 3,
                  "total": 80
                }
              ]
            }


        self.assertEqual(carts_apply_delivery(carts_totalize(msg1), msg1["delivery_fees"]), resp1)
        self.assertEqual(carts_apply_delivery(carts_totalize(msg2), msg2["delivery_fees"]), resp2)


if __name__ == '__main__' :
    unittest.main(verbosity=2)
