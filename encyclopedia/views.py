from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from markdown2 import Markdown
from django import forms
from . import util
import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import random
import csv 


"""
Renders wiki's index with lastest articles added displayed
"""
def index(request):
    # open Newest Entries database and read lastest 10 to the template
    with open('Newest_Entries.csv', mode="r") as titles:
        titles_clean = titles.read()
        titles_list = titles_clean.split()
        titles_list.reverse()
        LastestTen = []
        for names in titles_list[:10]:
            LastestTen.append(names)
        # if Newest Entries database is too big, clean it
        if len(titles_list) > 100:
            CleanCVS(LastestTen) 
    return render(request, "encyclopedia/index.html", {"entries": LastestTen, "form":SearchForm()})


"""
Renders via url requested entries
"""
def entries(request, title):
    entry = util.get_entry(title.capitalize())
    if entry:
        # convert markdown to html and render the entry route
        translator = Markdown()
        html = translator.convert(entry)
        return render(request, "encyclopedia/entry.html", {"entry":html, "title":title.upper(), "form":SearchForm()})
    else:
        # render 404 not found page
        return render(request, "encyclopedia/not_found.html", {"form":SearchForm()})


"""
implements the search function
"""
def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        # check if valid, and search requested query
        if form.is_valid():
            query = form.cleaned_data["search"].capitalize()
            EntriesList = util.list_entries()
            # if query match an entry completly, redirect to it
            if query in EntriesList:
                return redirect("entries", query)
            # if query partialy matchs, render a list of possible entries. Else, render 404 template
            else:
                MayBeLookingFor = []
                for entries in range(len(EntriesList)):
                    if query in EntriesList[entries]:
                        MayBeLookingFor.append(EntriesList[entries])
                if not MayBeLookingFor:
                    return render(request, "encyclopedia/search_not_found.html", {"form":SearchForm()})
                else:
                    return render(request, "encyclopedia/maybe_looking_for.html", {"form":SearchForm(), "titles":MayBeLookingFor})
        # if not valid, render search template again
        else:
            return redirect ("search", {"form":SearchForm()})        
    # via GET, render search template 
    else:
        return render(request, "encyclopedia/search.html", {"form":SearchForm()})


"""
returns a random entry
"""
# take a random entry and render it
def random_entry(request):
    EntriesList = util.list_entries()
    random_entry = random.choice(EntriesList)
    return entries(request, random_entry)


"""
creates a new entry using markdown language
"""
def new_entry(request):
    if request.method == "POST":
        # gather data from form and if valid, write it into a new .md archive in entries folder
        form = TextareaForm(request.POST)
        if form.is_valid():
            EntriesList = util.list_entries()
            title = form.cleaned_data["title"].capitalize()
            content = form.cleaned_data["new_entry"]
            # ensure entry doesn't already exist
            if title in EntriesList:
                return render(request, "encyclopedia/oops.html", {"form":SearchForm()})
            else:
                util.save_entry(title, content)
                # update Newest Entries database to show in index
                LastEntriesUpdate(title)
                return entries(request, title)
        # if invalid or GET request, redirect to new entry again
        else:
            return redirect("new", {"form":SearchForm()})
    else:
        return render(request, "encyclopedia/new_entry.html", {"form2":TextareaForm(), "form":SearchForm()})

"""
opens edit template with entry's markdown code loaded
"""
def get_edit(request):
    if request.method == "POST":
        # find requested entry
        title = request.POST.get("hidden_title").capitalize()
        with open(f"entries/{title}.md") as entry:
            entry_content = entry.read()
        return render(request, "encyclopedia/edit.html", {"form3":EditForm(initial={"new_title":title, "edited_entry":entry_content}), "form":SearchForm(), "title":title})
    # render 404 page if GET requested
    else:
        return render(request, "encyclopedia/not_found.html")

"""
edit markdown code of entry and save it 
"""
def edit(request):
    #load updated data
    form = EditForm(request.POST)
    if form.is_valid():
        #if valid, update entry with new data and redirect to it
        title = form.cleaned_data["new_title"].capitalize()
        content = form.cleaned_data["edited_entry"]
        util.save_entry(title, content)
        return redirect("entries", title) 
    else:
        return redirect ("encyclopedia/edit.html", {"form3":EditForm(initial={"new_title":title}), "form":SearchForm(), "title":title})

"""
Renders wiki's complete list of articles
"""
def articles(request):
    # Organize every article in wiki in 4 columns sorted by alphabetical order, then render it 
    articles_list = util.list_entries()
    AtoG = ["A", "B", "C", "D", "E", "F", "G"]
    HtoN = ["H", "I", "J", "K", "L", "M", "N"]
    OtoT = ["O", "P", "Q", "R", "S", "T"]
    Column1, Column2, Column3, Column4 = ([] for i in range(4))
    for article in articles_list:
        if article[0] in AtoG:
            Column1.append(article)
        elif article[0] in HtoN:
            Column2.append(article)
        elif article[0] in OtoT:
            Column3.append(article)
        else:
            Column4.append(article)
    return render(request, "encyclopedia/articles.html", {"Column1": Column1, "Column2":Column2, "Column3":Column3, "Column4":Column4, "form":SearchForm()})

#auxialiary functions

"""
Opens csv file with lastest articles submitted and write new article's title to bottom of it
"""
def LastEntriesUpdate(title):
    with open('Newest_Entries.csv', mode="a") as NewestEntries:
        csvtitle = []
        csvtitle.append(title)
        writer = csv.writer(NewestEntries, delimiter=",")
        writer.writerow(csvtitle)

"""
Cleans Newest Entries database when too big, leaving just the lastest ten
"""
def CleanCVS(new_list):
    with open('Newest_Entries.csv', mode="w") as NewestEntries:
        for titles in range(len(new_list)):
            NewestEntries.write(f"{new_list[titles]}\n")


"""
Global Forms used in the wiki
"""
# create search form class
class SearchForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search an article'}))

# create textarea form class for new entries
class TextareaForm(forms.Form):
    title = forms.CharField(label="title", widget=forms.TextInput(attrs={'placeholder': ' New article title'}))
    new_entry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ' Write a new article using Markdown language'}))

# create textarea form class for editing entries with markdown code prepolutaded, then render template
class EditForm(forms.Form):
    new_title = forms.CharField(label="title")
    edited_entry = forms.CharField(widget=forms.Textarea)






