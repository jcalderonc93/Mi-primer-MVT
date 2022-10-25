from tkinter.font import families
from django.shortcuts import render
from familiares.models import Familiar
# Create your views here.

def mostrar_familiar(request):
    persona_1 = Familiar(nombre="Jhonatan" , documento="1060652180", nacimiento="1993-4-30")
    persona_2 = Familiar(nombre="Vanessa" , documento="1053841571", nacimiento="1995-4-06")
    persona_3 = Familiar(nombre="Ginno" , documento="1054994818", nacimiento="1993-12-28")

    persona_1.save()
    persona_2.save()
    persona_3.save()

    familiares = Familiar.objects.all()
    
    return render(request,"familiares/familia.html",{"familiares":familiares})

