from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import CommentForm
from .models import Post


def get_date(post):
  return post['date']


class StartingPageView(ListView):
  model = Post
  template_name = "blog/index.html"
  context_object_name = "posts"

  def get_queryset(self):
    return Post.objects.order_by('-created_at')[:3]
  

class AllPostsView(ListView):
  model = Post
  template_name = "blog/all-posts.html"
  context_object_name = "all_posts"
  ordering = ['-date']


# class SinglePostView(DetailView):
#   model = Post
#   template_name = "blog/post-detail.html"
#   context_object_name = "post"

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     post = self.get_object()
#     context['post_tags'] = post.tags.all()
#     context['comment_form'] = CommentForm()
#     return context

class SinglePostView(View):
  template_name = "blog/post-detail.html"

  def is_stored_posts(self, request, post_id):
    stored_posts = request.session.get('stored_posts')
    if stored_posts is not None:
      is_saved_for_later = post_id in stored_posts
    else:
      is_saved_for_later = False

    return is_saved_for_later

  def get(self, request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
      "post": post,
      "post_tags": post.tags.all(),
      "comment_form": CommentForm(),
      "comments": post.comments.all().order_by('-created_at'),
      "saved_for_later": self.is_stored_posts(request, post.id)
    }
    return render(request, self.template_name, context)

  def post(self, request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()
      return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

    else:
      context = {
        'post': post,
        "post_tags": post.tags.all(),
        'comment_form': comment_form,
        "comments": post.comments.all().order_by('-created_at'),
        "saved_for_later": self.is_stored_posts(request, post.id)
      }
      return render(request, 'blog/post-detail.html', context)
  

class ReadLaterView(View):

  def get(self, request):
    stored_posts = request.session.get('stored_posts')
    context = {}

    if not stored_posts or len(stored_posts) == 0:
      context['posts'] = []
      context['has_posts'] = False
    else:
      posts = Post.objects.filter(id__in=stored_posts)
      context['posts'] = posts
      context['has_posts'] = True

    print(context)

    return render(request, 'blog/stored-posts.html', context)

  def post(self, request):
    stored_posts = request.session.get('stored_posts')
    post_id = int(request.POST['post_id'])

    if not stored_posts:
      stored_posts = []

    if post_id not in stored_posts:
      stored_posts.append(post_id)
    else:
      stored_posts.remove(post_id)

    request.session['stored_posts'] = stored_posts
    return HttpResponseRedirect('/')
    


# ########################################################################
# ########################################################################
# ######### Below are the function-based view implementations ############
# ########################################################################
# ########################################################################


# Create your views here.
def starting_page(request):
  # In the following query, django will automatically sort the posts by created_at in descending order
  # and return the first 3 posts. Not getting all the posts from the database and then slicing them.
  all_posts = Post.objects.all().order_by('-created_at')[:3]
  return render(request, "blog/index.html", {
    "posts": all_posts
  })


def posts(request):
  all_posts = Post.objects.all().order_by('-created_at')
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })


def post_detail(request, slug):
  identified_post = get_object_or_404(Post, slug=slug)
  return render(request, "blog/post-detail.html", {
    "post": identified_post,
    "post_tags": identified_post.tags.all()
  })