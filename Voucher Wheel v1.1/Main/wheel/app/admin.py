from app.models import Draw, UniqueCode, Prize
from django.contrib import admin


class DrawAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'email', 'code', 'prize', 'winner', 'try_again', 'retry_used']
    list_filter = ['prize__winner', 'prize__try_again', 'retry_used', 'date']
    search_fields = ['code', 'email', 'prize__label']

    def winner(self, obj):
        return obj.prize.winner

    def try_again(self, obj):
        return obj.prize.try_again


class UniqueCodeAdmin(admin.ModelAdmin):
    readonly_fields = ["code"]
    list_display = ['id', 'date', 'code', 'used']
    list_filter = ['used', 'date']


class PrizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'label', 'winner', 'try_again']
    list_filter = ['winner', 'try_again']


admin.site.register(UniqueCode, UniqueCodeAdmin)
admin.site.register(Draw, DrawAdmin)
admin.site.register(Prize, PrizeAdmin)
