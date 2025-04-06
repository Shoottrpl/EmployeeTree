import django_filters

from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    employment = django_filters.RangeFilter()
    salary = django_filters.RangeFilter()

    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'employment', 'salary']