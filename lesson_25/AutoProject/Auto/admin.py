from django.contrib import admin
from Auto.models import Car, CarModel, User, Brand


class CarModelInline(admin.TabularInline):
    model = CarModel


class BrandInline(admin.TabularInline):
    model = Brand


class CarInline(admin.TabularInline):
    model = Car


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('get_car_full_name', 'vin', 'is_active')
    search_fields = ('vin', )

    def get_car_full_name(self, obj):
        return f"{obj.car_brand.name} {obj.car_model.name}"
    get_car_full_name.short_description = 'Car'


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('phone_number', )
