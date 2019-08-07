from django.shortcuts import render, redirect
from .models import Nono

# Create your views here.
def new(request):
        return render(request, 'new.html')

def create(request):
    kname = request.GET.get('kname')
    ename = request.GET.get('ename')
    category = request.GET.get('category')
    country = request.GET.get('country')
    second = request.GET.get('second')
    tag = request.GET.get('tag')

    nono = Nono(
        kname=kname, 
        ename=ename, 
        category=category,
        country = country,
        second = second,
        tag = tag,
    )
    nono.save()

    # return render(request, 'create.html')
    return redirect('/japannono/')

def main(request):
    nonos = Nono.objects.all()
    context = {
        'nonos': nonos,
    }
    return render(request, 'main.html', context)

# def delete(request, todo_id):
#         nono = Nono.objects.get(id=todo_id)
#         todo.delete()
#         return redirect('/todos/')



