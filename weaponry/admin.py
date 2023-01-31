from django.contrib import admin
from .models import Soldier, Weapon, WeaponUnit

class WeaponUnitAdmin(admin.ModelAdmin):
    list_display = ('weapon', 'status', 'date', 'operator')
    list_editable = ('date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('id', 'weapon__name')



    fieldsets = (
        ('General', {'fields': ('id', 'weapon')}),
        ('Availability', {'fields': ('status', 'date' 'operator')}),
    )

class WeaponsUnitInline(admin.TabularInline):
    model = WeaponUnit
    extra = 0

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    inlines = [WeaponsUnitInline]
    can_delete = False
    extra = 0

class SoldierAdmin(admin.ModelAdmin):
    list_display = ('rank', 'last_name', 'id')
    inlines = [WeaponsUnitInline]
    model = Soldier
    extra = 0




# Register your models here.
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Soldier, SoldierAdmin)
admin.site.register(WeaponUnit, WeaponUnitAdmin)

