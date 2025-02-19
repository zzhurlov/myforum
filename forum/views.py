from django.shortcuts import render
from .models import Topic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def topic_list(request):
    topics = Topic.objects.all()
    paginator = Paginator(topics, 25)

    page_number = request.GET.get("page", 1)
    try:
        topics = paginator.page(page_number)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    return render(request, "forum/topic/topic_list.html", {"topics": topics})
