from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} ({self.breed})'
    
class Mission(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        if self.cat:
            return f'Mission {self.id} - Assigned to {self.cat}'
        else:
            return f'Mission {self.id} (Unassigned)'
    
    def check_completion(self):
        if all(target.is_complete for target in self.targets.all()):
            self.is_complete = True
            self.save()

class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'Target {self.name} in {self.country} - Mission {self.mission.id}'
    
    def save(self, *args, **kwargs):
        if self.is_complete:
            self.notes = self.notes
        super(Target, self).save(*args, **kwargs)