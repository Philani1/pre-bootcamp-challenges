def number_to_HM(num):
    hours = num/60
    minutes = num%60
    h_unit = ""
    m_unit = ""
    if int(hours) <= 1:
        h_unit = "hour"
    else:
        h_unit = "hours"
        
    if minutes <= 1:
        m_unit = "minute"
    else:
        m_unit = "minutes"    

    return f"{int(hours)} {h_unit}, {minutes} {m_unit}"

num = int(71)
print(number_to_HM(num))