from django.contrib.auth.decorators import login_required
from tool.Json_refactor import DateEncoder
from django.http import HttpResponse
from .models import Paper, LifeGdp
import json


@login_required
def index(request):
    papers = list(Paper.objects.values())
    return HttpResponse(json.dumps(papers, cls=DateEncoder))


@login_required
def get_life_gdp_data(request):
    data = list(LifeGdp.objects.values())
    return HttpResponse(json.dumps(data, cls=DateEncoder))
