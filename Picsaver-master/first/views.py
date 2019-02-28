#from django.shortcuts import render, get_object_or_404
####from django.template import loader
#from .models import Album
# Create your views here.

#def index(request):
 #   all_album = Album.objects.all()
    ####template = loader.get_template('first/index.html')
  #  context = {'all_album': all_album}
  #  return render(request, 'first/index.html', context)
   #### return HttpResponse(template.render(context, request))

#def detail(request, album_id):
 #   album = get_object_or_404(Album, pk=album_id)
  #  context = {'album': album}
   # return render(request, 'first/detail.html', context)

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Album

class IndexView(ListView):
    template_name = 'first/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(DetailView):
    model = Album
    template_name = 'first/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['placeName', 'city', 'state', 'country', 'description', 'picture']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['placeName', 'city', 'state', 'country', 'description', 'picture']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('picSaver:index')

