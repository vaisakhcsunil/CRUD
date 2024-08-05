from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from django.views.generic.edit import CreateView

from .models import person
class hellocreate(CreateView):
    model=person
    template_name='create.html'
    fields=["title","description"]





from django.views.generic.list import ListView
from .models import person
 
class helloList(ListView):
 
    # specify the model for list view
    model = person
    template_name='list.html'




from django.views.generic.detail import DetailView
 
from .models import person
 
class helloDetailView(DetailView):
    # specify the model to use
    model = person
    template_name='detail.html'



from django.views.generic.edit import UpdateView
 
from .models import person
 
class helloUpdateView(UpdateView):
    # specify the model to use
    model = person
    template_name='update.html'
    fields=["title","description"]
    

    success_url ="/"



# import generic UpdateView
from django.views.generic.edit import DeleteView

# Relative import of GeeksModel
from .models import person

class helloDeleteView(DeleteView):
	# specify the model you want to use
	model = person
	template_name='delete.html'
	# can specify success url
	# url to redirect after successfully
	# deleting object
	success_url ="/"
