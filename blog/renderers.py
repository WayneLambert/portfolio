from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.views import get_view_name


class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_view_name(self, cls, suffix=None):
        return "CUstom " + cls.__name__
