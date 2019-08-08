from django.core.management.base import BaseCommand, CommandError
import csv
from fileUpload.serializer import HouseSerializer
from fileUpload.utils.mathematics import numerize
from datetime import datetime


class Command(BaseCommand):
    help = 'Ingest CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        ingestedFile = options['file']

        with open(ingestedFile) as csvFile:
            csvReader = csv.DictReader(csvFile)
            line = 0
            for row in csvReader:
                line += 1
                for colv in csvReader.fieldnames:
                    if(row[colv] == ""):
                        row[colv] = None
                    if(row[colv] != None):
                        if(colv == 'price'):
                            row['price'] = numerize((row['price'])[1:])
                        if(colv == 'last_sold_date'):
                            row['last_sold_date'] = datetime.strptime(
                                row['last_sold_date'], "%m/%d/%Y").strftime('%Y-%m-%d')
                        if(colv == 'rentzestimate_last_updated'):
                            row['rentzestimate_last_updated'] = datetime.strptime(
                                row['rentzestimate_last_updated'], "%m/%d/%Y").strftime('%Y-%m-%d')
                        if(colv == 'zestimate_last_updated'):
                            row['zestimate_last_updated'] = datetime.strptime(
                                row['zestimate_last_updated'], "%m/%d/%Y").strftime('%Y-%m-%d')
                serializer = HouseSerializer(data=row)
                if serializer.is_valid():
                    serializer.save()
                if not serializer.is_valid():
                    print(serializer.error())
        self.stdout.write(str(line) + "records where successfly inputted")
