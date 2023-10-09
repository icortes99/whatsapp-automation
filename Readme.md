# Proyecto de Automatización de WhatsApp

Este proyecto te permite automatizar el envío de mensajes de WhatsApp a grupos específicos. Antes de comenzar, asegúrate de seguir estos pasos de configuración.

## Requisitos Previos

- **Python**: Debes tener Python instalado en tu sistema. Puedes descargarlo desde [Python.org](https://www.python.org/downloads/). Se recomienda usar Python 3.x.

- **pip**: pip es el administrador de paquetes de Python y generalmente se instala automáticamente junto con Python. Verifica que pip esté instalado ejecutando `pip --version` en tu terminal.

## Creación de un Entorno Virtual (Opcional pero recomendado)

Si deseas, puedes crear un entorno virtual para este proyecto. Esto ayuda a mantener las dependencias del proyecto separadas de otras aplicaciones Python en tu sistema.

1. **Crea un Entorno Virtual** (en la raíz del proyecto):

python -m venv venv


2. **Activa el Entorno Virtual**:

- En Windows:
  ```
  .\venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

## Instalación de la Biblioteca pywhatkit

Para ejecutar este proyecto, necesitas la biblioteca `pywhatkit`. Puedes instalarla utilizando pip:

pip install pywhatkit


Sigue las instrucciones y mensajes en la terminal para enviar mensajes a los grupos correspondientes.

## Notas Adicionales

- Si deseas personalizar los mensajes, modifica las variables `mensaje_nuevo_estudiante` y `mensaje_pareja_estudiantes` en `main.py`.
- Recuerda respetar la privacidad y las políticas de uso de WhatsApp al enviar mensajes automatizados.