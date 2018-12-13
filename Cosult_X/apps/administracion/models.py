from django.db import models
from datetime import datetime
from calendar import *
import datetime


##################################################
################# EMPLEADO  ######################


class Empleado(models.Model):
    #la llave primaria por defecto si no colocamos impliciatamente django lo creara.
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    cedula = models.IntegerField()

    C1 = (('Administrador', 'Administrador'), ('Recepcionista', 'Recepcionista'), ('Guardia', 'Guardia'))
    cargo = models.CharField(max_length=30, choices=C1, default='Administrador')



    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellidos)



############################################################
#####################  AREA  ###############################

class Area(models.Model):

    CAMP = (('Cancha', 'Cancha'), ('Piscina', 'Piscina'),('Churrasquera', 'Churrasquera'))
    seccion =models.CharField(max_length=20, choices=CAMP, default='Cancha')

    nombre = models.CharField(max_length=50)

    CAMP2 = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'))
    sector = models.CharField(max_length=20, choices=CAMP2, default='A')

    CAMP8 = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'))
    CAMP9 = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'))
    horaHora = models.CharField(max_length=20, choices=CAMP8, default='1')
    horaMinutos=models.CharField(max_length=20, choices=CAMP9, default='1')

    descripcion = models.TextField(default=' ')


    ESTADO = (('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Mantenimiento', 'Mantenimiento'))
    estado = models.CharField(max_length=20, choices=ESTADO, default='Activo')

    TIEMPO1 = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),('9', '9'), ('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'))
    tiempoVisitaTiempo = models.CharField(max_length=150, choices=TIEMPO1, default='1')



    HORAS = (('Horas', 'Horas'), ('Minutos', 'Minutos'))
    tiempoHoras = models.CharField(max_length=50, choices=HORAS, default='Horas')


    def __str__(self):
        #return '{0} {1} {2} {3} {4} {5} {6}'.format(self.nombre, self.tipo, self.sector,self.horario,self.descripcion,self.tiempo,self.estado)
        return '{0} {1} Sector:{2}'.format(self.nombre,'  -  ',self.sector)





###############################################################
########################  PRPIETARIO  #########################
class Propietario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    cedula = models.IntegerField()
    numero_casa = models.IntegerField()


    def __str__(self):
        cadena = "{0}  {1} Numero de casa: {2} "
        return cadena.format(self.nombre, self.apellidos, self.numero_casa)



#########################################
#################  RESERVA  #############


class Reserva(models.Model):

    propietario =  models.ForeignKey(Propietario, null=True, blank=True)
    area = models.ForeignKey(Area, null=True, blank=True)
    fecha = models.DateField()


    CAMP7 = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'))
    CAMP6 = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'))
    desdeHora = models.CharField(max_length=20, choices=CAMP7, default='1')
    hastaHora =models.CharField(max_length=20, choices=CAMP6, default='1')

    empleado = models.ForeignKey(Empleado, null=True, blank=True)

    def __str__(self):
        cadena = "{0}  {1}  {2}  {3}"
        return cadena.format(self.hora, self.propietario, self.area, self.empleado)



####################################################
###################### VISITA ###################



class Visita(models.Model):
    #la llave primaria por defecto si no colocamos impliciatamente django lo creara.

   # formato1 = date.today()

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    cedula = models.IntegerField()
    observacion = models.TextField(blank=True)
    fechaEntrada = models.DateField()
    fechaSalida = models.DateField()

    TIEMPO1 = (('1','1'), ('2','2'), ('3','3'), ('4','4'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10'))
    tiempoVisitaTiempo = models.CharField(max_length=150, choices=TIEMPO1, default='1')


    HORAS = (('Horas', 'Horas'), ('Minutos', 'Minutos'))
    tiempoHoras =models.CharField(max_length=50, choices= HORAS, default='Hora')

    MODO1 = (('Auto', 'Auto'), ('Bicicleta', 'Bicicleta'),('Moto', 'Moto'), ('A pie', 'A pie'))
    modoEntrada = models.CharField(max_length=150, choices= MODO1, default='Auto')

    propietario = models.ForeignKey(Propietario, null=True, blank=True)

    def __str__(self):
        return '{0} {1}  {2}'.format(self.nombre, self.apellidos, self.cedula)

#ESTADO = (('activo', 'activo'), ('inactivo', 'inactivo'))









