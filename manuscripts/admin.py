from django.contrib import admin

from manuscripts.models import Manuscript, ManuscriptCategory

admin.site.register(Manuscript)
admin.site.register(ManuscriptCategory)
