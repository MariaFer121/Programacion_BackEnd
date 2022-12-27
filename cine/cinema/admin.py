from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Continet)
admin.site.register(Country)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(UserSeeMovies)
admin.site.register(MovieDirector)
admin.site.register(MovieActors)
admin.site.register(Character)
admin.site.register(MovieActorsCharacter)