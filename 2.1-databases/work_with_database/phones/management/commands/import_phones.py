import csv
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='phones.csv')

    def handle(self, *args, **options):
        Phone.objects.all().delete()
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for row in phones:
            name = row['name']

            new_slug = slugify(name)


            Phone.objects.create(
                name=name,
                slug=new_slug,
                price=row['price'],
                image=row['image'],
                release_date=row['release_date'],
                lte_exists=row['lte_exists']
            )
        self.stdout.write(self.style.SUCCESS('Импорт успешно завершён!'))
