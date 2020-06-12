# from django.views.generic.edit import FormMixin, ProcessFormView


# class MultipleFormsMixin(FormMixin):
#     """
#     A mixin that provides a way to show and handle several forms
#     in a single request.
#     """

#     form_classes = dict()

#     def get_form_classes(self):
#         return self.form_classes

#     def get_forms(self, form_classes):
#         for key, klass in form_classes.items():
#             return dict([(key, klass(**self.get_form_kwargs()))])

#     def forms_valid(self, forms):
#         return super(MultipleFormsMixin, self).form_valid(forms)

#     def forms_invalid(self, forms):
#         return self.render_to_response(self.get_context_data(forms=forms))

#     def get_context_data(self, **kwargs):
#         if 'forms' not in kwargs:
#             kwargs['forms'] = self.get_forms(form_classes=self.get_form_classes())
#         return super().get_context_data(**kwargs)


# class ProcessMultipleFormsMixin(ProcessFormView):
#     """
#     A mixin that processes multiple forms on POST request.
#     Every form must be valid.
#     """

#     def get(self, request, *args, **kwargs):
#         form_classes = self.get_form_classes()
#         forms = self.get_forms(form_classes)
#         return self.render_to_response(self.get_context_data(form=forms))

#     def post(self, request, *args, **kwargs):
#         form_classes = self.get_form_classes()
#         forms = self.get_forms(form_classes)
#         if all([form.is_valid() for form in form.values()]):
#             return self.forms_valid
#         return self.forms_invalid(forms)
