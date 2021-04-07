# from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
# from django.contrib.auth.decorators import login_required
from .models import Workout
from services.models import Service


# Create your views here.
service = Service.objects.all()

class WorkoutHomeView(ListView):
    template_name = 'workout/workout_home.html'
    paginate_by = 4
    def get_queryset(self):
        return Workout.objects.all().order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkoutHomeView, self).get_context_data(**kwargs)
        context['title'] = 'Workout - GymCounselor'
        context['latest_post'] = Workout.objects.all().order_by('-pk')[:3]
        context['service'] = service
        return context


class WorkoutDetailView(DetailView):
    template_name = 'workout/workout_detail.html'

    def get_object(self, queryset=None):
        work_id = self.kwargs['pk']
        return Workout.objects.get(pk=work_id)

    def get_context_data(self, **kwargs):
        context = {
            'object': self.get_object(),
            'title': self.object.video_title,
            'latest_post': Workout.objects.all().order_by('-pk')[:3],
        }
        return context