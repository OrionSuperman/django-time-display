from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line
import datetime
from time import strftime
def index(request):
	now = datetime.datetime.now()
	year = now.strftime('%Y')
	print year
	time_now = {
	'year' : now.strftime('%Y'),
	'month' : now.strftime('%B'), 
	'day' : now.strftime('%A'),
	'time' : now.strftime('%X')
	}
	print time_now
	return render(request, 'givetime/index.html', time_now) # updated this line 
