from django.shortcuts import render
from django.views import View
from .models import SPBanModel,LoaiSPModel,SanPhamModel
#from Gio_Hang.forms import GioHangForm
from django.http import HttpResponse

#Create your views here.
class HomeView(View):
    def get(self,request):
        a = SPBanModel.objects.all()
        c= LoaiSPModel.objects.all()
        return render(request, 'San_Pham/home.html',{'f':a,'nav':'home','loai':c})
        
        #def post(self,request):
    #    g = GioHangForm(request.POST)
    #    if g.is_valid():
    #    g.save()
    #    return HttpResponse('Giỏ hàng của bạn đã được lưu chuyển đến bước đặt hàng')
    #    else:
    #        return HttpResponse('Sai cú pháp')


def loaisp(request,id):
    c = LoaiSPModel.objects.all()
    danhmuc= SanPhamModel.objects.all().filter(Loai_sp_id=id)
    return render(request,'San_Pham/danhmuc.html',{'a':danhmuc,'b':c,'loai':c})


def chitietsp(request,id):
    c = LoaiSPModel.objects.all()
    chitietsp = SPBanModel.objects.all().filter(id=id)
    return render(request,'San_Pham/chitietsp.html',{'a':chitietsp,'b':c,'loai':c})

cart ={}
def addcart(request):
    if request.is_ajax():
        id = request.POST.get('id')
        num = request.POST.get('num')
        proDetail = SPBanModel.objects.get(id = id)
        if id in cart.keys():
            itemCart ={
                'name': proDetail.San_Pham.Ten_sp,
                'gia' : proDetail.Gia_sale,
                'anh' : str(proDetail.San_Pham.Anh),
                'num' : int(cart[id]['num'])+1
                }
        else:
            itemCart ={
                'name': proDetail.San_Pham.Ten_sp,
                'gia' : proDetail.Gia_sale,
                'anh' : str(proDetail.San_Pham.Anh),
                'num' : num
                }
        cart[id] = itemCart
        request.session['cart'] = cart
        cartInfo =request.session['cart']

        html = render_to_string('home/addcart.html',{'cart':cartInfo})

    return HttpResponse(html)
