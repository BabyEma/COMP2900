payrate = float(input('Pago por hora: '))
houRate = float(input('Horas trabajadas:'))

overtimeHours = 0 
if (houRate > 40):
    overtimeHours = houRate - 40
    totalPay = (40 * payrate) + (overtimeHours * (payrate * 2))
else:
    totalPay = houRate + payrate

    print(f'El sueldo a pagar es: {totalPay})')


