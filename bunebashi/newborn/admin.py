from django.contrib import admin
from . models import Service, Username, User, Genre, Comment


admin.site.register(Service)
admin.site.register(Username)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Comment)