"""Module for translating diffrent languages"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Function to translate English to French text"""
    my_mem_translator = MyMemoryTranslator(source = 'en', target = 'fr')
    french_text = my_mem_translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Function to translate French to English text"""
    my_mem_translator = MyMemoryTranslator(source = 'fr', target = 'en')
    english_text = my_mem_translator.translate(french_text)
    return english_text
