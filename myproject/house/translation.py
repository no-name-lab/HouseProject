from modeltranslation.translator import translator, TranslationOptions
from .models import Property, Region

class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address')


translator.register(Property, PropertyTranslationOptions)

