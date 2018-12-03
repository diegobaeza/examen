from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'compras/inicio.html', {})


def base_layout(request):
	template='compras/inicio.html'
	return render(request,template)

def getdata(request):
	results=feed.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)

