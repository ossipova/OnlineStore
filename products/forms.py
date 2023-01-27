from django import forms


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()
    currency = forms.CharField(max_length=3)
    rate = forms.FloatField(min_value=1, max_value=5)
    commentable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': True}), required=False)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=2)
