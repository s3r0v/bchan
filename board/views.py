from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def IndexView(request):
	return render(request, 'index.html')

def BoardView(request, link):
	board = BoardModel.objects.filter(link=link)[0]
	thread_form = ThreadForm()
	threads = ThreadModel.objects.filter(board=board)
	return render(request, 'board/board_base.html', {'board':board, 'form':thread_form, 'threads':threads})

def CreateThreadView(request):
	form = ThreadForm(request.POST)
	if form.is_valid():
		content = form.cleaned_data['content']
		new_thread = ThreadModel(content=content, board=BoardModel.objects.filter(link="b")[0])
		new_thread.save()
		return redirect("../../b")