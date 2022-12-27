from django.db import models

# Create your models here.
class Continet(models.Model):
    name_Continet= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name_Continet

class Country(models.Model):
    name_Country= models.CharField(max_length=50)
    continet = models.ForeignKey(
        Continet,
        on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return self.name_Country

class Profile(models.Model):
    description_Profile= models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.PROTECT,  null= True)
    def __str__(self) -> str:
        return self.description_Profile

class User(models.Model):
    name_User= models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.RESTRICT
    )
    def __str__(self) -> str:
        return self.name_User

class Director(models.Model):
    name_Director= models.CharField(max_length=50)
    profile= models.ForeignKey(
        Profile,
        on_delete=models.PROTECT
    )
    def __str__(self) -> str:
        return self.name_Director

class Actor(models.Model):
    name_Actor = models.CharField(max_length=50)
    profile=models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        null=True
    )
    def __str__(self) -> str:
        return self.name_Actor

class Movie(models.Model):
    imdb_Movie =models.CharField(max_length=50)
    movie_title = models.CharField(max_length=50)
    movie_year = models.IntegerField()
    director =models.ManyToManyField(Director, through='MovieDirector')
    actor = models.ManyToManyField(Actor, through='MovieActors')
    user = models.ManyToManyField(User, through="UserSeeMovies" )

    def __str__(self) -> str:
        return self.movie_title

class UserSeeMovies(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'El usuario {self.user} ve la pelicula {self.movie}'

class MovieDirector(models.Model):
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE
    )
    movie= models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return f'{self.director} dirige la pelicula {self.movie}'

class MovieActors(models.Model):
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE
    )
    movie=models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    character = models.ManyToManyField('Character')
    def __str__(self) -> str:
        return f'{self.actor} actua en la pelicula: {self.movie}'

class Character (models.Model):
    name_Character = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name_Character

class MovieActorsCharacter(models.Model):

    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE
    )
    movie_actor = models.ForeignKey(
        MovieActors,
        on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return f'{self.movie_actor} interpretando a {self.character}'