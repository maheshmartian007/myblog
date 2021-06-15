from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic import ListView
from blogapp.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def PostListView(request, tag_slug = None):
	post_list = Post.objects.all()
	tag = None

	if tag_slug:
		tag = get_object_or_404(Tag, slug = tag_slug)
		post_list = post_list.filter(tags__in = [tag])


	paginator = Paginator(object_list = post_list, per_page = 5)
	page_number = request.GET.get('page')

	count = int(request.COOKIES.get('count',0))
	new_count = count+1

	my_dict = {'post_list': post_list, 'tag': tag , 'new_count': new_count}
	request.session['new_count'] = new_count
	
	response = render(request = request, template_name ="blogapp/tech-index.html" , context= my_dict)
	response.set_cookie('count', new_count, max_age=60)

	return  response

	

def post_detail_view(request, year, month, day, post):

	
	post = get_object_or_404(Post, slug = post, status= 'published', publish__year = year, publish__month=month, publish__day = day)
	print(post, 'this is post')



	my_dict = {'post': post}
	return render(request = request, template_name = 'blogapp/tech-single.html', context= my_dict)

# def single_tech(request):
# 	return render(request = request, template_name = "blogapp/tech-single.html")