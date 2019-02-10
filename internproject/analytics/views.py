from .forms import *
from django.shortcuts import render
from django.shortcuts import *

options = (
    "2019-02-05_10:33:18", "2019-02-05_10:34:04"
)


def preprocess_file():
    with open("log.txt", "rb") as f:
        present = None
        data = {}
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            string = str(line.strip())[2:-1]
            if string.find("query time is") != -1:
                first = ":".join(string.split(":")[1:])
                f.readline()
                second = str(f.readline().strip())[2:-1].split(":")[1]
                f.readline()
                third = str(f.readline().strip())[2:-1].split(":")[1]
                present = (first.strip(), second.strip(), third.strip())
                data[present] = []
            elif string.find("articles_title") != -1:
                temp = []
                temp.append("".join(str(string.strip()).split(":")[1:]).strip())
                temp.append("".join(str(f.readline().strip())[2:-1].split(":")[1:]).strip())
                temp.append("".join(str(f.readline().strip())[2:-1].split(":")[1:]).strip())
                temp.append("".join(str(f.readline().strip())[2:-1].split(":")[1:]).strip())
                data[present].append(temp)
    return data


def base_page(request):
    form = UploadFileForm()
    return render(request, "upload.html", {'form': form})


def handle_uploaded_file(f):
    with open('log.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def select_fields(request):
    data = preprocess_file()
    datetime = options[0]
    obj = None
    for i in data:
        if i[0] == datetime:
            obj = data[i]
        return render(request, 'select_form.html', {'object': obj, 'options': options, 'select_option': datetime})


def process_selectfield(request):
    data = preprocess_file()
    datetime = request.POST['date']
    obj = None
    for i in data:
        if i[0] == datetime:
            obj = data[i]
    return render(request, 'select_form.html', {'object': obj, 'options': options, 'select_option': datetime })


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect("analytics:select_field")
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
