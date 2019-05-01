from rest_framework import views, viewsets, status
from rest_framework.response import Response
from . import serializers
# from analytics.get_results import get_results
# from blog.permissions import BasePermission
from . import Analytic


class AnalyticsViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.AnalyticsSerializer

    def list(self, request):
        # json_data = get_results
        serializer = serializers.AnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)

    def create(self, request):
        # json_data = get_results
        serializer = serializers.AnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # json_data = get_results
        try:
            if serializer.is_valid():
                serializer = serializers.AnalyticsSerializer(data=request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            raise Response(status=status.HTTP_400_BAD_REQUEST)
