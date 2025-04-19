from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage

from .forms import UserBioForm, UploadFileForm


def proccess_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
        'a': a,
        'b': b,
        'result': result
    }
    return render(request, 'requestdataapp/request-query-params.html', context)


def user_form(request: HttpRequest) -> HttpResponse:
    form = UserBioForm
    context = {
        'form':  form
    }
    return render(request, 'requestdataapp/user-bio-form.html', context)

def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, files=request.FILES)
        if form.is_valid():
            # myfile = request.FILES['myfile']
            myfile = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            print('save file', filename)
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request, 'requestdataapp/file-upload.html', context)