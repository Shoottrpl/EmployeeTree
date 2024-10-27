from distutils.command.register import register
from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


from .models import Position, Employee



@admin.register(Position)
class PositionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name']



@admin.register(Employee)
class EmployeeAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title']
    expand_tree_by_default = True
    list_per_page = 50
