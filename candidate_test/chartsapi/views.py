from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import ChartDataService

class ChartDataAPI(APIView):
    def get(self, request):
        data = ChartDataService.get_simple_data()
        return Response(data, status=status.HTTP_200_OK)
