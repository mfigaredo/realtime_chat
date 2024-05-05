from django.contrib import admin
from .models import *

class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name', 'groupchat_name', 'admin', 'is_private', 'members_list')

admin.site.register(ChatGroup, ChatGroupAdmin)
admin.site.register(GroupMessage)