from django.shortcuts import render, get_object_or_404, redirect
from .models import Six
from django.urls import reverse
from .forms import createForm

# Create your views here.
def main(request):
    sixs = Six.objects.all
    return render(request, 'main.html', {'six':sixs})

def update(request, change_id):
    change_obj = get_object_or_404(Six, pk=change_id)
    if request.method == "POST":
        change_obj.imagename = request.POST['imagename']
        change_obj.imageinfo = request.POST['imageinfo']
        change_obj.imgaeinfo2 = request.POST['imageinfo2']
        change_obj.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request,'update.html',{'change_key':change_obj})


def new(request):
    form = createForm()
    if request.method == "POST" :
        Six_val = Six()
        Six_val.photo = request.FILES['photo']
        Six_val.imagename = request.POST['imagename']
        Six_val.imageinfo = request.POST['imageinfo']
        Six_val.imageinfo2 = request.POST['imageinfo2']
        Six_val.save()
        return redirect(reverse('main'))
    else :
        pass
    return render(request, 'new.html', {'form':form})

def delete(request, delete_id):
    delete_obj = get_object_or_404(Six, pk=delete_id)
    delete_obj.delete()
    return redirect('main')