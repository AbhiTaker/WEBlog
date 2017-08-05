from django.contrib import admin

# Register your models here.
from .forms import SignUpForm, PostForm, CommentForm

from .models import Comment,Post,SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","name"]
	form = SignUpForm
	#class Meta :
		#model = SignUp
			


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(SignUp,SignUpAdmin)
