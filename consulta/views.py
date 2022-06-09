
from django.db.models import Q
from .models import Medico
from django.views.generic import ListView, DetailView
# Create your views here.


class ListViewBase(ListView):
    model = Medico
    context_object_name = 'medicos'
    ordering = ['-id']
    template_name = 'consulta/pages/home.html'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(publicado=True,)

        return qs


class ListViewEspecialidade(ListViewBase):
    template_name = 'consulta/pages/especialidade.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            publicado=True,
            especialidade__id=self.kwargs.get('especialidade_id'),
        )
        return qs


class ListViewSearch(ListViewBase):
    template_name = 'consulta/pages/search.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('search', '').strip()
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(nome_completo__icontains=search_term) |
                Q(crm__icontains=search_term),
            ),
            publicado=True
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('search', '').strip()

        ctx.update({'search_term': search_term})
        return ctx


class MedicoView(DetailView):
    model = Medico
    context_object_name = 'medico'
    template_name = 'consulta/pages/medico.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            publicado=True,
            pk=self.kwargs.get('pk'),
        )
        return qs
