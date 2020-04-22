from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Server, Channel
from .forms import ServerForm, EmptyForm
from django.contrib.auth.models import User

# -----------------SERVERS-----------------

# A view that returns all servers
def index_server(request):
    servers = Server.objects.filter(owner=request.user)
    if request.method == 'POST':
        form = EmptyForm(request.POST)
        print(servers, flush=True)
        return redirect('index')
    else:
        form = EmptyForm()
    context = {
        "servers": servers,
        'form': form,
    }
    return render(request, "servers.html", context)

# A view that presents a form to add another server
@login_required(login_url='/login/')
def add_server(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("Add server message", flush=True)
        # create a form instance and populate it with data from the request:
        form = ServerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #n = form.cleaned_data["display_name"]
            #request.user.server_set.create(display_name=n)
            #add owner a different way
            newServer = Server(
                display_name=form.cleaned_data["display_name"],
                owner=request.user
            )
            newServer.save()
            # redirect to a new URL:
            return redirect('../')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ServerForm()
    return render(request, 'add_server.html', {'form': form})

# -----------------CHANNELS-----------------

# A view that returns all channels of a certain server
def index_channel(request, pk):
    # Conditions for object to retrieve
    channels = Channel.objects.filter(server_id=pk)
    context = {
        "channels": channels,
    }
    return render(request, "channels.html", context)