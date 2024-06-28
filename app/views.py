# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, FormView
from .models import Book, Review, User
from .forms import CustomUserCreationForm, FavoriteBooksForm, RecentReadsForm, ReviewForm
from django.db.models import Avg, Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as mainUser


class ExploreBooksView(ListView):
    model = Book
    template_name = 'books/explore_books.html'
    context_object_name = 'books'


class SignUpView(CreateView):
    model = mainUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def form_valid(self, form):
        # Additional logic if needed
        return super().form_valid(form)
    
class HomeView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"

    def get_queryset(self):
        # Fetch the top 5 books with the most reviews
        top_books = Book.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:5]
        return top_books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['most_reviewed_books'] = self.get_queryset()
        if self.request.user.is_authenticated:
            custom_user, created = User.objects.get_or_create(user=self.request.user)
            context['favorite_books_form'] = FavoriteBooksForm(instance=custom_user)
            context['recent_reads_form'] = RecentReadsForm(instance=custom_user)
            context['favorite_books'] = custom_user.favorite_books.all()
            context['recent_reads'] = custom_user.recent_reads.all()
        return context

    


    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            custom_user = get_object_or_404(User, user=request.user)
            favorite_books_form = FavoriteBooksForm(request.POST, instance=custom_user)
            recent_reads_form = RecentReadsForm(request.POST, instance=custom_user)

            if 'favorite_books_form' in request.POST and favorite_books_form.is_valid():
                favorite_books_form.save()

            if 'recent_reads_form' in request.POST and recent_reads_form.is_valid():
                recent_reads_form.save()

        return redirect('home')

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object  # Get the Book object from the view

        average_rating = Review.objects.filter(book=book).aggregate(Avg('rating'))['rating__avg']
        context['average_rating'] = round(average_rating, 2) if average_rating else None

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