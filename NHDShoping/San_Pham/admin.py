from django.contrib import admin
from .models import SanPhamModel, LoaiSPModel, SPBanModel


class LoaiSPModelAdmin(admin.ModelAdmin):
    list_display = ('Loai_sp',)

admin.site.register(LoaiSPModel, LoaiSPModelAdmin)


class SanPhamModelAdmin(admin.ModelAdmin):
    list_display = ('Ma_sp','Ten_sp','Loai_sp')


admin.site.register(SanPhamModel, SanPhamModelAdmin)


class SPBanModelAdmin(admin.ModelAdmin):
   list_display = ('San_Pham',)
admin.site.register(SPBanModel, SPBanModelAdmin)