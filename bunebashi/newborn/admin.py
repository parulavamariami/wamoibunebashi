from django.contrib import admin
from . models import Service, Username, User, Genre, Comment, ContactMessage


admin.site.register(Service)
admin.site.register(Username)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(ContactMessage)