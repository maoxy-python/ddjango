from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from main_app.forms import MyForm


class IndexView(View):
    def get(self,request):
        return render(request,"index.html")
    def post(self,request):
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponse("success")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("fail")