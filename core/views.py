from django.shortcuts import render
import json

from .models import *
from .forms import *

from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#####################
#Библиотека
def library(request):
    template = "library.html"
    exempls = []
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    
    currentPage = 0
    pageCount = int(len(exempls)/8) + 1*int(len(exempls)%8!=0)
    listPage = []
    for i in range(8*currentPage, 8*currentPage+8):
        if len(exempls)>i:
            listPage.append([exempls[i], ThreatExemplar.objects.filter(Exemplar = exempls[i].id)])

    listRowPage = []
    for i in range(len(listPage)):
        if(i%2 == 0):
            listRowPage.append([listPage[i]])
        else:
            listRowPage[-1].append(listPage[i])

    context = {
        'login': None,
        'CategoryForm': CategoryForm(),
        'Exemplars': listRowPage,
        'PageCurrent': currentPage+1,
        'PagePrevious': currentPage,
        'PageNext': currentPage+2,
        'Pages': range(1, pageCount+1),
        'PageCount': pageCount
    }
    return render(request, template, context)


def library_page(request, page):
    template = "library.html"
    exempls = []
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    
    currentPage = int(page)-1
    pageCount = int(len(exempls)/8) + 1* int(len(exempls)%8!=0)
    listPage = []
    for i in range(8*currentPage, 8*currentPage+8):
        if len(exempls)>i:
            listPage.append([exempls[i], ThreatExemplar.objects.filter(Exemplar = exempls[i].id)])

    listRowPage = []
    for i in range(len(listPage)):
        if(i%2 == 0):
            listRowPage.append([listPage[i]])
        else:
            listRowPage[-1].append(listPage[i])

    context = {
        'login': None,
        'CategoryForm': CategoryForm(),
        'Exemplars': listRowPage,
        'PageCurrent': currentPage+1,
        'PagePrevious': currentPage,
        'PageNext': currentPage+2,
        'Pages': range(1, pageCount+1),
        'PageCount': pageCount
    }
    return render(request, template, context)


def library_pers(request, login):
    login = login
    template = "library.html"
    exempls = []
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    
    currentPage = 0
    pageCount = int(len(exempls)/8) + 1*int(len(exempls)%8!=0)
    listPage = []
    for i in range(8*currentPage, 8*currentPage+8):
        if len(exempls)>i:
            listPage.append([exempls[i], ThreatExemplar.objects.filter(Exemplar = exempls[i].id)])

    listRowPage = []
    for i in range(len(listPage)):
        if(i%2 == 0):
            listRowPage.append([listPage[i]])
        else:
            listRowPage[-1].append(listPage[i])

    context = {
        'login': login,
        'CategoryForm': CategoryForm(),
        'Exemplars': listRowPage,
        'PageCurrent': currentPage+1,
        'PagePrevious': currentPage,
        'PageNext': currentPage+2,
        'Pages': range(1, pageCount+1),
        'PageCount': pageCount
    }
    return render(request, template, context)

def library_pers_page(request, login, page):
    login = login
    template = "library.html"
    exempls = []
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    for ex in Exemplar.objects.all():
        exempls.append(ex)
    
    currentPage = int(page)-1
    pageCount = int(len(exempls)/8) + 1* int(len(exempls)%8!=0)
    listPage = []
    for i in range(8*currentPage, 8*currentPage+8):
        if len(exempls)>i:
            listPage.append([exempls[i], ThreatExemplar.objects.filter(Exemplar = exempls[i].id)])

    listRowPage = []
    for i in range(len(listPage)):
        if(i%2 == 0):
            listRowPage.append([listPage[i]])
        else:
            listRowPage[-1].append(listPage[i])

    context = {
        'login': login,
        'CategoryForm': CategoryForm(),
        'Exemplars': listRowPage,
        'PageCurrent': currentPage+1,
        'PagePrevious': currentPage,
        'PageNext': currentPage+2,
        'Pages': range(1, pageCount+1),
        'PageCount': pageCount
    }
    return render(request, template, context)

