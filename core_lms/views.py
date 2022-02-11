from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


class EditView(object):
    model = None
    success_url = None
    form = None
    template_name = None

    def update_instance(self, request, id):
        instance = get_object_or_404(self.model, pk=id)

        if request.method == 'POST':
            form = self.form(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(
                    self.get_success_ulr(instance)
                )
        else:
            form = self.form(instance=instance)

        return render(request, self.template_name, self.get_context({
            'form': form,
            'instance': instance
        }))

    def get_success_ulr(self, instance):
        return reverse(self.success_url)

    def get_context(self, context):
        return context
