from django.db import models

class Post(models.Model):
    # Field for the title of the post
    title = models.CharField(max_length=140)

    # Field for the main content of the post
    body = models.TextField()

    # Field for an optional signature with a default value
    signature = models.CharField(
        max_length=140,
        default="You can't bring back what you've lost, think about what you have now!"
    )

    # Field for the date and time of the post
    date = models.DateTimeField()

    # Human-readable representation of the post, shown as its title
    def __str__(self):
        return self.title
