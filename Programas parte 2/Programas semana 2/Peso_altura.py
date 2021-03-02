def peso_altura():
    return 77, 1.83


def pagamento_semanal(valor_por_hora, numero_horas = 40):
    assert valor_por_hora >= 0 and numero_horas > 0
    
    return valor_por_hora * numero_horas

def calculo(x, y = 10, z = 5):
    return x + y * z;

def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s
