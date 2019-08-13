from django.conf import settings


def get_ga_tracking_id(request):
    return {'ga_tracking_id': settings.GA_TRACKING_ID}
