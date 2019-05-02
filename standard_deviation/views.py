from rest_framework.views import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.conf import settings
from standard_deviation.service import calculate_standard_deviation_for_days


@api_view(('GET',))
def get_standard_deviation_of_days(request):
    registered_users, casual_users = calculate_standard_deviation_for_days()
    response = {
        'registered_users': registered_users,
        'casual_users': casual_users,
        'status': status.HTTP_200_OK
    }
    return Response(response)
