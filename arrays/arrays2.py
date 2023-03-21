def get_cob():
    return [
        {'id':1, 'cob':'cob1'},
        {'id':2, 'cob':'cob2'},
        {'id':3, 'cob':'cob3'}
    ]

def get_riesgos():
    coberturas = get_cob()
    return [
        {'id':1, 'riesgo':'riesgo1', 'cob':coberturas[0]},
        {'id':2, 'riesgo':'riesgo2', 'cob':coberturas[1]},
        {'id':3, 'riesgo':'riesgo3', 'cob':coberturas[2]},
    ]

def get_endosos():
    riesgos = get_riesgos()
    return [
        {'id':1, 'endoso':'endoso1', 'riesgos':[]},
        {'id':2, 'endoso':'endoso2', 'riesgos':[]},
        {'id':3, 'endoso':'endoso3', 'riesgos':riesgos},
    ]

def get_endosos2():
    riesgos = get_riesgos()
    return [
        {'id':1, 'endoso':'endoso1', 'riesgos':[]},
        {'id':2, 'endoso':'endoso2', 'riesgos':[]},
        {'id':3, 'endoso':'endoso3', 'riesgos':riesgos},
    ]

def get_endosos3():
    riesgos = get_riesgos()
    return [
        {'id':1, 'endoso':'endoso1', 'riesgos':[]},
        {'id':2, 'endoso':'endoso2', 'riesgos':[]},
        {'id':3, 'endoso':'endoso3', 'riesgos':riesgos},
        {'id':4, 'endoso':'endoso4', 'riesgos':riesgos},
        {'id':5, 'endoso':'endoso4', 'riesgos':riesgos},
    ]

def get_polizas():
    endosos = get_endosos()
    return [
        {'id':1, 'poliza':'poliza1', 'endosos':endosos},
    ]

def get_polizas2():
    endosos = get_endosos2()
    return [
        {'id':1, 'poliza':'poliza1', 'endosos':endosos},
    ]

def get_polizas3():
    endosos = get_endosos3()
    return [
        {'id':1, 'poliza':'poliza1', 'endosos':endosos},
    ]

polizas = get_polizas()
endosos = polizas[0].get('endosos')

polizas2 = get_polizas2()
endosos2 = polizas2[0].get('endosos')

polizas3 = get_polizas3()
endosos3 = polizas3[0].get('endosos')

"""
FUNCTION: 
Compare between 2 arrays and if one is largest add the new items to the 1st array

param1: 1st array (original)
param2: 2nd array (for compare)
return: 1st array with the added item or without it
"""
def function(array1, array2):
    for i in range(len(array2)):
        if (len(array1) > i) == False:
            array1.append(array2[i])
    return array1
    
print("CASO 1: MISMOS ENDOSOS")
print(function(endosos, endosos2))
print("CASO 2: NUEVOS ENDOSOS")
print(function(endosos, endosos3))

array = [
    [], 
    ['0', 'RENOVACION', '21/04/2021', '21/05/2021', '21/05/2022', '1.299,40', '129,94', '396,14', '1.825,48', '456,31', '1.369,17', '0,00', '10/08/2021'], 
    ['1', 'ENDOSOS', 'MODIFICACION DE RIESGO', '28/04/2021', '21/05/2021', '21/05/2022', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '0,00', '/ /']
]

array.pop(0)
for j in range(len(array)):
    for i in range(len(array[j])):
        print(i, " ", array[j][i])
  
