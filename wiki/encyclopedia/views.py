from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import random as r
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def title(request, title):
    content = util.get_entry(title)

    if content is None:
        return render(request, "encyclopedia/errorpage.html")

    content = markdown2.markdown(content)

    page = render(request, "encyclopedia/entry.html", {"content": content, "title": title})

    return page

def search(request):
    query = request.GET.get("q")
    entries_list = util.list_entries()

    storage = []

    for entry in entries_list:
        if query == entry:
            return HttpResponseRedirect(reverse("title", args=[entry]))
        elif query in entry:
            storage.append(entry)

    return render(request, "encyclopedia/search.html", {"results": storage})

def new(request):
    if request.method == "POST":
        entries_list = util.list_entries()

        title = request.POST.get("title")
        content = request.POST.get("content")

        if title in entries_list:
            return render(request, "encyclopedia/errorpage.html")

        util.save_entry(title, content)

        return HttpResponseRedirect(reverse("title", args=[title]))

    return render(request, "encyclopedia/new.html")

def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("content")

        util.save_entry(title, content)

        return HttpResponseRedirect(reverse("title", args=[title]))
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {"title": title, "content": content})

def random(request):
    entries_list = util.list_entries()
    random_entry = r.choice(entries_list)

    return HttpResponseRedirect(reverse("title", args=[random_entry]))
