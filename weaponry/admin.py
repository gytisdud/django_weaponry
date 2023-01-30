from django.contrib import admin
from .models import Soldier, Weapon, WeaponUnit


class WeaponInstanceAdmin(admin.ModelAdmin):
    list_display = ('weapon', 'status', 'due_back')
    list_editable = ('due_back', 'status')
    list_filter = ('status', 'due_back')
    search_fields = ('id', 'weapon__name')



    fieldsets = (
        ('General', {'fields': ('id', 'weapon')}),
        ('Availability', {'fields': ('status', 'due_back' 'operator')}),
    )

class WeaponsUnitInline(admin.TabularInline):
    model = WeaponUnit
    extra = 0

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    inlines = [WeaponsUnitInline]
    can_delete = False
    extra = 0





# Register your models here.
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Soldier)
admin.site.register(WeaponUnit)


