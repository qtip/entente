from .models import Server, Channel

""" def servers_var(request):
    servers = Server.objects.all()
    context = {
        "servers": servers,
    }
    return {"servers_var": servers} """

def channels_var(request):
    channels = Channel.objects.all()
    context = {
        "channels": channels,
    }
    return {"channels_var": channels}

current = 0

def view_current(request):
    return {"view_current": current}

