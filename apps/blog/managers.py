from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset().filter(status=1)
        return qs.prefetch_related("categories").select_related("author__profile")
