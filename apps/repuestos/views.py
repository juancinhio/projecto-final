from django.shortcuts import render, reverse
from .forms import RepuestosForm
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import RepuestosForm
from .models import Repuestos
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    FormView
)
# Create your views here.

class RepuestosForm(FormView):
    form_class = RepuestosForm
    template_name = 'repuestos/repuestos.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.save()
        
        campos_seleccionados = [field_name for field_name, value in form.cleaned_data.items() if value]
        campos_seleccionados_str = ','.join(campos_seleccionados)

        detalles_url = reverse('repuesto_detalles', kwargs={'seleccionados': campos_seleccionados_str})
        return self.success_url

class RepuestosDetallesView(FormView):
    template_name = 'mostrar_detalles.html'

    def get(self, request, seleccionados):
        campos_seleccionados = seleccionados.split(',')
        detalles = {}  
        repuestos = Repuestos.objects.first()  

        for campo in campos_seleccionados:
            detalle = getattr(repuestos, f"detalle_{campo}", "")
            detalles[campo] = detalle

        context = {'campos_seleccionados': campos_seleccionados, 'detalles': detalles}
        return render(request, self.template_name, context)