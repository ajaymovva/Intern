from django import forms

choices = (
    (1, "2019-02-05_10:33:18"), (2, "2019-02-05_10:34:04")
)


class UploadFileForm(forms.Form):
    file = forms.FileField()


# class SelectdateForm(forms.Form):
#     date = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'onchange': 'actionform.submit();'}))
