# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:40:43 2021

@author: 57314
"""
#iva= 19 %
#entrada
ingr_tot_pag =int(input("digite valor a pagar:"))

#proceso

prod_iva= ingr_tot_pag*19 

des_prod= ingr_tot_pag *0.05 /100

tot_pag= ingr_tot_pag*19*0.05 


#salida
print("el iva de su producto es:", ingr_tot_pag*19)
print("su descuesto de lproducto es:", ingr_tot_pag*0.05)

print("su total a pagar es:" ,ingr_tot_pag*19*0.05)

