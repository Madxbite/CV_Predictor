from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

def index(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

        return HttpResponse(task)
    else:
        return render(request, "CV_Predictor/index.html", {
            "form": NewTaskForm()
        })



class NewTaskForm(forms.Form):
    task = forms.FileField(label="PDF File:")