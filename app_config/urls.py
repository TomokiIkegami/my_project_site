"""
URL configuration for app_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ContactFormView, ContactResultView

urlpatterns = [
    # proj_overviewのURLの場合、proj_overviewのurls.pyを呼び出す
    path('proj_overview/',include('proj_overview.urls')),  
    # 何もURLを指定しない場合（app_config/view.pyで、自動的に「app_folder」にアクセスするように設定済み）
    path('', views.index, name='index'),
    # 管理サイトにアクセスするURL
    path('admin/',admin.site.urls),
    # email送信フォームにアクセスするURL
    path('contact/',ContactFormView.as_view(), name = 'contact_form'),
    # emailの送信結果をユーザーに表示するためのURL
    path('contact/result/',ContactResultView.as_view(), name='contact_result'),
]

# メディアファイル公開用のURL設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
