from django import forms
from .models import SeatInfo

FLOOR_CHOICES = (
	("3", "Floor 3"),
	("4", "Floor 4"),
	("5", "Floor 5"),
	("7", "Floor 7"),
	("8", "Floor 8"),
	("9", "Floor 9"),
	("10", "Floor 10"),
	)

AREA_CHOICES = (
	("A", "Area A"),
	("B", "Area B"),
	("C", "Area C"),
	("D", "Area D"),
	("E", "Area E"),
	)

SEAT_CHOICES = (
	("0", "0"),
	("1", "1"),
	("2", "2"),
	("3", "3"),
	("4", "4"),
	("6", "6"),
	)

class searchForm(forms.Form):
	
	floor = forms.ChoiceField(label=u'floor_selection', choices=FLOOR_CHOICES)
	area = forms.ChoiceField(label=u"area_selection", choices=AREA_CHOICES)

	def __int__(self, *args, **kwargs):
		super(searchForm, self).__init__(*args, **kwargs)
		self.fields['floor'].choices = FLOOR_CHOICES
		self.fields['area'].choices = AREA_CHOICES
		


class updateForm(forms.ModelForm):
	floor = forms.ChoiceField(label=u'floor_selection', choices=FLOOR_CHOICES)
	area = forms.ChoiceField(label=u"area_selection", choices=AREA_CHOICES)
	seats = forms.ChoiceField(label=u"area_selection", choices=SEAT_CHOICES)

	def __int__(self, *args, **kwargs):
		super(updateForm, self).__init__(*args, **kwargs)
		self.fields['floor'].choices = FLOOR_CHOICES
		self.fields['area'].choices = AREA_CHOICES
		self.fields['seats'].choices = SEAT_CHOICES
	# floor = forms.CharField(max_length=2, choices=[])
	# area = forms.CharField(max_length=1, choices=[])
	# seats = forms.CharField(max_length=1, choices=[])
	# def __init__(self, *args, **kwargs):
	# 	super(updateForm, self).__init__(*args, **kwargs)
	# 	self.fields['floor'].choices = forms.ModelChoiceField(queryset=SeatInfo.objects.values_list("floor", flat=True).distinct(), empty_label=None)
	# 	self.fields['area'].choices = forms.ModelChoiceField(queryset=SeatInfo.objects.values_list("area", flat=True).distinct(), empty_label=None)
	# 	self.fields['seats'].choices = forms.ModelChoiceField(queryset=SeatInfo.objects.values_list("seats", flat=True).distinct().order_by('seats'), empty_label=None)

	class Meta:
		model = SeatInfo
		fields = ['table']
		widgets = {'table': forms.TextInput(attrs={"id":"vacant_table", "class":"form-control", "type":"text", "placeholder":"table number"}),}
	# def __int__(self, *args, **kwargs):
	# 	super(updateForm, self).__int__(*args, **kwargs)
	# 	self.fields['floor'].choices = FLOOR_CHOICES
	# 	self.fields['area'].choices = AREA_CHOICES
	# 	self.fields['seats'].choices = SEAT_CHOICES