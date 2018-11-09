from django.shortcuts import render, get_object_or_404, redirect
from products.models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.template import context
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from products.forms import SignUpForm, CreateProjectForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.db.models import OuterRef, Subquery, Count, Min
from django.db.models import DecimalField, IntegerField, ExpressionWrapper
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request,template,context)

def login(request):
	user = request.user
	if user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user_login = authenticate(request, username=username, password=password)

			if user_login is not None:
				messages.success(request, "Welcome back to Basket Compare")
				django_login(request, user_login)
				return redirect('/')

	else:
		form = AuthenticationForm()

	context = {'form': form}
	template = "registration/login.html"
	return render(request, template, context)

def logout(request):
	django_logout(request)
	messages.success(request, "You are now logged out. See you again soon!")
	return redirect('/')

def about(request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)

def pdp(request, code=None, slug=None):
	user = request.user
	master_product = Product.objects.get(bc_sku=code, product_slug=slug, product_type="master_product")
	compared_products = Product.objects.filter(bc_sku=code, product_type="compared_product").order_by('product_price')
	context = {
		'master_product': master_product,
		'compared_products': compared_products,
	}
	template = 'pdp.html'
	if user.is_authenticated:
		user_favourites_count = user.profile.favourites.count()
		context.update({
			'user_favourites_count': user_favourites_count,
		})
		try:
			projects = Project.objects.filter(user=user)
		except ObjectDoesNotExist:
				projects = None
		context.update({
			'projects': projects
		})

	return render(request, template, context)

def plp(request, subcategory_slug):
	template = 'plp.html'
	subcategory = get_object_or_404(SubCategory, subcategory_slug=subcategory_slug)

	subquery = Product.objects.filter(bc_sku=OuterRef('bc_sku')).values('bc_sku').annotate(product_count=Count('*')-1).annotate(min_price=Min('product_price'))
	master_products_list = Product.objects.filter(product_type='master_product').annotate(product_count=Subquery(subquery.values('product_count'))).annotate(min_price=ExpressionWrapper(Subquery(subquery.values('min_price')), output_field=DecimalField(decimal_places=2, max_digits=10))).order_by('product_description')

	paginator = Paginator(master_products_list, 8)
	page = request.GET.get('page')
	products = paginator.get_page(page)
	context = {
		'subcategory': subcategory,
		'products': products,
		'products_list': master_products_list,
	}

	return render(request, template, context)

def category_landing(request, category_slug):
	template = 'category_landing.html'
	category = get_object_or_404(Category, category_slug=category_slug)
	sub_categories = SubCategory.objects.filter(category_name=category)
	context = {
		'category': category,
		'sub_categories': sub_categories,
	}

	return render(request, template, context)

def search_page(request):
	template = 'search.html'
	query = request.GET.get("q")
	
	if query:
		query_list = Product.objects.filter(product_type="master_product", product_description__icontains=query)
		paginator = Paginator(query_list, 8)
		page = request.GET.get('page')
		products = paginator.get_page(page)
		context = {
			'products': products,
			'q': query,
			'query_list': query_list
		}
		return render(request, template, context)

	elif query is "":
		return redirect('/')

def sign_up(request):
	user = request.user
	if user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			# new_user = form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			new_user = User.objects.create_user(username, email=email, password=password)
			login(request, new_user)
			messages.success(request, "Thanks For Registering!")
			return redirect('/')
		
	else:
		form = SignUpForm()

	template = "registration/register.html"
	context = {'form': form}
	return render(request, template, context)



def favourites(request):

	user = request.user

	if request.user.is_authenticated:
		profile = Profile.objects.get(user=user)

		if request.method == 'POST':

			if 'addtofavourites' in request.POST: #Name of submit button
				product_code = int(request.POST['bc_sku'])
				product = Product.objects.get(bc_sku=product_code, product_type="master_product")
				user.profile.favourites.add(product)

			elif 'removefromfavourites' in request.POST:
				product_code = int(request.POST['bc_sku'])
				product = Product.objects.get(bc_sku=product_code, product_type="master_product")
				profile.favourites.remove(product)

			elif 'deleteallfavourites' in request.POST:
				profile.favourites.all().delete()

			return redirect('registration/favourites')	

		else:
			subquery = Product.objects.filter(bc_sku=OuterRef('bc_sku')).values('bc_sku').annotate(min_price=Min('product_price'))
			favourites = user.profile.favourites.all().annotate(min_price=ExpressionWrapper(Subquery(subquery.values('min_price')), output_field=DecimalField(decimal_places=2, max_digits=10))).order_by('product_description')
			context = {
				'favourites': favourites
				}
			template = "registration/favourites.html"
			return render(request, template, context)

	else:
		return redirect('register')
		

