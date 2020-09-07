from django.db import models



# veg/nog
choices1=(
    ('1','veg'),
    ('2','nonveg')
)


class data(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.first_name
    
class Name(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class dataset(models.Model):
    
    food_item = models.CharField(max_length=200)
    quantity = models.IntegerField(blank=False)
    calories = models.IntegerField(blank=False)
    foodcat = models.CharField(max_length=200,choices=choices1)


    
