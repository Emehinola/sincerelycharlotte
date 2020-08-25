from django.db import models
from user.models import User

# Create your models here.

# Blog model
class Blog(models.Model):
    categories = [
        ("Politics", "Politics"),
        ("Education", "Education"),
        ("Entertainment", "Entertaiment"),
        ("Foods", "Foods"),
        ("LoveAndRelationship", "Love And Relationship"),
        ("Gossip", "Gossip"),
        ("Counselling", "Counselling"),
        ("Technology", "Technology"),
        ("Book", "Book"),
        ("Religion", "Religion"),
        ("Sports", "Sports"),
        ("Technology", "Technology"),
        ("Fashion", "Fashion"),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()
    image = models.ImageField(upload_to='post upload images')
    category = models.CharField(choices=categories, max_length=30)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog Posts'
        ordering = ['-time']

    def __str__(self):
        return self.title

# comment model
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    userEmail = models.EmailField(blank=True, null=True, default="Unknown User")
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-time']

    def __str__(self):
        if self.author:
            return f"{self.author} | {self.post.title}"
        else:
            return f"{self.userEmail} | {self.post.title}"
    
# post like model
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f"{self.author} | {self.post.title}"
    
# favorite model
class Favorite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return f"{self.author} | {self.title}"


class DailyThought(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.TextField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = "Daily Thoughts"

    def __str__(self):
        return f'{self.author} | {self.time}'
    