"""
This file handle weekly products update
"""
import logging
from store.models import Product
from store import logic


def update_database():
    """
    Update database
    :return:
    """

    products = Product.objects.all()

    for product in products:
        code = product.code
        product.delete()
        logic.get_product(code)


if __name__ == '__main__':
    logging.info('Updating database products !')
    update_database()