#####################
#Экземпляр
def exemplar_page(request, id, page):
    template = "exemplar.html"
    exempl = Exemplar.objects.get(id = id)
    thrExempl = ThreatExemplar.objects.all().filter(Exemplar = exempl)
    
    allThrExempl = []
    for elem in thrExempl:
        allThrExempl.append({
            'name': elem.Name,
            'imageList': ThreatExemplarImage.objects.all().filter(ThreatExemplar = elem)
        })
    context = {
        'login': None,
        'id': id,
        'page': page,
        'Exemplar': exempl,
        'ThrExempl': allThrExempl
    }
    return render(request, template, context)

def exemplar_pers_page(request, login, id, page):
    template = "exemplar.html"
    exempl = Exemplar.objects.get(id = id)
    thrExempl = ThreatExemplar.objects.all().filter(Exemplar = exempl)
    
    allThrExempl = []
    for elem in thrExempl:
        allThrExempl.append({
            'name': elem.Name,
            'imageList': ThreatExemplarImage.objects.all().filter(ThreatExemplar = elem)
        })
    context = {
        'login': login,
        'id': id,
        'page': page,
        'Exemplar': exempl,
        'ThrExempl': allThrExempl
    }
    return render(request, template, context)

#####################
#Вход
def sign_in(request):
    
    if request.method == "POST":

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
        }
        if User.objects.all().filter(Name=fields['login'], Password=fields['password']):
            template = 'library.html'
            return HttpResponseRedirect(reverse("library_pers_page", args=[fields['login']]))
        else:
            template = "sign_in.html"
            sign_form = SignForm()
            context = {
                'form': sign_form,
                "message": "Логин или пароль не верны."
            }
            return render(request, template, context)    
    else:
        template = "sign_in.html"
        sign_form = SignForm()
        context = {
            'form': sign_form
        }
        return render(request, template, context)

#####################
#Регистрация
def register(request):
    
    if request.method == "POST":
        user = User()

        fields = {
            'login': request.POST.get("login"),
            'password': request.POST.get("password"),
            'rePassword': request.POST.get("rePassword")
        }

        if User.objects.all().filter(Name=fields['login']):
            template = "register.html"
            reg_form = RegisterForm()
            reg_form.fields["login"].initial = fields['login']
            reg_form.fields["password"].initial = fields['password']
            reg_form.fields["rePassword"].initial = fields['rePassword']
            context = {
                'form': reg_form,
                "message":"Пользователь с таким логином уже зарегистрирован"
            }
            return render(request, template, context)
        elif fields['password'] != fields['rePassword']:
            template = "register.html"
            reg_form = RegisterForm()
            reg_form.fields["login"].initial = fields['login']
            reg_form.fields["password"].initial = fields['password']
            reg_form.fields["rePassword"].initial = fields['rePassword']
            context = {
                'form': reg_form,
                "message":"Введенные пароли не совпадают. Попробуйте еще раз"
            }
            return render(request, template, context)
        else:
            user.Name = fields['login']
            user.Password = fields['password']
            user.save()
            return HttpResponseRedirect(reverse("sign_in"))  
    else:
        template = "register.html"
        sign_form = RegisterForm()
        context = {
            'form': sign_form
        }
        return render(request, template, context)


