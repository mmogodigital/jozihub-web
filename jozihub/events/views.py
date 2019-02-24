from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'events/events.html', context)

def venue_hire(request):
    context = {}
    return render(request, 'events/venue_hire.html', context)
# '''
# Created on 25 Nov 2013

# @author: michael
# '''
# from django.views import generic as generic_views

# from tunobase.core import utils as core_utils
# from tunobase.corporate.media import models
# from django.contrib import messages


# class Events(generic_views.ListView):
#     paginate_by = 12

#     def get_queryset(self):
#         return models.Event.objects.permitted()\
#             .for_current_site().past_events().order_by('-start')

#     def get_context_data(self, *args, **kwargs):
#         context = super(Events, self).get_context_data(**kwargs)

#         events = models.Event.objects.permitted().for_current_site()

#         context.update({
#             'current_and_future_events':
#                 events.current_and_future_events().order_by('start')
#         })

#         return context


# class EventDetail(generic_views.DetailView):

#     def get_object(self):
#         return core_utils.get_permitted_object_or_404(
#             models.Event,
#             slug=self.kwargs['slug']
#         )


# class VenueHire(generic_views.edit.FormView):
#     def form_valid(self, form):
#         form.send_email()
#         messages.success(self.request, 'Venue request sent')
#         return self.render_to_response(self.get_context_data(form=form))
