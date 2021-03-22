from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento


class NewDepartamentroView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shorname']

        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa)
        return super().form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/listar_departamentos.html"
    context_object_name = 'departamentos'
