from django.shortcuts import render

from basicformsapp.forms import NewUserForm

def index(request):
    return render(request,'basicformsapp/index.html')

def users(request):
    form = NewUserForm()
    # form_dic = {'form': form}

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ("Invalid Form!!")

    return render(request,'basicformsapp/signup.html',{'form':form})

# Create your views here.
