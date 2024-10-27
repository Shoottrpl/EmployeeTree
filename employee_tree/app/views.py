from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic.list import ListView

from .models import Employee, Position

class IndexView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'app/index.html'
    paginate_by = 50


class EmployeesView(IndexView):
    template_name = 'app/employees.html'
    def get_ordering(self):
        # ordering = self.request.GET.get('salary')
        ordering = 'full_name'
        print(ordering)
        return ordering


