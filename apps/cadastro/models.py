from django.db import models
from..turma.models import Turma

class Cadastro(models.Model):

    UF = (('AC','Acre'),('AL','Alagoas'),('AP','Amapá'),('AM','Amazonas'),('BA','Bahia'),('CE','Ceará'),
          ('DF','Distrito Federal'),('ES','Espírito Santo'),('GO','Goiás'),('MA','Maranhão'),('MG','Minas Gerais '),
          ('MS','Mato Grosso do Sul'),('MT','Mato Grosso'),('PA','Pará'),('PB','Paraíba'),('PE','Pernambuco'),
          ('PI','Piauí'),('PR','Paraná'),('RJ','Rio de Janeiro'),('RN','Rio Grande do Norte'),('RO','Rondônia'),
          ('RR','Roraima'),('RS','Rio Grande do Sul'),('SC','Santa Catarina'),('SE','Sergipe'),('SP','São Paulo'),
          ('TO','Tocantins'),
    )

    PERIODO = (('MANHA', 'MANHA'),('TARDE', 'TARDE'),('NOITE', 'NOITE'))

    EST_CIVIL = (('SOLTEIRO','SOLTEIRO'),('CASADO', 'CASADO'),('SEPARADO', 'SEPARADO'),('DIVORCIADO','DIVORCIADO'),('VIUVO', 'VIUVO'))

    OP = (('SIM', 'SIM'),('NAO', 'NAO'))

    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=50)
    nascimento = models.DateField()
    local_de_nascimento = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=UF)
    celular = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50)
    escola = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    periodo = models.CharField(max_length=20, choices=PERIODO) 
    pai = models.CharField(max_length=50)
    profissao_pai = models.CharField(max_length=50, null=True, blank=True)
    mae = models.CharField(max_length=50)
    profissao_mae = models.CharField(max_length=50, null=True, blank=True)
    estado_civil = models.CharField(max_length=20, choices=EST_CIVIL) 
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    movimento_pastoral = models.CharField(max_length=50)
    batizado = models.CharField(max_length=20, choices=OP)
    data_batizado = models.DateField()
    eucaristia = models.CharField(max_length=20, choices=OP)
    cidade_eucaristia = models.CharField(max_length=50)
    paroquia = models.CharField(max_length=50)
    diocese = models.CharField(max_length=50)
    historico = models.TextField(max_length=500, blank=True, null=True, help_text=u"Ano - Curso - Idade - Catequista - Frequência - Aproveitamento")

    def __str__(self):
        return self.nome+' - '+self.pai+' - '+self.mae
