from django.contrib import admin
from reviewsite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')
    
admin.site.register(Post,PostAdmin)
# Register your models here.
