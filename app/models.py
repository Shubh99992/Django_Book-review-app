from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=40, default='Not Available Data')
    genre = models.CharField(max_length=100, default="Philoshopy")
    details = models.TextField(max_length=1000, default='No details available')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite_books = models.ManyToManyField(Book, related_name='favorited_by')
    recent_reads = models.ManyToManyField(Book, related_name='readed_recent_by')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.user.username

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)
            
    def is_following(self, user):
        query = self.followers.all()
        return query.filter(user__username=user).exists()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    
