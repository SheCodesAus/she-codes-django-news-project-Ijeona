from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context
class EditStoryView(generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html' 

class All_stories_View(generic.ListView):
    template_name = 'news/allstories.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class AuthorStories (generic.ListView): 
    template_name = 'news/authorstories.html'
    context_object_name = 'stories'

    def get_queryset(self):
       return NewsStory.objects.filter(author=self.kwargs['pk'])
       
class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    context_object_name = 'story'
    template_name = 'news/deleteStory.html' 
    success_url = reverse_lazy('news:index')