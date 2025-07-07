from django.contrib import admin
from .models import Reservation
from .models import HeroImage

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'created_at')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'phone')

admin.site.register(HeroImage)


# Register your models here.
