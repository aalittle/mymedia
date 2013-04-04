from django.db import models

'''this represents a particular medium of media: movie, book, etc.'''
class Medium(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    rating = models.PositiveSmallIntegerField(default=0)
    is_complete = models.BooleanField(default=False)
    
    MOVIE = 'MV'
    BOOK = 'BK'
    TV = 'TV'
    MUSIC = 'MU'
    MEDIUM_CHOICES = (
        (MOVIE, 'Movie'),
        (BOOK, 'Book'),
        (TV, 'TV'),
        (MUSIC, 'Music'),
    )
    medium_type = models.CharField(max_length=2,
                                    choices=MEDIUM_CHOICES,
                                    default=MOVIE)
    owner = models.ForeignKey('auth.User', related_name='media')
    
    class Meta:
            ordering = ('created',)
