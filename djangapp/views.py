from django.shortcuts import render,redirect
from .models import djann
# Create your views here.
def djann_create(request):
    a=djann.objects.all()
    if request.method=='POST':
        a=request.POST.get('course')
        b=request.POST.get('fees')
        djann.objects.create(course=a,fees=b)
        return redirect('home')
    return render(request,'index.html',{'a':a})

def delete_djann(request,id):
    djann.objects.filter(id=id).delete()
    return redirect('home')

def update_djann(request, id):
    b = djann.objects.get(id=id)

    if request.method == 'POST':
        b.course = request.POST.get('course')
        b.fees = request.POST.get('fees')

        b.save()

        return redirect('home')

    return render(request, 'update.html', {'b': b})
