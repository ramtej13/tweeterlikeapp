from django.contrib import admin
from .models import test,PetsDetails,Pets
# Register your models here.

class PetsAdmin(admin.ModelAdmin):
    # list_display = ['__str__','petUser__username']
    list_display = ['__str__','petUser']
    search_fields = ['petUser__username','pet_details__pet_Name']
    class Meta:
        model = Pets

admin.site.register(test),
admin.site.register(Pets,PetsAdmin),
admin.site.register(PetsDetails)