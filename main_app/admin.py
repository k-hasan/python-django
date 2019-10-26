from django.contrib import admin
from . models import QuoteCategory
from . models import Quote
from . models import PostCategory
from . models import Post


admin.site.register(QuoteCategory)
admin.site.register(Quote)
admin.site.register(PostCategory)
admin.site.register(Post)

# Register your models here.
