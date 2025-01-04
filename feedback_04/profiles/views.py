from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ProfileForm
from .models import UserProfile


# Create your views here.
class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProfileListView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")

    
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })
