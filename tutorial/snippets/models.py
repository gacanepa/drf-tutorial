from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXER_FIELDS = {"NAME": 0, "ALIASES": 1, "FILETYPES": 2, "MIMETYPES": 3}
LEXERS = [lexer for lexer in get_all_lexers() if lexer[LEXER_FIELDS["ALIASES"]]]

# List of tuples. Each element consists of the first alias and the language name.
LANGUAGE_CHOICES = sorted(
    [
        (lexer[LEXER_FIELDS["ALIASES"]][0], lexer[LEXER_FIELDS["NAME"]])
        for lexer in LEXERS
    ]
)

STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)

    def __repr__(self):
        return self.title

    class Meta:
        ordering = ["created"]
