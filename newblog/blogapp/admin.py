from django.contrib import admin
from blogapp.models import *
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'author', 'less_content', 'publish', 'created', 'updated', 'status', 'Pimage']
	list_filter = ['status', 'author']
	search_fields = ('author', 'title', 'body')
	raw_id_fields = ('author',)
	ordering = ['status', 'publish']
	prepopulated_fields = {'slug': ('title',)}

	def less_content(self, obj):
		# This function will extract the first 30 charactracters
		# return obj.content[:30]
		return format_html(f'<span style = "color:#03A9F4">{obj.body[:32]}</span>')

admin.site.register(Post, PostAdmin)

