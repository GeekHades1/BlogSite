from django.shortcuts import render
import time
# Create your views here.

def blog_index(request):
    t = time.asctime()
    context = {
        'test': '测试内容',
        'welcome': '欢迎您！',
        'datatime': str(t),
    }
    return render(request, 'blog_index.html',context)
