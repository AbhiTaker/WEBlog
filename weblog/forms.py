from django import forms

from models import Post, Comment, SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['name', 'email']

			


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
