from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Slide,Critica,Obra
from .forms import ContatoForm
from django.core.paginator import Paginator
from django import template
from django.db.models import Count
from django.core.mail import send_mail

def jb_index(request):
    #posts = Post.objects.all()
    titl='index'
    return render(request, 'index.html', {'titl': titl})

def slide_home(request):
    slides = Obra.objects.filter(slide=1).order_by('?')[:15]
    titl='Home'
    return render(request, 'home.html', {'slides': slides,'titl': titl})
    
def obra_list(request):

    variables = request.GET.copy()
    busca = ''

    pagina=1
    p = Paginator(Obra.objects.all(), 35)
    if 'q' in variables:
    	busca = request.GET.get('q')
    	p = Paginator(Obra.objects.filter(nome__contains=busca), 35)

    if 'p' in variables:
    	pagina = int(request.GET.get('p'))

    totalimagens = p.count
    totalpaginas = p.num_pages
    vai=1

    lim=6
    if ((pagina - (lim/2)) <= 1):
    	inicio=1
    elif ((pagina + (lim/2)) >= totalpaginas):
        inicio=int(totalpaginas - (lim-1))
    else:
        inicio=int(pagina - (lim/2))

    if ((inicio + (lim-1)) >= totalpaginas):
        fim=int(totalpaginas)
    else:
        fim=int(inicio+(lim-1))
    

    page = p.page(pagina)
    obras = page.object_list

    if obras.count() > 28:
    	ultima = 27
    else:
    	ultima = (int(obras.count()/7) * 7) - 1

    if(pagina < totalpaginas):
    	proxima = pagina + 1
    	if(pagina > 1):
    		anterior = pagina - 1
    	elif(pagina == 1):
    		anterior = totalpaginas;
    elif(pagina == totalpaginas):
    	proxima = 1
    	anterior = pagina - 1


    #obras = Obra.objects.all().order_by('id')[:35]
    lista = list(range(inicio,(fim + 1)))
    titl='Obras'
    return render(request, 'obras.html', {'obras': obras,'titl': titl,'totalpaginas': totalpaginas,'lim': lim,'pagina': pagina,'inicio': inicio,'fim': fim,'proxima': proxima,'anterior': anterior,'lista': lista,'ultima': ultima,'busca': busca})

def jb_biografia(request):
    #posts = Post.objects.all()
    titl='Biografia'
    return render(request, 'biografia.html', {'titl': titl})

def critica_list(request):
    criticos = Critica.objects.exclude(exibe_menu=0)
    criticas = Critica.objects.all()
    titl='Críticas'
    return render(request, 'critica.html', {'criticas': criticas,'criticos': criticos,'titl': titl})
    
def jb_contato(request):
    titl='Contato'
    sucesso = ""
    slides1 = Obra.objects.filter(slide=1).order_by('?')[:15]
    slides2 = Obra.objects.filter(slide=1).order_by('?')[:15]
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            #mail = form.save(commit=False)
            titulo = request.POST['tit_mensagem']
            mensagem = request.POST['mensagem']
            nome = request.POST['nome']
            mail = request.POST['mail']
            telefone = request.POST['telefone']
            celular = request.POST['celular']
            rodape_mensagem = ""
            if telefone or celular:
            	if telefone:
            		rodape_mensagem =  rodape_mensagem + "Telefone: " + telefone
            	if telefone and celular:
            		rodape_mensagem =  rodape_mensagem + " - "
            	if celular:
            		rodape_mensagem =  rodape_mensagem + "Celular: " + celular
            mensagem = mensagem + "\r\n\r\n" + rodape_mensagem
            send_mail(titulo, mensagem, 'jeremias.bezerra@gmail.com', ['jeremias.bezerra@gmail.com', nome + " <" + mail + ">"],fail_silently=True)
            sucesso = "Sua Mensagem foi Enviada com Sucesso!"

    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form,'slides1': slides1,'slides2': slides2,'sucesso':sucesso})
