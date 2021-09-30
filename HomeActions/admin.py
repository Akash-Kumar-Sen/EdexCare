from django.contrib import admin
from .models import HomeActions,ActionBullet,CustomerResponse

class ActionBulletAdmin(admin.StackedInline):
    model = ActionBullet


class HomeActionsAdmin(admin.ModelAdmin):
    inlines = [ActionBulletAdmin]

@admin.register(ActionBullet)
class ActionBulletAdmin(admin.ModelAdmin):
    pass

admin.site.register(HomeActions,HomeActionsAdmin)
admin.site.register(CustomerResponse)