from django.contrib import admin
from .models import Soldier, Weapon, WeaponUnit


class WeaponUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'weapon', 'status', 'due_back', 'operator')
    list_editable = ('due_back', 'status', 'operator')
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
    can_delete = False
    extra = 0

class SoldierAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'rank')
    inlines = [WeaponsUnitInline]
    model = Soldier
    extra = 0


# Register your models here.
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Soldier, SoldierAdmin)
admin.site.register(WeaponUnit, WeaponUnitAdmin)

