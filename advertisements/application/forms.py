""" Forms for wiews POSt add application """

from django import forms
from .models import WindowsApplication, AndroidApplication


class AdvertisementFormWindows(forms.ModelForm):
    """ Form for creating new WindowsApplication """

    class Meta:
        """ Meta information for WindowsApplication """
        model = WindowsApplication
        fields = [
            'name', 'title',
            'short_description', 'full_description',
            'image_application_main', 'image_application_2', 'image_application_3',
            'image_application_4', 'image_application_5',
            'name_file_main', 'file_main',
            'name_file_additional', 'file_additional',
            'verified',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Название программы',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Заголовок для программы',
                }
            ),
            'short_description': forms.Textarea(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Краткое описание программы'
                }
            ),
            'full_description': forms.Textarea(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Полное описание программы'
                }
            ),
            'image_application_main': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Главное изображение программы'
                }
            ),
            'image_application_2': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Второе изображение программы'
                }
            ),
            'image_application_3': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Третье изображение программы'
                }
            ),
            'image_application_4': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Четвёртое изображение программы'
                }
            ),
            'image_application_5': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Пятое изображение программы'
                }
            ),
            'name_file_main': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Название главного файла программы'
                }
            ),
            'file_main': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Главный файл программы'
                }
            ),
            'name_file_additional': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Название дополнительного файла программы'
                }
            ),
            'file_additional': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Дополнительный файл программы'
                }
            ),
            'verified': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input btn-outline-primary'
                }
            ),
        }

    def clean_title(self):
        """Validate that the title is not empty and does not start with a question mark"""
        name = self.cleaned_data.get('name')
        title = self.cleaned_data.get('title')

        if name.startswith('?'):
            """ Validate that the title starts with a question mark """
            raise forms.ValidationError("Title cannot start with a question mark")

        if title.startswith('?'):
            """ Validate that the title ends with a question mark """
            raise forms.ValidationError("Title cannot start with a question mark")

        return name


class AdvertisementFormAndroid(forms.ModelForm):
    """Form for creating new AndroidApplication"""

    class Meta:
        """ Meta information for AndroidApplication """
        model = AndroidApplication
        fields = [
            'name', 'title',
            'short_description', 'full_description',
            'image_application_main', 'image_application_2', 'image_application_3',
            'image_application_4', 'image_application_5',
            'name_file_main', 'file_main',
            'name_file_additional', 'file_additional',
            'verified',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Название программы',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Заголовок для программы',
                }
            ),
            'short_description': forms.Textarea(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Краткое описание программы'
                }
            ),
            'full_description': forms.Textarea(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Полное описание программы'
                }
            ),
            'image_application_main': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Главное изображение программы'
                }
            ),
            'image_application_2': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Второе изображение программы'
                }
            ),
            'image_application_3': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Третье изображение программы'
                }
            ),
            'image_application_4': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Четвёртое изображение программы'
                }
            ),
            'image_application_5': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Пятое изображение программы'
                }
            ),
            'name_file_main': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Название главного файла программы'
                }
            ),
            'file_main': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Главный файл программы'
                }
            ),
            'name_file_additional': forms.TextInput(
                attrs={
                    'class': 'form-control bg-dark text-light btn-outline-primary',
                    'placeholder': 'Название дополнительного файла программы'
                }
            ),
            'file_additional': forms.FileInput(
                attrs={
                    'class': 'form-control bg-dark text-primary btn-outline-primary',
                    'placeholder': 'Дополнительный файл программы'
                }
            ),
            'verified': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input btn-outline-primary'
                }
            ),
        }

    def clean_title(self):
        """Validate that the title is not empty and does not start with a question mark"""
        name = self.cleaned_data.get('name')
        title = self.cleaned_data.get('title')

        if name.startswith('?'):
            """ Validate that the title starts with a question mark """
            raise forms.ValidationError("Title cannot start with a question mark")

        if title.startswith('?'):
            """ Validate that the title ends with a question mark """
            raise forms.ValidationError("Title cannot start with a question mark")

        return name
