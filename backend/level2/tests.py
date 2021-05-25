import unittest
from app import app, carts_total


class PriceCase(unittest.TestCase):
    """ Test case for the application """
    def test_calculate_carts(self):
        resp = {"carts": []}
        msg1 = {
              "articles": [
                { "id": 1, "name": "water", "price": 150 },
                { "id": 2, "name": "honey", "price": 200 },
                { "id": 3, "name": "mango", "price": 300 },
                { "id": 4, "name": "tea", "price": 1000 }
              ],
              "carts": [
                {
                  "id": 1,
                  "items": [
                    { "article_id": 1, "quantity": 6 },
                    { "article_id": 2, "quantity": 4 },
                    { "article_id": 4, "quantity": 1 }
                  ]
                },
                {
                  "id": 2,
                  "items": [
                    { "article_id": 2, "quantity": 1 },
                    { "article_id": 3, "quantity": 8 }
                  ]
                },
                {
                  "id": 3,
                  "items": []
                }
              ]
            }
        resp1 = {"carts":[{"id":1,"total":2700},{"id":2,"total":2600},{"id":3,"total":0}]}

        msg2 = {
              "articles": [
                { "id": 1, "name": "water", "price": 130 },
                { "id": 2, "name": "honey", "price": 250 },
                { "id": 3, "name": "mango", "price": 300 },
                { "id": 4, "name": "tea", "price": 1000 }
              ],
              "carts": [
                {
                  "id": 1,
                  "items": [
                    { "article_id": 1, "quantity": 100 },
                    { "article_id": 2, "quantity": 330 },
                    { "article_id": 4, "quantity": 1 }
                  ]
                },
                {
                  "id": 2,
                  "items": [
                    { "article_id": 2, "quantity": 1 },
                    { "article_id": 3, "quantity": 98 }
                  ]
                },
                {
                  "id": 3,
                  "items": [
                    { "article_id": 4, "quantity": 10 },
                    { "article_id": 2, "quantity": 1 }
                  ]
                }
              ]
            }

        resp2 = {"carts":[{"id":1,"total":96500},{"id":2,"total":29650},{"id":3,"total":10250}]}

        msg3 = {
              "articles": [
                { "id": 1, "name": "water", "price": 130 },
                { "id": 2, "name": "honey", "price": 250 },
                { "id": 3, "name": "mango", "price": 300 },
                { "id": 4, "name": "tea", "price": 1000 }
              ],
              "carts": [
                {
                  "id": 1,
                  "items": [
                    { "article_id": 1, "quantity": 100 },
                    { "article_id": 2, "quantity": 330 },
                    { "article_id": 4, "quantity": 1 }
                  ]
                },
                {
                  "id": 2,
                  "items": [
                    { "article_id": 2, "quantity": 1 },
                    { "article_id": 3, "quantity": 98 }
                  ]
                },
                {
                  "id": 3,
                  "items": [
                    { "article_id": 4, "quantity": 10 },
                    { "article_id": 2, "quantity": 9 }
                  ]
                }
              ]
            }

        resp3 = {"carts":[{"id":1,"total":96500},{"id":2,"total":29650},{"id":3,"total":12250}]}

        self.assertEqual(carts_total(msg1, {"carts": []}), resp1)
        self.assertEqual(carts_total(msg2, {"carts": []}), resp2)
        self.assertEqual(carts_total(msg3, {"carts": []}), resp3)



if __name__ == '__main__':
    unittest.main(verbosity=2)
