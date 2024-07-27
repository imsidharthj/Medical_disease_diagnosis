import csv
from django.core.management.base import BaseCommand
from diagnosis_app.models import Disease, Symptom

class Command(BaseCommand):
    help = 'Load disease data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            for row in csv_reader:
                disease_name = row[0]
                disease, created = Disease.objects.get_or_create(name=disease_name)
                for symptom_name in row[1:]:
                    Symptom.objects.get_or_create(disease=disease, name=symptom_name.strip())
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
