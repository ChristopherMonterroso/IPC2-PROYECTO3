from django import forms

class FileForm(forms.Form):
    forms.FileField(label="file")

class AddFormRecurso(forms.Form):
   id_recurso = forms.CharField(label="id_recurso")
   nombre = forms.CharField(label="nombre")
   abreviatura = forms.CharField(label="abreviatura")
   metrica = forms.CharField(label="metrica") 
   tipo = forms.CharField(label="tipo") 
   valor_x_hora = forms.CharField(label="valor_X_hora") 

class AddFormCategoria(forms.Form):
   id = forms.CharField(label="id")
   nombre = forms.CharField(label="nombre")
   descripcion = forms.CharField(label="descripcion")
   cargaTrabajo = forms.CharField(label="cargaTrabajo") 

class AddFormConfiguracion(forms.Form):
   id_categoria = forms.CharField(label="id_categoria")
   id = forms.CharField(label="id")
   nombre = forms.CharField(label="nombre")
   descripcion = forms.CharField(label="descripcion") 

class AddFormCliente(forms.Form):
   nit = forms.CharField(label="nit")
   nombre = forms.CharField(label="nombre")
   usuario = forms.CharField(label="usuario")
   clave = forms.CharField(label="clave") 
   direccion = forms.CharField(label="direccion")
   email = forms.CharField(label="email") 

class AddFormInstancia(forms.Form):
   nit = forms.CharField(label="nit")
   id_i = forms.CharField(label="id_i")
   id_c = forms.CharField(label="id_c")
   nombre = forms.CharField(label="nombre") 
   fechaInicio = forms.CharField(label="fechaInicio")
   estado = forms.CharField(label="estado")
   fechafinal = forms.CharField(label="fechafinal")

 
  
