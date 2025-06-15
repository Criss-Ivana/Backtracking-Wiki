from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from markdown import markdown
from . import util
import random
class SearchEntryForm(forms.Form):
    entry_search = forms.CharField(
        label="",       
        widget=forms.TextInput(attrs={'placeholder': 'Cauta problema...    ', 'class': 'search-input'})
    )

def index(request):
    entries_ = util.list_entries()
    entry_search = None
    search_list = []
    random_page=random.choice(entries_)
    print(random_page)
    if request.method == "POST":
        form_index = SearchEntryForm(request.POST)
        if form_index.is_valid():
            entry_search = form_index.cleaned_data["entry_search"]
            if entry_search:
                search_list = [entry for entry in entries_ if entry_search.lower() in entry.lower()]
            for entry in entries_:
                    if entry_search.lower() == entry.lower():
                        return redirect('pages:wikipage', entry=entry)
            if len(search_list)==0:
                return redirect('pages:error', error=f'No search results for "{entry_search}"')
    return render(request, "encyclopedia/index.html", {
        "entries": entries_,
        "form": SearchEntryForm(),
        "entry_search": entry_search,
        "search_list" : search_list,
        "random_page" : random_page,
    })


def wiki(request, entry):
    #layout var:
    entries_ = util.list_entries()
    entry_search = None
    search_list = []
    random_page=random.choice(entries_)
    print(random_page)
    if request.method == "POST":
        form_index = SearchEntryForm(request.POST)
        if form_index.is_valid():
            entry_search = form_index.cleaned_data["entry_search"]
            if entry_search:
                search_list = [entry for entry in entries_ if entry_search.lower() in entry.lower()]
            for entry in entries_:
                    if entry_search.lower() == entry.lower():
                        return redirect('pages:wikipage', entry=entry)
            if len(search_list)==0:
                return redirect('pages:error', error=f'No search results for "{entry_search}"')
    #done layout
    if entry not in entries_:
         return redirect('pages:error', error="Page could not be found")
    coded_text=util.get_entry(entry)
    print(coded_text[0])
    link = coded_text[0]
    if isinstance(link, bytes):  # Check if it's a bytes object
        link = link.decode("utf-8")  # Decode it to a string
    if coded_text is None:
        return HttpResponse("The requested page was not found.", status=404)
    content=markdown(coded_text[1])
    return render(request, "encyclopedia/wikipage.html", {
        "entry" : entry,
        "link" : link,
        "content" :content,
        "entries": entries_,
        "form": SearchEntryForm(),
        "entry_search": entry_search,
        "search_list" : search_list,
        "random_page" : random_page,
    })


def error(request, error="Page could not be found"):
    #layout var:
    entries_ = util.list_entries()
    entry_search = None
    search_list = []
    random_page=random.choice(entries_)
    print(random_page)
    if request.method == "POST":
        form_index = SearchEntryForm(request.POST)
        if form_index.is_valid():
            entry_search = form_index.cleaned_data["entry_search"]
            if entry_search:
                search_list = [entry for entry in entries_ if entry_search.lower() in entry.lower()]
            for entry in entries_:
                    if entry_search.lower() == entry.lower():
                        return redirect('pages:wikipage', entry=entry)
            if len(search_list)==0:
                return redirect('pages:error', error=f'No search results for "{entry_search}"')
    #done layout
     
    return render(request, "encyclopedia/error.html", {
        "error" : error,
        "entries": entries_,
        "form": SearchEntryForm(),
        "entry_search": entry_search,
        "search_list" : search_list,
        "random_page" : random_page,
     })
