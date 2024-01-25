from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import ArticleInfo # 記事の情報が入ったDB

# Create your views here.
# 記事の情報を辞書に格納して、proj_article.htmlに返す
def showProjOverviews(request):
    context = {}
    all_article = ArticleInfo.objects.all() # 全記事を取得
    context = {'all_article':all_article,}  # contextに全記事を格納
    print(all_article[0].article)
    return render(request, 'proj_overview/proj_article.html',context)   

def detail(request, id):    # ルートで指定した値をid変数として取り出す
    article = get_object_or_404(ArticleInfo, pk=id) # 指定したidのレコードに対応するオブジェクトを取得（pk=primary key、データを識別するための目印）
    context = {'article':article,} # contextにidで指定したarticleを渡す
    return render(request, 'proj_overview/detail.html',context) # テンプレートに渡す
