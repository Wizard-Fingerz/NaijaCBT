from django.db import models
from datetime import date
from django.contrib.auth.models import User
# from jamb.models import Specialization
# # Create your models here.


# EXAM_CHOICES = [
#         ("UTME", "UTME"),
#         ("WAEC", "WAEC"),
#         ("NECO", "NECO"),
#         ("PUTME", "PUTME"),
#     ]
# SUBJECT_CHOICES_UTME = [
#         ("USE OF ENGLISH", "USE OF ENGLISH"),
#         ("MATHEMATICS", "MATHEMATICS"),
#         ("PHYSICS", "PHYSICS"),
#         ("ENGLISH", "USE OF ENGLISH"),
#     ]

# SUBJECT_CHOICES_WAEC = [
#         ("ENGLISH LANGUAGE", "ENGLISH LANGUAGE"),
#         ("GENERAL MATHEMATICS", "GENERAL MATHEMATICS"),
#         ("FURTHER MATHEMATICS", "FURTHER MATHEMATICS"),
#         ("LITERATURE IN ENGLISH", "LITERATURE IN ENGLISH"),
#         ("PHYSICS", "PHYSICS"),
#         ("HAUSA", "HAUSA"),
#         ("IGBO", "IGBO"),
#         ("YORUBA", "YORUBA"),
#         ("BIOLOGY", "BIOLOGY"),
#         ("CHEMISTRY", "CHEMISTRY"),
#         ("PHYSICS", "PHYSICS"),
#         ("AGRICULTURAL SCIENCE", "AGRICULTURAL SCIENCE"),
#         ("GOVERNMENT", "GOVERNMENT"),
#         ("ECONOMICS", "ECONOMICS"),
#         ("GEOGRAPHY", "GEOGRAPHY"),
#         ("CIVIC EDUCATION", "CIVIC EDUCATION"),
#         ("CHRISTIAN RELIGIOUS STUDIES", "CHRISTIAN RELIGIOUS STUDIES"),
#         ("ISLAMIC STUDIES", "ISLAMIC STUDIES"),
                
#     ]
# SUBJECT_CHOICES_NECO = [
#         ("USE OF ENGLISH", "USE OF ENGLISH"),
#         ("MATHEMATICS", "MATHEMATICS"),
#         ("PHYSICS", "PHYSICS"),
#         ("ENGLISH", "USE OF ENGLISH"),
#     ]

# def ExamSubject(examType):
#     if examType == "UTME":
#         return SUBJECT_CHOICES_UTME
#     elif examType == "WAEC":
#         return SUBJECT_CHOICES_WAEC
#     elif examType == "NECO":
#         return SUBJECT_CHOICE_NECO


# current_year = date.today().year

# YEAR_CHOICES = tuple((str(i), str(i)) for i in range(1978,current_year))


# # class StartExam(models.Model):
# #     examType =models.CharField(max_length=20, choices = EXAM_CHOICES, default= 'UTME')
# #     year = models.CharField(max_length=20, choices = YEAR_CHOICES, default= str(current_year))
# #     subject = models.CharField(max_length=20, choices = SUBJECT_CHOICES_UTME, default = "USE OF ENGLISH")

# class Subject(models.Model):
#     subject_name = models.CharField(max_length = 200)
#     subject_desc = models.TextField()



# class Student(models.Model):
#     student = models.OneToOneField(User, on_delete=models.CASCADE)
#     spec = models.OneToOneField(Specialization, on_delete=models.CASCADE)