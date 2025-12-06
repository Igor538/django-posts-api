from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length=30)
    conteudo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor}"

    class Meta:
        ordering = ['-created']
