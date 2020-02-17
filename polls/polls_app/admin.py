from django.contrib import admin

from .models import Question  # pylint: disable=relative-beyond-top-level

admin.site.register(Question)
