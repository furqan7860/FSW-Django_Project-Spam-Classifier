from django.contrib import admin

from .models import BlockedEmails, BlockedIps, BlockedWords

admin.site.register(BlockedEmails)
admin.site.register(BlockedIps)
admin.site.register(BlockedWords)

