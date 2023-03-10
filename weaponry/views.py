from django.shortcuts import render
from django.http import HttpResponse
from .models import Weapon, Soldier, WeaponUnit
from django.contrib import messages
from django.contrib.auth.forms import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

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

@login_required
def soldiers(request):
    paginator = Paginator(Soldier.objects.all(), 12)
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


class WeaponListView(LoginRequiredMixin, generic.ListView):
    model = Weapon
    paginate_by = 6
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


class WeaponByAdminCreateView(LoginRequiredMixin, CreateView):
    model = WeaponUnit
    fields = ('weapon', 'due_back', 'status', 'operator')
    success_url = '/weaponry/'
    template_name = 'create_unit.html'
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class WeaponByAdminDeleteView(LoginRequiredMixin, DeleteView):
    model = WeaponUnit
    template_name = 'delete_weapon.html'

    def test_func(self):
        weapon = self.get_object()
        return self.request.user == weapon.admin

    def get_success_url(self):
        soldier_id = self.kwargs['soldier_id']
        return reverse_lazy('soldier', kwargs={'soldier_id': soldier_id})




