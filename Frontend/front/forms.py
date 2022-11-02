from django import forms

class FileForm(forms.forms):
    forms.FileField(label="file")
