from django.http import HttpResponseRedirect
# from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import ReviewForm
from .models import Review


# Create your views here.
class ReviewView(CreateView):
  model = Review # This will automatically fetch all the reviews from the database and pass it to the template
  fields = '__all__'
  # form_class = ReviewForm # ReviewForm must be a model form
  template_name = 'reviews/review.html'
  success_url = '/thank-you'


class ThankYouView(TemplateView):
  template_name = 'reviews/thank_you.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['message'] = 'This works!'
    return context
  

class ReviewsListView(ListView):
  template_name = 'reviews/review_list.html'
  model = Review # This will automatically fetch all the reviews from the database and pass it to the template
  context_object_name = 'reviews' # This will pass the reviews list to the template with the name 'reviews'

  def get_queryset(self):
    base_query = super().get_queryset()
    data = base_query.filter(ratings__gt=3)
    return data
  

class SingleReviewView(DetailView):
  template_name = 'reviews/single_review.html'
  model = Review # This will automatically fetch all the reviews from the database and pass it to the template
  # context_object_name = 'review' # Django by default use the model name in lowercase as the context_object_name

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    loaded_review = self.object
    favorite_id = self.request.session.get('favorite_review')
    context['is_favorite'] = favorite_id == str(loaded_review.id)
    return context


class AddFavoriteView(View):
  def post(self, request):
    review_id = request.POST['review_id']
    request.session['favorite_review'] = review_id
    return HttpResponseRedirect('/reviews/' + review_id)


# ####################################
# ####################################
# Below we are using Form view to get/post reviews form
# ####################################
# ####################################

# class ReviewView(FormView):
#   form_class = ReviewForm
#   template_name = 'reviews/review.html'
#   success_url = '/thank-you'

#   # The following method is called when the form is valid and 
#   # then it saves the form data to the database
#   def form_valid(self, form):
#     form.save()
#     return super().form_valid(form)

# ####################################
# ####################################
# Below we are using simple View class to render the templates
# ####################################
# ####################################

# class ReviewView(View):

#   def get(self, request):
#     form = ReviewForm()
#     return render(request, 'reviews/review.html', {
#       "form": form
#     })

#   def post(self, request):
#     form = ReviewForm(request.POST)

#     if form.is_valid():
#       form.save() # This will save the form data to the database using Modelform
#       # review = Review(user_name=form.cleaned_data['user_name'],
#       #   review_text=form.cleaned_data['review_text'],
#       #   ratings=form.cleaned_data['ratings'])
#       # review.save()
#       return HttpResponseRedirect('/thank-you')
    
#     return render(request, 'reviews/review.html', {
#       "form": form
#     })

  
# ####################################
# ####################################
# Below we are using TemplateView to render the templates
# ####################################
# ####################################

# class ReviewsListView(TemplateView):
#   template_name = 'reviews/review_list.html'

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     reviews = Review.objects.all()
#     context['reviews'] = reviews
#     return context

# class SingleReviewView(TemplateView):
#   template_name = 'reviews/single_review.html'

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     review_id = kwargs['id']
#     review = Review.objects.get(pk=review_id)
#     context['review'] = review
#     return context

# ####################################
# ####################################
# Below are the function-based view
# ####################################
# ####################################


# def reviews(request):
#   if request.method == 'POST':
#     form = ReviewForm(request.POST)

#     if form.is_valid():
#       form.save() # This will save the form data to the database using Modelform
#       # review = Review(user_name=form.cleaned_data['user_name'],
#       #   review_text=form.cleaned_data['review_text'],
#       #   ratings=form.cleaned_data['ratings'])
#       # review.save()
#       return HttpResponseRedirect('/thank-you')
    
#   else: 
#     form = ReviewForm()

#   return render(request, 'reviews/review.html', {
#     "form": form
#   })

# def thank_you(request):
#   return render(request, 'reviews/thank_you.html')

