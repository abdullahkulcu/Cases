from django import forms
from .models import Subscriber
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper


class SubscriberForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=3, empty_value="name")
    surname = forms.CharField(max_length=50, min_length=3, empty_value="surname")
    email = forms.EmailField(label="E-Mail")
    phone = forms.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"
        self.helper.form_action = "/form/save/sub"
        self.helper.form_show_errors = True

        self.helper.layout = Layout(
            "name",
            "surname",
            "email",
            "phone",
            Submit("submit", "Gönder", css_class="btn-success")
        )
