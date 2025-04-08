from django import forms
from .models import Podcast, Contact, Category



default_attrs = {
    'class': 'text-zinc-800 font-medium text-sm placeholder:font-normal placeholder:text-sm w-full bg-gray-100/10 border border-red-900/40 placeholder-red-800/70 px-4 py-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-indigo-100',
    }

default_label_attrs = {
    'class': 'text-white text-sm font-regular mb-1 block',
}

default_error_attrs = {
    'class': 'text-[#04f5dc] font-normal text-sm',
}


class PodcastForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )


    class Meta:
        model = Podcast
        fields= ["title", "description", "file", 'm3u8_url', "thumbnail", "poster_image", "categories"]   
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100/0 px-4 py-2 border border-gray-300/30 text-[#fd4527] rounded-sm placeholder-stone-700 focus:outline-none focus:ring-2 focus:ring-indigo-100',
                'placeholder': 'Enter title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-gray-100/0 px-4 py-2 border border-gray-300/30 text-[#fd4527] rounded-sm placeholder-stone-700 focus:outline-none focus:ring-2 focus:ring-indigo-100',
                'rows': 3,
                'placeholder': 'Enter description'
            }),
            'file': forms.FileInput(attrs={
                'class': 'w-full text-stone-500 font-regular text-sm bg-gray-300/10 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-stone-800 file:hover:bg-stone-700 file:text-white rounded',
            }),
            'm3u8_url': forms.URLInput(attrs={
                'class': 'w-full bg-gray-100/0 px-4 py-2 border border-gray-300/30 text-[#fd4527] placeholder-stone-700 rounded-sm focus:outline-none focus:ring-2 focus:ring-indigo-100',
                'placeholder': 'Enter M3U8 URL'
            }),
            'thumbnail': forms.FileInput(attrs={
                'class': 'w-full text-stone-500 font-regular text-sm bg-gray-300/10 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-stone-800 file:hover:bg-stone-700 file:text-white rounded',
            }),
            'poster_image': forms.FileInput(attrs={
                'class': 'w-full text-stone-500 font-regular text-sm bg-gray-300/10 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-stone-800 file:hover:bg-stone-700 file:text-white rounded',
            }),
        }

        
        




class ContactForm(forms.ModelForm):

    accept_privacy_policy = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'id': 'accept_privacy_policy'}),
        error_messages={'required': 'Hai dimenticato di acettare'}
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            'name': forms.TextInput(attrs={**default_attrs, 'placeholder': 'Nome e cognome', 'id': 'name'}),
            'email': forms.EmailInput(attrs={**default_attrs, 'placeholder': 'La tua email', 'id': 'email'}),
            'phone': forms.TextInput(attrs={**default_attrs, 'placeholder': 'Il tuo numero di telefono', 'id': 'phone'}),
            'subject': forms.TextInput(attrs={**default_attrs, 'placeholder': 'Oggetto', 'id': 'subject'}),
            'message': forms.Textarea(attrs={
                **default_attrs,
                'placeholder': 'Scrivi un messaggio (almeno 20 caratteri)',
                'rows': 5,
                'id': 'message'
            }),
        }
        error_messages = {
            'name': {'required': 'Il nome è obbligatorio'},
            'email': {'required': 'L’email è obbligatoria'},
            'phone': {'required': 'Il numero di telefono è obbligatorio'},
            'subject': {'required': 'L’oggetto è obbligatorio'},
            'message': {'required': 'Il messaggio è obbligatorio'},
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
            if field.label:
                field.label = f"<span class='{default_label_attrs['class']}'>{field.label}</span>"

    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(email=email).exists():
            raise forms.ValidationError("Questa email è già registrata")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message', '')  # Default to an empty string if the field is missing
        if len(message) < 20:
            raise forms.ValidationError(
                f"Il messaggio deve contenere almeno 20 caratteri (Attualmente sono {len(message)})"
            )
        return message
    
   
        