from django.contrib import admin
from .models import ParsedData
from .parser import pass_to_temp_table


class ParsedDataAdmin(admin.ModelAdmin):
    change_form_template = 'change_form.html'


admin.site.register(ParsedData, ParsedDataAdmin)
