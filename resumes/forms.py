from django import forms
from .models import CV, Experience, Education, Skill
from django.forms import formset_factory


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'job_description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['university', 'faculty', 'gpa']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'email', 'mobile', 'github', 'linkedin', 'summary']

    def __init__(self, *args, **kwargs):
        super(CVForm, self).__init__(*args, **kwargs)
        self.fields['experiences'] = formset_factory(ExperienceForm)
        self.fields['educations'] = formset_factory(EducationForm)
        self.fields['skills'] = formset_factory(SkillForm)
