from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


urlpatterns =[
    path('', PostListView.as_view() ,name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view() ,name='user-posts'),
    path('post/new/', PostCreateView.as_view() ,name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view() ,name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() ,name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() ,name='post-delete'),
    path('about/',views.about,name='blog-about'), 
]

# when trying to add variables to our route we can write it as shown above

#in case of create and update form the template default is named as post_form.html
#in case of delete the template post_confirm_delete
