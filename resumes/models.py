from django.db import models

def resume_upload_path(instance, filename):
    return f"resumes/{filename}"

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    file = models.FileField(upload_to=resume_upload_path)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position}"
