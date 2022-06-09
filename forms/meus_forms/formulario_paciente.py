
from consulta.models import Paciente
from django import forms


class CadastroPaciente(forms.ModelForm):
    nome_completo = forms.CharField(
        required=True,
        help_text='Digite seu nome completo',
        error_messages={'required': 'Campo obrigatorio'}
    )

    idade = forms.CharField(
        required=True,
        widget=forms.NumberInput,
        error_messages={'required': 'Campo obrigatorio'}
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu email aqui'})
    )

    sexos = [('Feminino', 'Feminino'), ('Masculino', 'Masculino')]
    genero = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=sexos,
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={
                'type': 'datetime-local',
            }),
        input_formats=('%Y-%m-%dT%H:%M',),
    )

    class Meta:
        model = Paciente
        fields = 'nome_completo', 'idade', 'genero',\
            'email', 'telefone', 'date',
