from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator, URLValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Information
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, validators=[EmailValidator()])
    mobile = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    github = models.URLField(max_length=255, validators=[URLValidator()])
    linkedin = models.URLField(max_length=255, validators=[URLValidator()])

    # Summary
    summary = models.TextField()

class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField(max_length=500)

class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='educations')
    university = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    gpa = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(4.0)
        ]
    )

class Skill(models.Model):
    LEVEL_CHOICES = [(i, i) for i in range(1, 6)]  # Create choices from 1 to 5

    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    level = models.IntegerField(choices=LEVEL_CHOICES)  # Now level is a choice field
