from django.utils.functional import lazy
# from django.contrib.auth.password_validation import password_validators_help_texts
from django.utils.html import format_html, format_html_join


def _validators_help_texts(validators):
  help_texts = []
  if validators is not None:
    for validator in validators:
      help_texts.append(validator.get_help_text())
    return help_texts


def _validators_help_text_html(validators=None, help_text_wrapper=None):
  """
  Return an HTML string with all help texts of all configured validators
  """
  print(f'{validators = }')

  if help_text_wrapper is None:
    help_text_wrapper = {
    'element': ('div', {'class':''}),
    'grouped': ('div', {'class':''})
  }

  help_texts = _validators_help_texts(validators)

  html_generator = ((
    help_text,
    help_text_wrapper['element'][0],
    help_text_wrapper['element'][1]['class']
  ) for help_text in help_texts )
  help_items = format_html_join('', '<{1} class="{2}">{0}</{1}>', html_generator)

  html_group_generator = (
    help_items,
    help_text_wrapper['grouped'][0],
    help_text_wrapper['grouped'][1]['class']
  )
  return format_html('<{1} class="{2}">{0}</{1}>', *html_group_generator) if help_items else ""
  
  # return help_items

help_text_html = lazy(_validators_help_text_html, str)
