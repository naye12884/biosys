import peewee as pw
from pyairtable.orm import Model
from pyairtable.orm import fields

#BASE DE DATOS LOCAL
base_datos = pw.SqliteDatabase("base_datos.db")

class Usuario(pw.Model):
    clave  = pw.TextField(primary_key=True)
    contra = pw.TextField()
    nombre = pw.TextField()
    admin  = pw.IntegerField()
    class Meta:
        database = base_datos

#usuarios = Usuario.select()
#for u in usuarios:
#    print(u.clave, u.contra, u.nombre, u.admin)

#BASE DE DATOS EN LA NUBE
