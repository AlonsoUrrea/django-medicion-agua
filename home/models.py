from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
    #end class
#end class

class RaspberryPi(models.Model):
    id_raspberry = models.AutoField(primary_key=True)
    mac_address = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raspberries'
    #end class
#end class

class Sensor(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    id_raspberry = models.ForeignKey(RaspberryPi, models.DO_NOTHING, db_column='id_raspberry', blank=True, null=True)
    echo_gpio = models.IntegerField(blank=True, null=True)
    trigger_gpio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensores'
    #end class
#end class

class Tanque(models.Model):
    id_tanque = models.AutoField(primary_key=True)
    distancia_cm = models.FloatField(blank=True, null=True)
    nombre = models.CharField(max_length=64, blank=True, null=True)
    id_sensor = models.ForeignKey(Sensor, models.DO_NOTHING, db_column='id_sensor', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tanques'
    #end class
#end class

class Medicion(models.Model):
    id_mediciones = models.AutoField(primary_key=True)
    dato_natural = models.FloatField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    id_sensor = models.ForeignKey(Sensor, models.DO_NOTHING, db_column='id_sensor', blank=True, null=True)
    hora_fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mediciones'
    #end class

    def porcentaje_a_100(self):
        return round(self.porcentaje * 100, 2)
    #end def
#end class
