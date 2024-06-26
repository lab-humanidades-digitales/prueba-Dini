## LIBRERIA
import streamlit as st

## Diccionario de números entre 1 y 10
D = {0:'', 1:'huk', 2:'iskay', 3:'kimsa', 4:'tawa', 5:'pichqa', 6:'suqta', 7:'qanchis', 8:'pusaq', 9:'isqun', 10:'chunka'}

## Terminación en vocal o consonante

## input: string s
def sufijo(s):
    ## si termina en vocal
    if s[-1] in 'aeiou':
        s = s + '-yuq'
    ## termina en consonante
    else:
        s = s + '-ni-yuq'
    return s

## Función que recibe un entero entre 1 y 99, y entrega su versión en palabras

## input: entero n entre 1 y 99
def quechua(n):
    ## el número es menor o igual a 10
    if n <= 10:
        ## usamos el diccionario
        s = D[n]
    ## el número es mayor a 10
    else:
        ## el número comienza con chunka
        s = 'chunka'
        
        ## extraemos la decena y la unidad
        decena = n//10
        unidad = n%10
        
        ## agregamos la unidad
        s = s + ' ' + D[unidad]
        
        ## si la decena es mayor a 1
        if decena > 1:
            s = D[decena] + ' ' + s
            
        ## agregamos el sufijo
        if unidad!=0:
            s = sufijo(s)
    return s

##titulo
st.title ('Descubre tu número favorito en quechua!')

n_input = st.slider("Selecciona un número entre 1 y 99 ❤️", 1, 99, 1)

st.write(quechua(n_input))
