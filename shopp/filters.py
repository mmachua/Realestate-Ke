from .models import BusinessAddress
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = BusinessAddress
        fields = ['category', 'name', ]