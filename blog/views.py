from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Blog, BlogComment


class BlogHomeView(ListView):
    template_name = 'blog/blog_home.html'
    paginate_by = 4

    def get_queryset(self):
        return Blog.objects.all().order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['title'] = 'Blog - GymCounselor'
        context['latest_post'] = Blog.objects.all().order_by('-pk')[:3]
        return context


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        blog_id = self.kwargs['pk']
        return Blog.objects.get(pk=blog_id)

    def get_context_data(self, **kwargs):
        context = {
            'object': self.get_object(),
            'title': self.object.blog_title,
            'latest_post': Blog.objects.all().order_by('-pk')[:3],
            'comments': BlogComment.objects.filter(comment_blog=self.object.pk).order_by('-pk')[:3],
            'comment_count': BlogComment.objects.filter(comment_blog=self.object.pk).count()
        }
        return context


class BlogFilterView(ListView):
    template_name = 'blog/blog_home.html'

    def get_queryset(self):
        search = self.request.GET.get('search', None)
        tag = self.request.GET.get('tag', None)
        if search is not None:
            return Blog.objects.filter(blog_title__icontains=search)
        elif tag is not None:
            return Blog.objects.filter(blog_category__icontains=tag)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogFilterView, self).get_context_data(**kwargs)
        context['latest_post'] = Blog.objects.all().order_by('-pk')[:3]
        context['title'] = 'Blog - GymCounselor'
        return context


#
# # @login_required
# def add_comment(request, post_id):
#     comment = request.POST.get('comment', None)
#     if comment is None:
#         comment = request.session.get('post_comment')
#         print(comment)
#
#     if request.user.is_authenticated:
#         BlogComment.objects.create(
#             comment_blog_id=post_id,
#             comment=comment,
#             comment_user=request.user
#         )
#         return redirect('blog_detail', post_id)
#
#     else:
#         request.session['post_comment'] = comment
#         return redirect('login')


def add_comment(request, post_id):
    comment = request.POST.get('comment', None)
    email = request.POST.get('email', None)
    BlogComment.objects.create(
        comment_blog_id=post_id,
        comment=comment,
        comment_user=email
    )
    return redirect('blog_detail', post_id)
