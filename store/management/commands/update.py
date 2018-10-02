"""
Cron task to update products in database
"""
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

        for product in products:
            code = product.code
            logging.info("Getting {}".format(code))

            try:
                product.delete()
                logging.info("Deleting succeed !...")

                try:
                    logic.get_product(code)
                    logging.info("Product has been updated !")

                except ValueError:
                    logging.info("The product has been removed...")

            except ValueError:
                logging.info("Deleting failed !...")

