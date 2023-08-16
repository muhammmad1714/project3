class BulmaMixin(object):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.input_type in ('text', 'email', 'password', 'number', 'urls'):
                visible.field.widget.attrs['class']= 'input'
            elif visible.field.widget.widget.input_type == 'file':
                visible.field.widget.template_name = 'file_input.html'