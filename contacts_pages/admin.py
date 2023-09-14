import textwrap

from django.contrib import admin
from django.utils.html import format_html

from contacts_pages.models import FeedbackMessage


class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ('user_preview', 'message_preview', 'sent')
    list_display_links = None

    def user_preview(self, obj):
        if obj:
            name = obj.name
            email = obj.email
            number = obj.number

            formatted_info = f"""
                <h4>Имя: {name}</h4>
                <h4>Email: {email}</h4>
                <h4>Номер: {number}</h4>
            """
            return format_html(formatted_info)
        return ''

    user_preview.short_description = 'Клиент'  # Название колонки

    def message_preview(self, obj):
        words = obj.msg.split()
        lines = textwrap.wrap(" ".join(words), width=70)
        textarea = "<br/>".join(lines)
        return format_html(textarea) if obj else ''

    message_preview.short_description = 'Сообщение'  # Название колонки

    def has_add_permission(self, request):
        return False

    class Meta:
        model = FeedbackMessage


admin.site.register(FeedbackMessage, FeedbackMessageAdmin)
