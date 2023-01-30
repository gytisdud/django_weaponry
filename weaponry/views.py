from django.shortcuts import render
from django.http import HttpResponse
from .models import Weapon, Soldier, WeaponUnit
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.edit import CreateView

def index(request):
    num_weapons = Weapon.objects.all().count()
    num_units = WeaponUnit.objects.all().count()
    num_units_available = WeaponUnit.objects.filter(status__exact='a').count()
    num_soldiers = Soldier.objects.count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_weapons': num_weapons,
        'num_units': num_units,
        'num_units_available': num_units_available,
        'num_soldiers': num_soldiers,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

def soldiers(request):
    paginator = Paginator(Soldier.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_soldiers = paginator.get_page(page_number)
    # soldiers = Soldier.objects.all()
    context = {
        'soldiers': paged_soldiers
    }
    return render(request, 'soldiers.html', context=context)
# Create your views here.
def soldier(request, soldier_id):
    single_soldier = get_object_or_404(Soldier, pk=soldier_id)
    return render(request, 'soldier.html', {'soldier': single_soldier})


class WeaponListView(generic.ListView):
    model = Weapon
    paginate_by = 5
    template_name = 'weapon_list.html'

class WeaponDetailView(generic.DetailView):
    model = Weapon
    template_name = 'weapon_detail.html'

def search(request):
    query = request.GET.get('query')
    search_results = Weapon.objects.filter(Q(name__icontains=query) |
                                        Q(description__icontains=query))
    return render(request, 'search.html', {'weapons': search_results, 'query':
        query})

class WeaponUnitListView(generic.ListView):
    model = WeaponUnit
    paginate_by = 6
    template_name = 'weapon_unit.html'



