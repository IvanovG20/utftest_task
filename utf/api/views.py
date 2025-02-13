from django.db.models import Prefetch

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from food.models import FoodCategory, FoodListSerializer, Food


class FoodListView(APIView):
    """Выдает все опубликованные блюда"""

    def get(self, request):
        queryset = FoodCategory.objects.filter(
            food__is_publish=True
        ).prefetch_related(
            Prefetch(
                'food',
                queryset=Food.objects.filter(is_publish__exact=True)
            )
        )
        serializer = FoodListSerializer(queryset, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
