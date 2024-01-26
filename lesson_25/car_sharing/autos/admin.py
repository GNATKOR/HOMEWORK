from django.contrib import admin
from autos.models import Car, CarModel, User, Brand


class CarModelInline(admin.TabularInline):
    model = CarModel


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ordering = ('name',)
    inlines = [CarModelInline]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('get_car_full_name', 'vin', 'is_active')
    search_fields = ('vin', )

    def get_car_full_name(self, obj):
        """This func was added so that in the "Car" model in django admin,
         the car model is displayed as - (specific brand, specific model,
          specific vin and whether it is active)"""
        return f"{obj.car_brand.name} {obj.car_model.name}"
    get_car_full_name.short_description = 'Car'


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('phone_number', )
