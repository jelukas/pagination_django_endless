# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from endless_pagination.decorators import page_template
from .models import City

@page_template('geography/index_page.html')  # just add this decorator
def index(request, template='geography/index.html', extra_context=None):
	cities = City.objects.all()
	context = {'cities': cities}
	if extra_context is not None:
		context.update(extra_context)
	return render_to_response(template,context,context_instance=RequestContext(request))