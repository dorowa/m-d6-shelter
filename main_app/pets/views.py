from django.shortcuts import render

# Create your views here.
from pets.forms import KindForm
from pets.models import Kind, PetSpecie
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import get_object_or_404

class KindMenuList(ListView):
    model = Kind
    template_name = 'kind_menu.html'

class PetSpeciesList(ListView):
    model = PetSpecie
    menu_list = Kind.objects.all()
    template_name = "petspecies_list.html"

class PetSpeciesCards(ListView):
    """Получаем список животных по меню, выбрав вид"""
    menu_list = Kind.objects.all()
    template_name = "petspecies_list.html"
    def get_queryset(self):
        self.kind = get_object_or_404(Kind, kind_name=self.kwargs['kind'])
        return PetSpecie.objects.filter(kind=self.kind)

class AboutView(ListView):
    model = Kind
    template_name = 'about.html'

class PetSpecieCard(DetailView):
    model = PetSpecie
    menu_list = Kind.objects.all()
    template_name = "pet_card.html"
    