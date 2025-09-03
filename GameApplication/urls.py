from django.urls import path
from .import views

urlpatterns = [
    path('tictactoe/', views.TicTacToe, name='tictactoe'),
    path('tetris/', views.Tetris, name='tetris'),
    path('snake/', views.Snake, name='snake'),
    path('rock/', views.rock, name='rock'),
    
    
    
]