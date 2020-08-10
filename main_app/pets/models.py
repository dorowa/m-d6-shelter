from django.db import models

# Create your models here.
class Kind(models.Model):
    kind_name = models.TextField()
    kind_info = models.TextField()
    kind_link = models.CharField(max_length=20, null=True)
    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"
    def __str__(self):
        return f'{self.kind_name}'


class Breed(models.Model):
    breed_name = models.TextField()
    breed_info = models.TextField()
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
    def __str__(self):
        return f'{self.breed_name}'

class Volunteer(models.Model):
    vol_name = models.TextField()
    vol_phone = models.CharField(max_length=11)
    vol_rating = models.SmallIntegerField(default=1)
    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"
    def __str__(self):
        return f'{self.vol_name}'

class PetSpecie(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER = [
        (MALE, "мальчик"),
        (FEMALE, "девочка")
    ]
    pet_name = models.TextField()
    pet_birthdate = models.DateField()
    pet_register_date = models.DateField()
    pet_gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    pet_img = models.ImageField(upload_to="pet_imgs/", blank = True, null = True)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, related_name = 'kinds')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breeds')
    volunteer = models.ManyToManyField(Volunteer, through='PetAction', related_name = "volunteers", blank = True)
    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"
    def __str__(self):
        return f'{self.pet_name}'

class PetAction(models.Model):
    pa_action = models.CharField(max_length=20)
    pa_date = models.DateField()
    pa_info = models.TextField()
    petspecie = models.ForeignKey(PetSpecie, on_delete=models.CASCADE, related_name='taken_pet')
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name = 'took_volunteer')
    class Meta:
        verbose_name = "Передача"
        verbose_name_plural = "Передачи"
    def __str__(self):
        return f'{self.pet_action}'
