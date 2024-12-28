from django.contrib import admin
from .models import Contact, About, Facts, Offer, Products, Team, Service, Testimonial, Newsletter
# Register your models here.
admin.site.register(Facts)
admin.site.register(Offer)
admin.site.register(Contact)
admin.site.register(Products)
admin.site.register(Service)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Newsletter)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}