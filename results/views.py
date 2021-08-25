from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import announced_pu_results, polling_unit
from .forms import PollingUnitForm, get_ip_address


class IndexView(generic.View):
    """Show result from each pulling unit"""
    def get(self, request, *args, **kwargs):
        pu_results = announced_pu_results.objects.all()
        return render(request, 'results/index.html', {'pu_results': pu_results})

class PollingUnit(generic.View):
    """show results(sum total) of all the polling unit under each local government"""
    def get(self, request, *args, **kwargs):
        pu_units = polling_unit.objects.all()
        return render(request, 'results/polling_unit.html', {'pu_units': pu_units})

class PostPoll(generic.View):

    def get(self, request, *args, **kwargs):
        form = PollingUnitForm()
        ip_address = get_ip_address()
        return render(request, 'results/post.html', {'ip_address': ip_address})

    
    def post(self, request, *args, **kwargs):
        ip_address = request.POST.get("ip_address")
        datetime = request.POST.get("datetime")
        party_abbreviation = request.POST.get("party_abbreviation")
        party_score = request.POST.get("party_score")
        entered_by = request.POST.get("entered_by")
        polling_unit_uniqueid = request.POST.get("polling_unit_uniqueid")
        announced_pu_results.objects.get_or_create(
            user_ip_address=ip_address,
            date_entered=datetime,
            party_abbreviation=party_abbreviation,
            party_score=party_score,
            entered_by_user=entered_by,
            polling_unit_uniqueid=polling_unit_uniqueid
            )
        return render(request, 'results/post.html', {'ip_address': ip_address})