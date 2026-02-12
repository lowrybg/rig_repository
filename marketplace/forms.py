from django import forms

from marketplace.models import Listing, PriceReport


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'related_component', 'condition','price', 'description', 'contact_email']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),

        }

class PriceReportForm(forms.ModelForm):
    class Meta:
        model = PriceReport
        fields = ['component', 'store_name', 'price','url']

        