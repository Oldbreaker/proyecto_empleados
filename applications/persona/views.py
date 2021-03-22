from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.views.generic.base import TemplateView

# models
from .models import Empleado


class InicioView(TemplateView):
    """Vista que carga la página de inicio"""
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'id'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name__icontains=palabra_clave)
        return lista


class ListByAreaEmpleado(ListView):
    'Lista empleados de un area'
    template_name = 'persona/list_by_area.html'
    queryset = Empleado.objects.filter(departamento__name='Gerencia')
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(departamento__name=area)
        return lista


class ListEmpleadosByKword(ListView):
    """ Lista  empleaod por la palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('******************************')
        palabra_clave = self.request.GET.get('kword', '')
        print('==========', palabra_clave)
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidad.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = self.request.GET.get('id', 1)
        print(empleado)
        empleado_habilidades = Empleado.objects.get(id=empleado)

        return empleado_habilidades.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # Toot un proceso
        context['titulo'] = 'Empleado del mes'
        return context


class SuccesView(TemplateView):
    template_name = "persona/succes.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

   # def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
    #    print(HttpResponse)
    #   return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/eliminar.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'id'
    context_object_name = 'empleados'
    model = Empleado
