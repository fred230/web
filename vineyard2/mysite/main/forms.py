from django import forms

from .models import Post, prayer

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('title', 'slug', 'author', 'content', 'status','image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }



class EditBlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'status')
        

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


    
   


class PrayerForm(forms.ModelForm):
    class Meta:
        model = prayer
        fields = ['name', 'email', 'prayerItem']
    