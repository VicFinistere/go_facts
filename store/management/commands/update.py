"""
Cron task to update products in database
"""
import requests
from django.core.management.base import BaseCommand
# from django.core.management.base import CommandError
# from polls.models import Question as Poll
import logging
from store import logic
from store.models import Product


class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(self, *args, **options):
        """
        Weekly Products Updates
        """
        logging.info("We will update products in database !")
        products = Product.objects.all()
        logging.info("There is {}".format(products.count()))

        for product in products:
            code = product.code
            # logging.info("Getting {}".format(code))

            try:
                product.delete()
                # logging.info("Deleting succeed !...")

                try:
                    page = "https://world.openfoodfacts.org/api/v0/product/{}.json".format(code)
                    data = requests.get(page).json()

                    if data:
                        if data['product']:
                            product = data['product']
                            try:
                                product_array = logic.fetch_product_array(product)

                                if product_array is not None:
                                    logic.save_product(product_array)
                                else:
                                    pass
                                    # logging.info('Getting product array failed...')

                            except IndexError:
                                pass
                                # logging.info('Updating product have failed...')
                        else:
                            pass
                            # logging.info('No product found with the code {} ...'.format(code))
                    else:
                        pass
                        # logging.info('Getting product page failed...')

                except ValueError:
                    pass
                    # logging.info("The product has been removed...")

            except ValueError:
                pass
                # logging.info("Deleting failed !...")

        logging.info('Exit the update process')
