def calc_pay (iHoursWorked, iHourlyWage, iTaxRate, iFicaValue) :
    iGrossPay = (iHoursWorked*iHourlyWage)
    iTaxes = iGrossPay*iTaxRate
    iFica = iGrossPay*iFicaValue
    iTakeHomePay = round(iGrossPay - iTaxes - iFica, 2)

    return iTakeHomePay
