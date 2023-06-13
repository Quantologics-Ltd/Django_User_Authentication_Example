from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='upload/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Doc(models.Model):
    #client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    file = models.FileField(upload_to="clients_docs", null=True, blank=True)

    def __str__(self):
        return str(self.name)


