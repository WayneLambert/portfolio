from rest_framework import viewsets, status
from rest_framework.response import Response
from analytics import serializers


class AnalyticsViewSet(viewsets.ViewSet):
    serializer_class = serializers.AnalyticsSerializer

    def list(self, request):
        serializer = serializers.AnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)

    def create(self, request):
        serializer = serializers.AnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            serializer = serializers.AnalyticsSerializer(data=request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            raise Response(status=status.HTTP_400_BAD_REQUEST)
