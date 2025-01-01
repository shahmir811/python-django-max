from django.shortcuts import get_object_or_404, render

from .models import Post


def get_date(post):
  return post['date']

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