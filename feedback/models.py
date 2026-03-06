from django.db import models

class Course(models.Model):
    pass

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    image = models.URLField(max_length=500, blank=True, null=True)

    content = models.TextField()
    rating = models.IntegerField()

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="feedbacks"
    )

    def __str__(self):
        return f"{self.name} - ⭐{self.rating}"

