from django.views.generic.list import ListView

from .models import Employee, Position

class IndexView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'app/index.html'
    paginate_by = 50


class EmployeesView(IndexView):
    template_name = 'app/employees.html'

    def get_queryset(self):
        queryset =  super().get_queryset().values('full_name', 'employment', 'position__name', 'salary')
        self.request.session['sort'] = self.request.GET['sort']
        order = self.request.session['sort']

        if order:
             queryset = queryset.order_by(order)

        return queryset



