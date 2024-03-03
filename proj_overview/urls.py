from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap

app_name = 'proj_overview' # 各ルートがどのアプリケーションのビューなのかを指定

sitemaps = {
    'articles': ArticleSitemap,
}

urlpatterns = [
    # proj_overviewのURLの場合、proj_overviewのurls.pyを呼び出す
    path('',views.showAllProjects,name='all_projects'), # メモ：第1引数の文字列を削除すると、URLがアプリ名だけになる（逆に文字を入れるとURLを設定できる）
    # proj_overviewの後に整数型のidが来たら、views.pyのdetail関数を呼び出す
    path('<int:id>', views.detail, name='detail'),
    # サイトマップ用のURL
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='sitemap'),
]