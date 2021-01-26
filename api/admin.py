from django.contrib import admin

from api.models import Car, Rate


class CarAdmin(admin.ModelAdmin):
    search_fields = ("make", "model")
    list_display = ("id", "make", "model")


class RateAdmin(admin.ModelAdmin):
    search_fields = ("car", "rating")
    list_display = ("id", "car_id", "rating")


admin.site.register(Car, CarAdmin)
admin.site.register(Rate, RateAdmin)
