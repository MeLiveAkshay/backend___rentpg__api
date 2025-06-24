from django.db import models

# Create your models here.
class TeamMember(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)
    member_role = models.CharField(max_length=100)
    member_bio = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    member_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.member_name