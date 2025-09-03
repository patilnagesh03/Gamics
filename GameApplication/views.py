from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def TicTacToe(request):
    return render(request, 'Games/tictactoe.html')


@login_required(login_url='/login/')
def Tetris(request):
    return render(request, 'Games/tetris.html')

@login_required(login_url='/login/')
def Snake(request):
    return render(request, 'Games/snake.html')


@login_required(login_url='/login/')
def rock(request):
    return render(request, 'Games/rock.html')

