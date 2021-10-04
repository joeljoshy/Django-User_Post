from django.urls import reverse_lazy,reverse
from .forms import PostForm
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.views import generic
from django.views.generic import ListView,DetailView
from django.http import JsonResponse,HttpResponseRedirect
from django.core import serializers

from django.core.paginator import Paginator




def PostView(request):

    form = PostForm()

    return render(request,'post.html',{'form' : form})

def addPost(request):
    if request.is_ajax and request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            ser_instance = serializers.serialize('json',[instance])

            return JsonResponse({'instance':ser_instance},status=200)


        else:

            return JsonResponse({'error':form.errors},status=400)
    return JsonResponse({'error':''},status=400)

def listpost(request):

    posts = Post.objects.all().order_by('id')

    post_paginator = Paginator(posts,5)
    page_num = request.GET.get('page')

    page = post_paginator.get_page(page_num)

    context = {
        'count': post_paginator.count,
        'page':page
    }

    return render(request,'listall.html',context)
#
# class ListAll(ListView):
#     model = Post
#     template_name = 'listpost.html'
#     # ordering = ['-date']
#
#     def get_ordering(self):
#         ordering = self.request.GET.get('ordering', '-date')
#         # validate ordering here
#         return ordering

class PostDetail(DetailView):
    model = Post
    template_name = 'postdetails.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data(**kwargs)
        item = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = item.total_likes()
        liked = False
        if item.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

def likeView(request,pk):

    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True


    # post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))
