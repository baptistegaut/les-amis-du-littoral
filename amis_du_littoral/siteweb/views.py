from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import io
from siteweb.models import Bulletin
# Create your views here.

# views of home page

def association(request):

	return render( request, 'siteweb/association.html')

def bureau(request):

	return render( request, 'siteweb/bureau.html')

def histoire(request):

	return render( request, 'siteweb/histoire.html')

def preoccupations(request):

	return render( request, 'siteweb/preoccupations.html')

def avenir(request):

	return render( request, 'siteweb/avenir.html')

def participations(request):

	return render( request, 'siteweb/participations.html')

# views of bulletin page

def bulletins(request):

	bulletins = Bulletin.objects.all()

	return render( request, 'siteweb/bulletins.html', {'tous_les_bulletins': bulletins})

def bulletin(request, numero):
	image_data = open("" + numero +".pdf", "rb").read()
	return HttpResponse(image_data, content_type='application/pdf')

# views of contact page

def contact(request):

	return render( request, 'siteweb/nouscontacter.html')

def rejoigneznous(request):

	return render( request, 'siteweb/rejoigneznous.html')

# views of documents

def documents(request):
	return render(request, 'siteweb/documents.html')

def lddl(request):
	image_data = open("lddl.pdf", "rb").read()
	return HttpResponse(image_data, content_type='application/pdf')

def abp(request):
	image_data = open("abp.pdf", "rb").read()
	return HttpResponse(image_data, content_type='application/pdf')





