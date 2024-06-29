from django import forms
from .models import Task

from django.utils import timezone
from django.contrib.auth.models import User




class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    status = forms.CharField(max_length=255)
    priority = forms.CharField(max_length=255)
    category = forms.CharField(max_length=255)
    assigned_to = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=[(user.id, user.username) for user in User.objects.all()]
    )

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        return timezone.make_aware(timezone.datetime.combine(due_date, timezone.datetime.min.time()))


    def save(self, commit=True):
        task = super(TaskForm, self).save(commit=False)
        assigned_to_ids = self.cleaned_data['assigned_to']
        if commit:
            task.save()
            task.assigned_to.set(User.objects.filter(id__in=assigned_to_ids))
        return task
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date','status', 'priority', 'category', 'assigned_to']