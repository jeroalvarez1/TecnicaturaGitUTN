
# Mensaje segun su edad

edad = int(input("Digite su edad: "))

mensaje = None #None es equivalente a null en python

if 0 <= edad < 10:
    mensaje = 'La infancia es increíble y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios y mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Dale importancia al amor y comienza el trabajo'
elif 30 <= edad < 65:
    mensaje = "Disfruta de tu familia que es el tesoro mas preciado"
elif 65 <= edad <120:
    mensaje = "Nunca es tarde para cumplir tus sueños"
else:
    mensaje = 'ERROR, etapa de vida incorrecta'

print(f"Tienes {edad} años, {mensaje} ")