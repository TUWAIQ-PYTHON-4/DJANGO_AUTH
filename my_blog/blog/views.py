from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import CreateView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)  # render tack 3 paramiters


def post_detail(request, post_id):
    post = get_object_or_404(Post,pk=post_id)  # take tow paramiters
    comments=post.comments.filter(active=True) #comments from models and this line to display commint
    comment_form=CommentForm()
    new_comment=None
    context = {'post': post,
               'comments':comments,
               'comment_form':comment_form,
               }
    #to add commant
    if request.method == 'POST':
        comment_form=CommentForm(data=request.POST) #CommentForm name forms
        if comment_form.is_valid(): #if the value corect--> save
            new_comment=comment_form.save(commit=False)
            new_comment.post = post #mapping with blog
            new_comment.save()
            new_comment = CommentForm()
    else:
        comment_form=CommentForm()

    #retern page
    return render(request, 'blog/detail.html', context)

class PostCreateView(CreateView):
    model=Post
    fields=['title','post_date','content']
    template_name = 'blog/newpost.html'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)



