from django.shortcuts import render
from jozihub.startups.models import StartUp

def index(request):
    context = { 'startups': list(StartUp.objects.all()) }
    return render(request, 'startups/startups.html', context)

def details(request):
    context = {}
    return render(request, 'startups/startups_details.html', context)
#
# class Startup(generic_views.ListView):
#
#     def get_queryset(self):
#         return models.StartupCompanies.objects.permitted()
#
# class StartupDetail(generic_views.DetailView):
#
#     def get_object(self):
#         return core_utils.get_permitted_object_or_404(
#             models.StartupCompanies,
#             slug=self.kwargs['slug']
#         )
