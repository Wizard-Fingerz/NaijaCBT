from django.db.models import Model
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.
SUBJECT = [
        ("USE OF ENGLISH", "USE OF ENGLISH"),
        ("MATHEMATICS", "MATHEMATICS"),
        ("PHYSICS", "PHYSICS"),
        ("ENGLISH", "USE OF ENGLISH"),
    ]


class Specialization(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    spec_name = models.CharField(max_length = 255)
    spec_desc = models.TextField()

class Subject(models.Model):
    department = models.ForeignKey(Profile.department, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=20,choices = DEPARTMENT_CHOICES, default= "SCIENCE")


class SubSpecMapper(models.Model):
    specializations = models.ForeignKey(Specialization.spec_name, related_name='', on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject.subject_name, related_name='', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
       for subject in SubSpecMapper.subjects:
            if subject in Subject:
                pass
       super(ModelName, self).save(*args, **kwargs) # Call the real save() method