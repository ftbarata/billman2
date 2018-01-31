from django.db import models
from django.core import validators
from django.conf import settings

class Service(models.Model):
    customer = models.ForeignKey('CustomerDetails', verbose_name='Cliente', on_delete=models.CASCADE)
    description = models.CharField('Descrição', max_length=500)
    unit_price = models.FloatField('Valor unitário', null=True, blank=True)
    count = models.IntegerField('Quantidade', null=True, blank=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.customer + ' - ' + self.description


class CustomerDetails(models.Model):
    class Meta:
        verbose_name = 'Detalhe do cliente'
        verbose_name_plural = 'Detalhes do cliente'

    customer_type = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )

    email = models.EmailField(primary_key=True, max_length=60)
    alternative_email = models.EmailField(max_length=60, null=True, blank=True)
    type = models.CharField('tipo', max_length=2, choices=customer_type, null=True, blank=True)
    name = models.CharField('nome',max_length=100, null=True, blank=True)
    razao_social = models.CharField('Razão Social', max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    responsibles = models.CharField('Responsáveis', max_length=300, null=True, blank=True)
    phones = models.CharField('Telefones', max_length=100, blank=True)
    services = models.ManyToManyField('Service', blank=True)
    billing_send_date = models.PositiveIntegerField('Dia de envio da fatura', validators=[validators.MaxValueValidator(28)], null=True, blank=True)
    billing_due_date = models.PositiveIntegerField('Dia de vencimento da fatura', validators=[validators.MaxValueValidator(28)], null=True, blank=True)
    created_at = models.DateField('Atualizado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)
    observations = models.CharField('Observações', max_length=500, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', blank=True, null=True)

    def __str__(self):
        return self.email


class BillingControl(models.Model):
    customer = models.ForeignKey(CustomerDetails, verbose_name='Cliente', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', verbose_name='Serviço', on_delete=models.CASCADE)
    attach_bill = models.BooleanField(default=False, verbose_name='Gerar boleto')
    active = models.BooleanField(verbose_name='Ativo', default=False)
    paid = models.BooleanField(verbose_name='Pago', default=False)

    class Meta:
        verbose_name = 'Controle de Cobrança'
        verbose_name_plural = 'Controles de Cobrança'

    def __str__(self):
        return self.customer.email + ' - ' + self.service.description


class ScheduledPrice(models.Model):
    customer = models.ForeignKey(CustomerDetails, verbose_name='Cliente', on_delete=models.CASCADE)
    send_date = models.DateField('Data de envio')
    duedate = models.DateField('Vencimento')
    description = models.CharField('Descrição', max_length=500)
    unit_price = models.FloatField('Valor unitário')
    count = models.IntegerField('Quantidade')
    attach_bill = models.BooleanField(default=False, verbose_name='Gerar boleto')

    class Meta:
        verbose_name = 'Agendamento de Cobrança'
        verbose_name_plural = 'Agendamentos de Cobranças'

    def __str__(self):
        return self.customer.email + ' - ' + self.description


class BillingHistory(models.Model):
    customer = models.ForeignKey(CustomerDetails, verbose_name='Cliente', on_delete=models.CASCADE)
    description = models.CharField('Descrição', max_length=500)
    value = models.FloatField('Valor', null=True, blank=True)
    date = models.DateField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Histórico Financeiro'
        verbose_name_plural = 'Históricos Financeiros'

    def __str__(self):
        return self.date


class OperationHistory(models.Model):
    customer = models.ForeignKey(CustomerDetails, verbose_name='Cliente', on_delete=models.CASCADE)
    ip_address = models.CharField('Endereço IP', max_length=50)
    description = models.CharField('Descrição', max_length=500)
    datetime = models.DateTimeField('Data/Hora', auto_now=True)

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Histórico de Operações'
        verbose_name_plural = 'Históricos de Operações'