from django.db import models

class SpottedMessage(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message #{self.id}"

    class Meta:
        verbose_name = "Spotted Message"
        verbose_name_plural = "Spotted Messages"
        ordering = ['-created_at']
