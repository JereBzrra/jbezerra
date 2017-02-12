from django import forms

class ContatoForm(forms.Form):

    class Meta:
        fields = ('nome','telefone', 'celular','mail','tit_menagem','mensagem')

