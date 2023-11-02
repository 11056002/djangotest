from django.shortcuts import render
from datetime import datetime
from reviewsite.models import Post

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html',locals())

'''
def homepage(request):
    posts = Post.object.all()
    post_list = list()
    for count, post in enumerate(posts):
        post_list.append("No.{}".format(str(count))+str(post)+"<br>")
    return HttpResponse(post_list)
# Create your views here.
'''
