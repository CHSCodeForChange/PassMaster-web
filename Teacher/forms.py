from datetime import datetime

from django import forms
from django.contrib.auth import models

from Passes.models import Pass
from Student.models import Student
from Teacher.models import Teacher


class CreatePass(forms.Form):
	pass_type = forms.CharField(max_length=1, widget=forms.HiddenInput(), initial="1")

	destinationTeacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), empty_label=None,
												label="Destination teacher", required=False,)

	location = forms.CharField(max_length=12, required=False, widget=forms.TextInput(
								attrs={'type': 'text',
										'class': 'form-control',
										'placeholder': 'Location',
								        'style': 'display: none;'}))

	students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), label="Student(s)", required=True)

	start = forms.DateTimeField(label='Start time', required=True, input_formats=['%Y-%m-%dT%H:%M'],
								initial=datetime.now, widget=forms.DateTimeInput(
								attrs={'type': 'datetime-local',
										'class': 'form-control'}))
	end = forms.DateTimeField(label='End time', required=True, input_formats=['%Y-%m-%dT%H:%M'],
								widget=forms.DateTimeInput(
								attrs={'type': 'datetime-local',
										'class': 'form-control'}))

	reason = forms.CharField(label='', required=True, max_length=240, widget=forms.TextInput(
		attrs={'type': 'text',
				'class': 'form-control',
				'placeholder': 'Reason for pass'}))

	user = models.User()

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super(CreatePass, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		originTeacher = Teacher.objects.get(profile=self.user.profile)
		if self.cleaned_data['pass_type'] == '1':
			for student in self.cleaned_data['students']:
				newPass = Pass(type='1', approved=True, startTimeRequested=self.cleaned_data['start'],
								endTimeRequested=self.cleaned_data['end'], description=self.cleaned_data['reason'],
								student=student, destinationTeacher=self.cleaned_data['destinationTeacher'],
								originTeacher=originTeacher)
				newPass.save()
		else:
			for student in self.cleaned_data['students']:
				newPass = Pass(type='2', approved=True, startTimeRequested=self.cleaned_data['start'],
				               endTimeRequested=self.cleaned_data['end'], description=self.cleaned_data['reason'],
				               student=student, location=self.cleaned_data['location'],
				               originTeacher=originTeacher)
				newPass.save()