from django.views.generic import TemplateView


class CVView(TemplateView):
    template_name = "cv.html"
