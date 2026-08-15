from django.contrib import admin
from .models import Content, ContentGenre, ProducerCountry, ContentActor, ContentLanguageStatus


admin.site.register(Content)
admin.site.register(ContentGenre)
admin.site.register(ProducerCountry)
admin.site.register(ContentActor)
admin.site.register(ContentLanguageStatus)