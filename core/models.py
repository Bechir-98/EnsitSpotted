from django.db import models

class SpottedMessage(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_to_n8n = models.BooleanField(default=False)

    def __str__(self):
        return f"Message #{self.id}"

    class Meta:
        ordering = ['created_at']
