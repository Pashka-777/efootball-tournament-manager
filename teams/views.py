from django.shortcuts import render, redirect
from .models import Team
from .forms import TeamForm


def team_list(request):
    teams = Team.objects.all()

    return render(request, 'teams/team_list.html', {
        'teams': teams
    })


def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('team_list')

    else:
        form = TeamForm()

    return render(request, 'teams/team_form.html', {
        'form': form
    })