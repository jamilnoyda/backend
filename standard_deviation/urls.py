# users/urls.py

from django.conf.urls import url

from standard_deviation.views import(
    get_standard_deviation_of_days
)


urlpatterns = [
    url(r'^days/$', get_standard_deviation_of_days,
        name='get_standard_deviation_of_days'),
    # url(r'^hours/$', get_standard_deviation, name = 'get_standard_deviation'),

]
