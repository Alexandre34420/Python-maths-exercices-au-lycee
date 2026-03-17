def tarif_1 (d):
    if d<200 :
        t=79
    else:
        t=79+((d-200)*0.5)
    return t

def tarif_2 (d):
    t=116.86
    return t

def meilleur (d):
    if  79+((d-200)*0.5)>116.86:
        return tarif_1
    else:
        return tarif_2
