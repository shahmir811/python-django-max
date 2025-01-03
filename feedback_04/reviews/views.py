from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm

# from .models import Review

# Create your views here.


class ReviewView(View):

  def get(self, request):
    form = ReviewForm()
    return render(request, 'reviews/review.html', {
      "form": form
    })

  def post(self, request):
    form = ReviewForm(request.POST)

    if form.is_valid():
      form.save() # This will save the form data to the database using Modelform
      # review = Review(user_name=form.cleaned_data['user_name'],
      #   review_text=form.cleaned_data['review_text'],
      #   ratings=form.cleaned_data['ratings'])
      # review.save()
      return HttpResponseRedirect('/thank-you')
    
    return render(request, 'reviews/review.html', {
      "form": form
    })


# Below are the function-based view

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

def thank_you(request):
  return render(request, 'reviews/thank_you.html')