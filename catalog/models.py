from django.db import models
import hashlib

class UploadedFile(models.Model):
    filename = models.CharField(max_length=255)
    file_hash = models.CharField(max_length=64, unique=True)
    analyzed = models.BooleanField(default=False)
    output_path = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.file_hash:
            self.file_hash = self.calculate_hash()
        super().save(*args, **kwargs)

    def calculate_hash(self):
        return hashlib.sha256(self.filename.encode()).hexdigest()
    
    def __str__(self):
        return self.filename

    class Meta:
        indexes = [models.Index(fields=['file_hash'])]