from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class SnackListView(ListView):
    model = Snack
    template_name = 'snacks/snack_list.html'
    
class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snacks/snack_detail.html'  
    
class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snacks/snack_update.html'
    fields = ['title','purchaser','description']
    
class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snacks/snack_create.html' 
    fields = ['title','purchaser','description']      
    
class  SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snacks/snack_delete.html'
    success_url = reverse_lazy('snack_list')  
        
    