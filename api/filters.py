import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    # emp_id = django_filters.RangeFilter(field_name='emp_id')
    id_min = django_filters.CharFilter(method='fileter_by_id_range', label='From EMP ID')
    id_max =  django_filters.CharFilter(method='filer_by_id_range', label='To EMP ID')
    
    class Meta:
        model = Employee
        fields = ['designation','emp_name','id_min','id_max']

    def filter_by_id_range(self,queryset,vlaue):
        if name  == 'id_min':
            return queryset.filter(emp_id_gte=vlaue)
        elif name == 'id_max' :
            return queryset.filter(emp_id_lte=vlaue)
        return queryset