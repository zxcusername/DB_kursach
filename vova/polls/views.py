from curses.ascii import SO
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Song, Dude, Review
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import SongForm, ReviewForm




# Create your views here.
def index(request):
    return render(request, 'polls/list.html')

def medved(request):

    return HttpResponse("<h2>уголовник</h2>")

    
def view_my_profile(request):
    try:

        name_dude = request.user
        # prunt(name_dude)/
        if str(name_dude)  == 'admin': return redirect('http://127.0.0.1:8000/admin')
        dude = Dude.objects.get(user = name_dude)
    except:
        raise Http404("Такого dude не существует")

    if dude.is_judge:
        judge_flag = True
        review_list = dude.review_set.all()
        return render(request, 'polls/myprofile.html', {'user':dude, 'judge_flag':judge_flag, 'review_list':review_list}) 
    else:
        judge_flag = False
        song_list = dude.song_set.all()
        return render(request, 'polls/myprofile.html', {'user':dude, 'judge_flag':judge_flag, 'song_list':song_list})

def view_dude(request, dude_id):
    # print("!!!!!!", request.user.id)
    try:
        dude = Dude.objects.get(id=dude_id)
    except:
        raise Http404("Такого dude не существует")
    
    if (str(request.user)  == str(dude) ):
        adress = 'polls/myprofile.html' 
    else: adress = 'polls/userpage.html'

    if dude.is_judge:
        review_list = dude.review_set.all()
        return render(request, adress, {'user':dude, 'review_list':review_list}) 
    else:
        song_list = dude.song_set.all()
        return render(request, adress, {'user':dude, 'song_list':song_list})
    

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

def add_song(request):
    error = ''
    if request.method == 'POST':
        form = SongForm(request.POST)
        # form.author = request.user.username
        print (form)
        print (form.cleaned_data)
        # form.cleaned_data.author = request.user.username
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/myprofile')
        else:
            # return print(form)
            error = 'Форма была неверной'
            
    print (request.user.username)
    form = SongForm()
    data = {
        'form': form,
        'error': error

    }
    return render(request, 'polls/add_song.html', data)

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            # return redirect('myprofile')
        else:
            print("!!!!!!!!!!!!!!!!!!", form.lirycs)
            error = 'Форма была неверной'
    
    form = ReviewForm()
    data = {
        'form':form,

    }

    return render(request, 'polls/add_review.html', {'form': form})