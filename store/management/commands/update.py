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
                page = "https://world.openfoodfacts.org/api/v0/product/{}.json".format(code)
                data = requests.get(page).json()

                if data:
                    if data['product']:
                        product_page = data['product']

                        try:

                            product_array = logic.fetch_product_array(product_page)

                            if product_array is not None:
                                name, code, grade, image, categories, nutriments = product_array

                                if product.name != name:

                                    try:
                                        product.name = name
                                    except ValueError:
                                        pass

                                if product.code != code:

                                    try:
                                        product.code = code
                                    except ValueError:
                                        pass

                                if product.grade != grade:

                                    try:
                                        product.grade = grade
                                    except ValueError:
                                        pass

                                if product.image != image:

                                    try:
                                        product.image = image
                                    except ValueError:
                                        pass

                                if product.categories != categories:

                                    try:
                                        product.categories = categories
                                    except ValueError:
                                        pass

                                if product.nutriments != nutriments:

                                    try:
                                        product.nutriments = nutriments
                                    except ValueError:
                                        pass

                                product.save()

                            else:
                                pass
                                # logging.info('Product array cannot be fetched ...')

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


logging.info('Exit the update process')
