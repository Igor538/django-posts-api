from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, serializers
from .models import Post

# ----------------------
# API
# ----------------------
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        exclude = []

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-created")

# ----------------------
# Páginas Django
# ----------------------
def inicio(request, editar_id=None):
    posts = Post.objects.all()
    post_editar = None
    if editar_id:
        post_editar = get_object_or_404(Post, id=editar_id)
    return render(request, "inicio.html", {"posts": posts, "post_editar": post_editar})

def postar(request):
    error = ""
    if request.method == "POST":
        autor = request.POST.get("autor")
        conteudo = request.POST.get("conteudo")
        if autor and conteudo:
            Post.objects.create(autor=autor, conteudo=conteudo)
            return redirect("inicio")
        else:
            error = "Preencha todos os campos!"
    return render(request, "postar.html", {"error": error})

def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    error = ""
    if request.method == "POST":
        autor = request.POST.get("autor")
        conteudo = request.POST.get("conteudo")
        if autor and conteudo:
            post.autor = autor
            post.conteudo = conteudo
            post.save()
            return redirect("inicio")
        else:
            error = "Preencha todos os campos!"
    return render(request, "inicio.html", {"posts": Post.objects.all(), "post_editar": post, "error": error})

def remover_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("inicio")