######################
#Личный кабинет
def personal(request, login):
    if request.method == "POST":

        fields = {
            'login': request.POST.get("login"),
            'email': request.POST.get("email"),
            'password': request.POST.get("password"),
            'rePassword': request.POST.get("rePassword"),
        }

        if fields['password'] != fields['rePassword']:
            user = User.objects.get(Name = login)
            template = "personal_cabinet.html"
            personal_form = PersonForm()
            personal_form.fields["login"].initial = fields["login"]
            personal_form.fields["email"].initial = fields["email"]
            personal_form.fields["password"].initial = fields["password"]
            personal_form.fields["rePassword"].initial = fields["rePassword"]
            context = {
                'login':login,
                'form': personal_form,
                'user': user,
                "message":"Введенные пароли не совпадают. Попробуйте еще раз."
            }
            return render(request, template, context)  
        
        if fields['login'] != login and User.objects.all().filter(Name=fields['login']):
            user = User.objects.get(Name = login)
            template = "personal_cabinet.html"
            personal_form = PersonForm()
            personal_form.fields["login"].initial = fields["login"]
            personal_form.fields["email"].initial = fields["email"]
            personal_form.fields["password"].initial = fields["password"]
            personal_form.fields["rePassword"].initial = fields["rePassword"]
            context = {
                'login':login,
                'form': personal_form,
                'user': user,
                "message":"Пользователь с таким логином уже зарегистрирован."
            }
            return render(request, template, context)
        
        #Сохранение
        user = User.objects.get(Name = login)
        user.Name = fields["login"]
        user.Email = fields["email"]
        user.Password = fields["password"]
        user.save()

        return HttpResponseRedirect(reverse("personal", args=[user.Name])) 
    else:
        user = User.objects.get(Name = login)
        template = "personal_cabinet.html"
        personal_form = PersonForm()
        personal_form.fields["login"].initial = user.Name
        personal_form.fields["email"].initial = user.Email
        personal_form.fields["password"].initial = user.Password
        personal_form.fields["rePassword"].initial = user.Password
        context = {
            'login':login,
            'form': personal_form,
            'user': user
        }

        return render(request, template, context)



######################
#Протоколы
def protocols(request, login):
    
    if request.method == "POST":

        fields = {
            'date': request.POST.get("date"),
            'address': request.POST.get("address"),
            'coordinates': request.POST.get("coordinates"),
            'description': request.POST.get("description"),
        }
        protocol = Protocol()
        protocol.User = User.objects.get(Name = login)
        protocol.Date = fields['date']
        protocol.Address = fields['address']
        protocol.Сoordinates = fields['coordinates']
        protocol.Description = fields['description']
        protocol.save()

        template = "protocols.html"
        protocol_form = ProtocolForm()

        prots = []
        for item in Protocol.objects.all().filter(User = User.objects.get(Name = login)):
            prots.append({
                'prot':item,
                'num': len(ProtocolExemplarFind.objects.all().filter(Protocol = item))
            })

        context = {
            'login':login,
            'form': protocol_form,
            'prots': prots
        }
        return render(request, template, context)  
    
              
    else:
        template = "protocols.html"
        protocol_form = ProtocolForm()

        prots = []
        for item in Protocol.objects.all().filter(User = User.objects.get(Name = login)):
            prots.append({
                'prot':item,
                'num': len(ProtocolExemplarFind.objects.all().filter(Protocol = item))
            })

        context = {
            'login':login,
            'form': protocol_form,
            'prots': prots
        }
        return render(request, template, context)

def protocols_delete(request, login, id):
    
    if Protocol.objects.all().filter(id=id):
        Protocol.objects.all().filter(id=id).delete()

    return HttpResponseRedirect(reverse("protocols", args=[login]))