def account(request):
	user = request.user
	if user.is_authenticated:	
		context = locals()
		template = 'registration/account.html'
		return render(request,template,context)
	else:
		return redirect('/')

def my_projects(request):
	user = request.user
	if request.user.is_authenticated:
		template = "registration/my_projects.html"
		try:
			projects = Project.objects.filter(user=user)
		except ObjectDoesNotExist:
				projects = None
		context = {
			'projects': projects
		}
		
		if request.method == 'POST':

			if 'delete-project' in request.POST:
				project_name = request.POST['project_name']
				project = Project.objects.get(user=user, name=project_name)
				Project.delete(project)

			if 'create-project-item' in request.POST:
				product_code = request.POST['bc_sku']
				form_project_slug = request.POST.get('project_slug')
				form_project_quantity = int(request.POST['project_quantity'])

				project= Project.objects.get(user=user, project_slug=form_project_slug)
				master_item = Product.objects.get(bc_sku=product_code, product_type="master_product")


				p = Project_Item.objects.create(quantity=form_project_quantity, project=project)
				p.item.add(master_item)





		return render(request, template, context)

	else:
		return redirect('register')



def create_project(request):
	user = request.user
	template = "registration/create_project.html"
	context = {}

	if request.method == 'POST':
		if 'create-project' in request.POST:
			form = CreateProjectForm(request.POST)
			if form.is_valid():
				try:
					project = form.save(commit=False)
					project.user = request.user
					form.save()
					return redirect('my-projects')
				except IntegrityError:
					e = "You can't have two projects with the same name"
					form.add_error(None, e)
					return render(request, template, context={"form": form})
	else:
		form = CreateProjectForm()

	context = {
	'form': form
	}
					
	return render(request, template, context)

def project(request, project_slug):
	user = request.user
	str_project_slug = str(project_slug)
	user_string = str(user.username)
	if request.user.is_authenticated:
		template = "registration/project.html"
		project = Project.objects.get(user=user, project_slug=project_slug)
		project_items = project.project_item_set.all()
		# for p in project_items:
		# 	q = p.values('bc_sku')
		# 	bc_sku_list.append(q)



		context = {
			'project': project,
			'project_items': project_items,
		}


		def my_custom_sql():
			with connection.cursor() as cursor:
				SQL = "SELECT DISTINCT t1.bc_sku, t1.product_description, quantity, merchant_id, Min(product_price), product_price * quantity AS sub_total FROM (SELECT * FROM products_product) t1 INNER JOIN (SELECT DISTINCT bc_sku, quantity FROM products_project a INNER JOIN products_project_item b ON a.id = b.project_id INNER JOIN products_project_item_item c ON b.id = c.project_item_id INNER JOIN products_product d ON d.id = c.product_id WHERE project_slug = %s AND user_id = %s) t2 ON t1.bc_sku = t2.bc_sku WHERE merchant_id = 'basket compare' OR merchant_id IN (SELECT DISTINCT merchant_id FROM products_project a INNER JOIN products_project_item b ON a.id = b.project_id INNER JOIN products_project_merchants c ON a.id = c.project_id WHERE project_slug = %s AND user_id = %s) GROUP BY merchant_id, t1.bc_sku ORDER BY t1.bc_sku, product_price "
				cursor.execute(SQL, [project_slug, user_string, project_slug, user_string])
				row = cursor.fetchall()
				context.update({
					'row': row
				})

			return row

		my_custom_sql()


		return render(request, template, context)

	else:
		return redirect('register')




# with connection.cursor() as cursor:
#     cursor.execute(
#     	"Select * from products_project_item"
#     	)
#     dictfetchall(cursor)
