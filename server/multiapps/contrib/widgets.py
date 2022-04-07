from django.forms import CheckboxSelectMultiple

class CheckboxSelectMultipleWidget(CheckboxSelectMultiple):

  class Media:
    css = {
      'screen': ('widgets/css/checkbox_select_multiple.css',)
    }
    js = (
      'vendor/js/jquery-3.6.0.js',
      'widgets/js/lodash.min.js',
      'widgets/js/checkbox_select_multiple.js',
    )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.attrs['size'] = 10
  