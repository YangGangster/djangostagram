from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormView
from django.http import Http404

from dspost.models import Dspost, Tag
from dspost.forms import PostForm

from django.core.paginator import Paginator

from django.utils.decorators import method_decorator
from dsuser.decorators import login_required

from dsuser.models import Dsuser

class PostListView(ListView):
    template_name = 'post_list.html'
    model=Dspost
    paginate_by = 4

    def get_queryset(self):
        posts = Dspost.objects.all().order_by('-registered_date')
        page = int(self.request.GET.get('p',1))
        paginator = Paginator(posts, 4)
        queryset = paginator.get_page(page)
        return queryset

@method_decorator(login_required,name="dispatch")
class PostCreationView(FormView):
    template_name = 'post_creation.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):

        user=None
        
        try:
            user = Dsuser.objects.get(userId=self.request.session['user'])
        except Dsuser.DoesNotExist :
                self.add_error('userId','아이디가 없습니다.')
        
        tags = form.data.get('tags').split(',')
        

        dspost = Dspost.objects.create(
            title = form.data.get("title"),
            author = user,
            img_url = form.data.get("img_url"),
            contents = form.data.get("contents")
        )

        for tag in tags:
            if not tag:
                continue

            _tag, _ = Tag.objects.get_or_create(name=tag.strip())

            dspost.tags.add(_tag)

        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Dspost.objects.all()
    context_object_name = 'post'

    def get_object(self,queryset=None):
        try:
            return Dspost.objects.get(pk=self.kwargs['pk'])
        except Dspost.DoesNotExist:
            raise Http404("404")

def page_not_found(request,exception):
    response = render(request,"404.html",{})
    return response

