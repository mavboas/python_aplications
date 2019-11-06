''' Autor:  Marcelo Augusto Vilas Boas
Data:   05/11/2019

Esta função tem como objetivo verificar se o dia atual é util, se sim a data atual é retornada;
se não é retonado o próximo dia util.

OBS: É levado em consideração somente os feriados brasileiros nacionais'''

import datetime
from workalendar.america import Brazil
from datetime import datetime


def dia_util():
    cal = Brazil()
    cal.holidays(2019)

    # dia de hj
    hoje = datetime.now()

    ano = hoje.year
    mes = hoje.month
    dia = hoje.day

    #verifica
    data = ('{0}/{1}/{2}').format(ano,mes,dia)
    data = datetime.strptime(data, '%Y/%m/%d').date()

    varind = (cal.is_working_day((data)) ) # é domingo

    # Retorna se o dia atual é util
    verifica_dia = varind

    #verifica e altera se não for um dia util.

    while varind ==  False:
        data = datetime.fromordinal(data.toordinal() + 1)
        varind = (cal.is_working_day((data)))  # é domingo

    # coleta o ANO, MES e DIA  da data final para inserir no código
    ano = data.year
    mes = int(data.month)
    dia = int(data.day)

    if mes < 10:
        mes = '0{0}'.format(mes)

    if dia < 10:
        dia = '0{0}'.format(dia)

    datafinal = '{0}/{1}/{2}'.format(dia,mes,ano)

    return datafinal,verifica_dia




