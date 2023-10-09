import pywhatkit as whats

mensaje_nuevo_estudiante = "Eso eso. Es para recordarte de postear tu status diario. Si por alguna razón no pueden avanzar un día, su status puede ser lo que tienen planeado para el siguiente dia. De esta forma podemos medir tu progreso y ayudarte en los módulos que más tiempo te demandan"

mensaje_pareja_estudiantes = "Hola Devs! Es para recordarles de postear su status diario. Si por alguna razón no pueden avanzar un día, su status puede ser lo que tienen planeado para el siguiente dia. De esta forma podemos medir su progreso y ayudarles en los módulos que más tiempo les demanda. Si ya lo hicieron pueden ignorar el mensaje. Muchas gracias! :D"

#Abrir y leer el archivo whats_info.txt
with open("whats_info.txt", "r") as archivo:
  lineas = archivo.readlines()

for linea in lineas:
  partes = linea.strip().split(": ")

  if len(partes) == 2:
    clave, valor = partes[0], partes[1]

    if clave == "ID_grupo":
      id_grupo = valor
    elif clave == "Tipo_mensaje":
      tipo_mensaje = valor
    elif clave == "Estado" and valor == "activo":
      estado_activo = True

      if estado_activo:
        if tipo_mensaje == "nuevo_estudiante":
          whats.sendwhatmsg_to_group_instantly(id_grupo, mensaje_nuevo_estudiante, 15, True, 3)
        elif tipo_mensaje == "pareja_estudiantes":
          whats.sendwhatmsg_to_group_instantly(id_grupo, mensaje_pareja_estudiantes, 15, True, 3)