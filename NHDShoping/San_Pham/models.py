from django.db import models

# Create your models here.

class LoaiSPModel(models.Model):
    Loai_sp = models.CharField(max_length=50, verbose_name='Loại Sản Phẩn', blank=True,)
    Link = models.CharField(max_length=50, verbose_name='Link',)
    Mo_ta = models.TextField(verbose_name='Mô Tả')
    Trang_thai = models.BooleanField(verbose_name='Trạng Thái')

    def __str__(self):
        return self.Loai_sp


class SanPhamModel(models.Model):
    Ma_sp = models.CharField( max_length=10, verbose_name='Mã Sản Phẩm')
    Loai_sp = models.ForeignKey(LoaiSPModel,on_delete=models.CASCADE,default=1)
    Ten_sp = models.CharField(max_length=50, verbose_name='Tên Sản Phẩm', blank=True)
    Mo_ta = models.TextField(verbose_name='Mô Tả')
    Gia_nhap = models.IntegerField(verbose_name='Giá Nhập', blank=True, default=0)
    Trang_thai = models.BooleanField(verbose_name='Trạng Thái')
    Anh = models.ImageField(upload_to='media')

    def __str__(self):
        return self.Ten_sp

mota= ((1,'Đang Sale 10 %'),(2,'Đang giảm mạnh'),(3,'Đang Sale 50 %'))

class SPBanModel(models.Model):
    San_Pham = models.ForeignKey(SanPhamModel,on_delete=models.CASCADE)
    Mo_ta = models.SmallIntegerField(verbose_name='Mô Tả',choices =mota,default=2 )
    Gia_ban = models.IntegerField(verbose_name='Giá Bán', blank=True, default=200000)
    Gia_sale = models.IntegerField(verbose_name='Giá Sale',  default=150000)
    Hang_ton = models.IntegerField(verbose_name='Hàng Tồn', default=100)
    Trang_thai = models.BooleanField(verbose_name='Trạng Thái',default=True)


    def __str__(self):
        return self.San_Pham.Ten_sp