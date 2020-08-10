from django.contrib import admin
from pets.models import PetSpecie, PetAction, Volunteer, Breed, Kind
from django.utils.html import format_html
# Register your models here.

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ("kind_name","kind_info")
    fields = ("kind_name","kind_info", "kind_link")

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    pass

@admin.register(PetSpecie)
class PetSpecieAdmin(admin.ModelAdmin):
    list_display = ("pet_name","pet_birthdate","pet_register_date","image_tag")
    fields = ("pet_name","pet_birthdate","pet_register_date","pet_img", "kind","breed", "pet_gender")
    def image_tag(self, obj):
        if obj.pet_img:
            return format_html(f'<img src="{obj.pet_img.url}" width="100"/>')
        return format_html(f'<img src="" width="100"/>')

@admin.register(PetAction)
class PetActionAdmin(admin.ModelAdmin):
    pass