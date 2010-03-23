from django.db import models

class ChunkManager(models.Manager):

    def get_content_by_key(self, key, default_value=None):
        
        try:
            return self.get(key=key).content
        except self.model.DoesNotExist:
            return default_value


class Chunk(models.Model):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(help_text="A unique name for this chunk of content", blank=False, max_length=255, unique=True)
    content = models.TextField(blank=True)

    objects = ChunkManager()
    
    def __unicode__(self):
        return u"%s" % (self.key,)
