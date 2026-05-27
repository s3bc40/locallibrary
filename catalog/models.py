from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)",
    )

    def __str__(self):
        """String representation"""
        return self.name

    def get_absolute_url(self):
        """URL for genre detail view"""
        return reverse("genre-detail", args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="genre_name_case_insensitive_unique",
                violation_error_message="Genre already exists (case insensitive match)",
            ),
        ]


class Book(models.Model):
    """Model representing a book"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "Author",
        on_delete=models.RESTRICT,
        null=True,
    )
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book",
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        help_text="13 Character <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>",
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        """Book string representation"""
        return self.title

    def get_absolute_url(self):
        """URL for the book detail view"""
        return reverse("book-detail", args=[str(self.id)])
