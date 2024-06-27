# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .models import Book, Review
from .forms import ReviewForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class HomeView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"
    # def get_queryset(self):
    #     return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object  # Get the Book object from the view
        context['form'] = ReviewForm()  # Add the ReviewForm to the context
        context['reviews'] = Review.objects.filter(book=book)  # Fetch reviews related to the book
        return context

    def post(self, request, *args, **kwargs):
        book = self.get_object()  # Get the Book object for this view
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['review_text']
            rating = form.cleaned_data['rating']
            # Assuming you have a Review model with fields: book, user, review_text, rating
            review = Review.objects.create(
                book=book,
                user=request.user,  # Assuming you have user authentication
                review_text=review_text,
                rating=rating
            )
            return redirect('book_details', pk=book.pk)  # Redirect to the book's detail page after submission
        else:
            # If the form is not valid, re-render the page with the form and any errors
            return self.render_to_response(self.get_context_data(form=form))