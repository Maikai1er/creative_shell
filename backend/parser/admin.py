from django.contrib import admin
from .models import ParsedData


class ParsedDataAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'


admin.site.register(ParsedData, ParsedDataAdmin)
