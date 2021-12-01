from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, PostCategory
from .filters import PostFilter



class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'postList'
    queryset = Post.objects.order_by('-created')
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class SearchList(PostList):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'postView'


class PostCreateView(CreateView):
    permission_required = ('news.add_post',
                           'news.change_post')
    template_name = 'add.html'


    def post(self, request, *args, **kwargs):
        post = Post(
            id_author=Author.objects.get(id_user=request.user),
            header=request.POST['header'],
            text=request.POST['text']
        )
        post.save()

        for id in request.POST.getlist('category'):
            postCategory = PostCategory(id_post=post, id_category=Category.objects.get(pk=id))
            postCategory.save()


class PostDeleteView(DeleteView):
    permission_required = ('news.delete_post',)
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class PostUpdateView(UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'edit.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)