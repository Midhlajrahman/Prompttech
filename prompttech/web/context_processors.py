from web.models import About
from web.models import Service
from web.models import SocialMedia


def main_context(request):
    return {
        "services": Service.objects.all(),
        "social_medias": SocialMedia.objects.all(),
        "about": About.objects.first(),
    }
