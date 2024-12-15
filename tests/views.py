from rest_framework import viewsets
from rest_framework.response import Response
from .models import AnimalTest
from .serializers import AnimalTestSerializer
from django.db.models import Avg, Max, Count


class AnimalTestViewSet(viewsets.ModelViewSet):
    queryset = AnimalTest.objects.all()
    serializer_class = AnimalTestSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Фильтрация по типу животного
        animal_species = request.query_params.get('animal_species', None)
        if animal_species:
            queryset = queryset.filter(animal_species=animal_species)

        # Статистика
        total_tests = queryset.count()
        average_productivity = queryset.aggregate(Avg('productivity'))['productivity__avg']
        max_productivity = queryset.aggregate(Max('productivity'))['productivity__max']
        good_health_count = queryset.filter(health_status=True).count()
        good_health_percentage = (good_health_count / total_tests * 100) if total_tests > 0 else 0

        response_data = {
            "total_tests": total_tests,
            "average_productivity": average_productivity,
            "max_productivity": max_productivity,
            "good_health_percentage": good_health_percentage,
            "results": AnimalTestSerializer(queryset, many=True).data,
        }

        return Response(response_data)