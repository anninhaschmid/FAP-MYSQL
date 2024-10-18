from django.db import models
class Pacientes(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    cpf = models.TextField(unique=True)
    data_consulta = models.DateField()
    senha = models.CharField(max_length=128)
    telefone = models.TextField(max_length=15)
class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    data_disponivel = models.DateField()
    telefone = models.TextField(max_length=15)
class AgendamentoConsulta(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    def __str__(self):
        return f'Consulta marcada: {self.paciente.nome} com {self.medico.nome} em {self.data} às {self.hora}'
