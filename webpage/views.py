from django.shortcuts import render
from . import discovery_client
# Create your views here.


def index(request):
    template_model = {}
    registered_apps = []
    for app in discovery_client.applications.applications:
        registered_apps.append(app.name)

    template_model["apps"] = registered_apps
    return render(request=request, template_name="index.html", context=template_model)
