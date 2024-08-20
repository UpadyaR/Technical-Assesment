from django.core.management.base import BaseCommand
import csv
from website.models import Ganison_dataset_1

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def handle(self, *args, **kwargs):
        with open('Ganison_dataset/Ganison_dataset_1.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Ganison_dataset_1.objects.create(**row)
        
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))