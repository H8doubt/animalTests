from django.db import models

class AnimalTest(models.Model):
    ANIMAL_SPECIES = [
        ('cow', 'Корова'),
        ('goat', 'Коза'),
        ('horse', 'Кобыла'),
        # Добавьте другие виды животных по необходимости
    ]

    animal_name = models.CharField(max_length=100)
    test_date = models.DateField()
    created_at = models.DateField()
    productivity = models.FloatField()
    health_status = models.BooleanField()  # True - хорошее состояние, False - плохое состояние
    animal_species = models.CharField(max_length=20, choices=ANIMAL_SPECIES)

    def __str__(self):
        return self.animal_name
