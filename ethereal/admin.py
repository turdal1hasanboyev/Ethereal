from django.contrib import admin

from .models import Account, Service, Work, Contact, About, Testimonial


admin.site.register(Account)
admin.site.register(Service)
admin.site.register(Work)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Testimonial)
