from django import forms
from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='upload/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=500)
    file = forms.FileField()

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )