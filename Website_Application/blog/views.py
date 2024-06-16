from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    # pylint: disable=no-member
    Data = {'Posts': Post.objects.all().order_by('-date_posted')}
    return render(request, 'blog/blog.html', Data)
def post(request, id):
    # pylint: disable=no-member
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})
