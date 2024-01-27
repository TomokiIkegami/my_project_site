from django.urls import path
from . import views
app_name = 'proj_overview' # 各ルートがどのアプリケーションのビューなのかを指定
urlpatterns = [
    # proj_overviewのURLの場合、proj_overviewのurls.pyを呼び出す
    path('all_projects',views.showAllProjects,name='all_projects'),
    # 何も指定しない場合、top_pageにアクセス
    path('',views.top_page, name='top_page'),
    # proj_overviewの後に整数型のidが来たら、views.pyのdetail関数を呼び出す
    path('<int:id>', views.detail, name='detail')
]