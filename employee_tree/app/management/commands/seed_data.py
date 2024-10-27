import random
from venv import logger

from django.core.management.base import BaseCommand
from django.db import connection
from faker import Faker
from app.models import Employee, Position



MODE_REFRESH = 'refresh'
MODE_CLEAR = 'clear'

fake = Faker('ru_RU')

class Command(BaseCommand):
    help = 'seed database for testing'

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help='Mode')
        parser.add_argument('--number_of_employee', type=str, help='Number_of_employee')

    def handle(self, *args, **options):
        self.stdout.write('seeding data....')
        run_seed(self, options['mode'], options['number_of_employee'])
        self.stdout.write('DONE')

def clear_data():
    logger.info('DELETE all table data')
    with connection.constraint_checks_disabled():
        Employee.objects.all().delete()

def create_employees():
    logger.info('Creating Employees')
    salary = [200000, 150000, 100000, 60000]
    level = [1, 2, 3, 4]
    position = list(Position.objects.all().values_list('id', flat=True).exclude(id=1))
    parent = list(Employee.objects.all().values_list('id',flat=True))
    employee = Employee(
        full_name = fake.name(),
        employment = fake.date_time_this_century(),
        salary = random.choice(salary),
        level = random.choice(level),
        parent_id = random.choice(parent),
        position_id = random.choice(position)
    )
    employee.save()
    logger.info(f"{employee.full_name} created")
    return employee

def run_seed(self, mode, number_of_employee):
    #clear_data()
    if mode == MODE_CLEAR:
        return
    for i in range(int(number_of_employee)):
        create_employees()






















