from django.urls import path

from . import views

urlpatterns = [
path('shows', views.shows), 
path('shows/new', views.new),
path('create', views.create),
path('shows/<int:show_id>/edit', views.edit),
path('shows/<int:show_id>', views.show_view),
path('delete/<int:show_id>',views.delete),
path('update/<int:show_id>', views.update),
path('', views.root),
]