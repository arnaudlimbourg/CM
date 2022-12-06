from django.shortcuts import render
from club.models import Club  # importer le modele pour l'utiliser plus tard


def index_view(request):
    """Index view welcoming our users
    """
    clubs = Club.objects.all()  # on récupère tous les clubs de notre base
    
    # le contexte est transmis au template
    context = {
        "clubs_list": clubs
    }
    return render(request, "club/index.html", context=context)

