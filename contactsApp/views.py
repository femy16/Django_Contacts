from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Contact
from .forms import ContactForm

# Create your views here.
def say_hi(request):
    contact=Contact.objects.all()
    return render(request,"contactsApp/index.html",{'contact':contact})
    
def addcontact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        return redirect("/")
    else:
        form = ContactForm()
        return render(request, "contactsApp/contact_form.html", {'form': form})
# def addcontact(request):
#     form=ContactForm()
#     return render(request,"contactsApp/contact_form.html",{'form':form})
# def do_addcontact(request):
#     form=ContactForm(request.POST)
#     form.save()
#     return redirect('/')
def editcontact(request,id):
    # contact=Contact.objects.get(pk=id)
    contact=get_object_or_404(Contact,pk=id)
    if request.method=="POST":
         form = ContactForm(request.POST, instance=contact)
         form.save()
         return redirect("/")
    else:
        form=ContactForm(instance=contact)
        # return HttpResponse(form)
        return render(request, "contactsApp/contact_form.html", {'form': form})