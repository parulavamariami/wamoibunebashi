from .models import Genre, Username

def seeder_func():

    genres = ['ლაშქრობა', 'ფოტო', 'სრიალი']
    usernames = ['მარიამ ფარულავა']
    for genre in genres:
        if not Genre.objects.filter(name=genre):
            new_genre = Genre(name=genre)
            new_genre.save()

    for username in usernames:
        if not Username.objects.filter(fullname=username):
            new_username = Username(fullname=username)
            new_username.save()