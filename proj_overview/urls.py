from django.urls import path
from . import views
app_name = 'proj_overview' # 各ルートがどのアプリケーションのビューなのかを指定
urlpatterns = [
    # proj_overviewのURLの場合、proj_overviewのurls.pyを呼び出す
    path('',views.showProjOverviews,name='proj_article'),
    # proj_overviewの後に整数型のidが来たら、views.pyのdetail関数を呼び出す
    path('<int:id>', views.detail, name='detail')
]