######################
#Протокол
def protocol(request, login, id):
    
    if request.method == "POST":

        #Изменение данных
        if request.POST.get("date"):
            prot = Protocol.objects.get(id = id)
            prot.Date = request.POST.get("date")
            prot.Address = request.POST.get("address")
            prot.Сoordinates = request.POST.get("coordinates")
            prot.Description = request.POST.get("description")
            prot.Note = request.POST.get("report")
            
            prot.save()

            return HttpResponseRedirect('{}#'.format(reverse("protocol", args=[login, id])))
        
        elif request.POST.get("idGenus"):
            prot = Protocol.objects.get(id = id)
            prot.Genus = Genus.objects.get(id = int(request.POST.get("idGenus")))
            prot.save()
            
            ProtocolExemplarChoice.objects.filter(Protocol = prot).delete()

            return HttpResponseRedirect('{}#file_name'.format(reverse("protocol", args=[login, id])))
        
        elif request.POST.get("idThreatExemplar"):
            protocolExemplar = ProtocolExemplarChoice()
            protocolExemplar.Protocol = Protocol.objects.get(id = id)
            protocolExemplar.Exemplar = Exemplar.objects.get(id = int(request.POST.get("idThreatExemplar")))
            protocolExemplar.save()
            
            return HttpResponseRedirect('{}#file_name'.format(reverse("protocol", args=[login, id])))
            
    else:
        template = "protocol.html"

        prot = Protocol.objects.get(id = id)

        exempleChoice = []
        for exempl in ProtocolExemplarChoice.objects.all().filter(Protocol = prot):
            exempleChoice.append({
                'id': exempl.id,
                'Name': exempl.Exemplar.Name,
                'Category': exempl.Exemplar.Category,
                'List': ThreatExemplar.objects.filter(Exemplar = exempl.Exemplar.id)
            })


        exempleFind = ProtocolExemplarFind.objects.all().filter(Protocol = prot)

        protForm = ProtocolFormChange()
        protForm.fields["date"].initial = prot.Date
        protForm.fields["address"].initial = prot.Address
        protForm.fields["coordinates"].initial = prot.Сoordinates
        protForm.fields["description"].initial = prot.Description
        protForm.fields["report"].initial = prot.Note

        choiceGenus = ChoiceGenus()
        choiceGenus.fields["idGenus"].initial = prot.Genus

        choiceThreatExemplar = ChoiceThreatExemplar()
        if prot.Genus :
            listThrId = []
            for thr in Exemplar.objects.filter(Q(Genus=prot.Genus) | Q(Genus=Genus.objects.get(Name="Все"))):
                if not ProtocolExemplarChoice.objects.all().filter(Protocol = Protocol.objects.get(id = id), Exemplar = thr.id):
                    listThrId.append(thr.id)
            choiceThreatExemplar.fields['idThreatExemplar'].queryset =  Exemplar.objects.filter(id__in = listThrId)
            

        context = {
            'login': login,
            'id': id,
            'prot': prot,
            'exempleChoice': exempleChoice,
            'exempleFind': exempleFind,
            'protForm': protForm,
            'choiceGenus': choiceGenus,
            'ChoiceThreatExemplar': choiceThreatExemplar
        }
        return render(request, template, context)


#Загрузка файла
def protocol_file(request):
    error = -1
    if request.method == 'POST' and request.FILES['myfile']:
        prot = Protocol.objects.get(id = int(request.POST.get("id")))
        prot.Archive = request.FILES['myfile']
        prot.save()

        error=0
        return HttpResponse(json.dumps({'id': int(request.POST.get("id")), 'name': prot.Archive.name}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")


#Удаление протокола
def protocol_thr_delete(request, login, idp, idt):
    ProtocolExemplarChoice.objects.filter(id = int(idt)).delete()
    return HttpResponseRedirect('{}#file_name'.format(reverse("protocol", args=[login, idp])))


#Алгоритм
def protocol_alg(request):
    error = -1
    if request.method == 'POST':
        prot = Protocol.objects.get(id = int(request.POST.get("id")))
        prot.Made = "1"
        prot.save()

        ProtocolExemplarFind.objects.filter(Protocol = prot).delete()

        for exempl in ProtocolExemplarChoice.objects.all().filter(Protocol = prot):
            prt = ProtocolExemplarFind()
            prt.Protocol=exempl.Protocol
            prt.Exemplar=exempl.Exemplar
            prt.save()

        error=0
        return HttpResponse(json.dumps({'id': int(request.POST.get("id")), 'name': prot.Archive.name}), content_type="application/json")
    return HttpResponse(json.dumps({'id': error}), content_type="application/json")
