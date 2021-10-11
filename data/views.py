import datetime
from data.models import data
from data.forms import DataForm
from django.shortcuts import render, redirect


def index(request):
    context = {"datas": data.objects.all()}

    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        context = {"form": DataForm()}
        return render(request, "create.html", context)


def update(request, id):
    instance = data.objects.get(id=id)

    if request.method == "POST":
        form = DataForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            instance.modTime = datetime.datetime.now()
            instance.save()
        return redirect("index")
    else:
        context = {"form": DataForm(instance=instance)}
        return render(request, "update.html", context)


def delete(request, id):
    instance = data.objects.get(id=id)
    instance.delete()

    return redirect("index")
