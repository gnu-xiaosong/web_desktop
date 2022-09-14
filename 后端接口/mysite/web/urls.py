from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('getUserMiniApp/', views.getUserMiniApp),
    path('api/getUserMiniApp/', views.getUserMiniApp),

    path('login/', views.login),
    path('api/login/', views.login),

    path('postShell/', views.postShell),
    path('api/postShell/', views.postShell),

    path('getUserWallpaper/', views.getUserWallpaper),
    path('api/getUserWallpaper/', views.getUserWallpaper),

    path('userFileSystem/', views.userFileSystem),
    path('api/userFileSystem/', views.userFileSystem),

    path('getFileContent/', views.getFileContent),
    path('api/getFileContent/', views.getFileContent),

    path('saveFileContent/', views.saveFileContent),
    path('api/saveFileContent/', views.saveFileContent),

    path('getFileContent/', views.getFileContent),
    path('api/getFileContent/', views.getFileContent),

    path('uploadFiles/', views.uploadFiles),
    path('api/uploadFiles/', views.uploadFiles),

    path('createDirFile/', views.createDirFile),
    path('api/createDirFile/', views.createDirFile),
]