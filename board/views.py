from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def IndexView(request):
	return render(request, 'index.html')

def BoardView(request, link):
	board = BoardModel.objects.filter(link=link)[0]
	thread_form = ThreadForm()
	return render(request, 'board/board_base.html', {'board':board, 'form':thread_form})

def CreateThreadView(request):
	form = ThreadForm(request.POST)
	print(form.content)
	return HttpResponse(content)