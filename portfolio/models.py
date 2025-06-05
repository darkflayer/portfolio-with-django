from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
      # e.g., "Programming Language", "Framework"

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    deployed_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
