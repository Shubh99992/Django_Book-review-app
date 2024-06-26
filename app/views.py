# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect
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
    # Book = Book
    model = Book
    # Reviews = Review.objects.all()
    template_name = "books/book_detail.html"
    context_object_name = "book"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()  # Add the form to the context
        return context

    def post(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=self.kwargs.get('pk'))
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book  # Assuming your Review model has a foreign key to Book
            review.user = request.user
            review.save()
            return redirect('book_details', pk=book.pk)  # Redirect to the book's detail view
        else:
            # If the form is not valid, re-render the page with the form errors
            return self.render_to_response(self.get_context_data(form=form))