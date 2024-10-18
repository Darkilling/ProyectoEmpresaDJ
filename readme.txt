instalar venv

python -m ensurepip --upgrade
-----------

correr venv

venv\Scripts\activate  #en windows

si tienes este error

venv\Scripts\activate : No se puede cargar el archivo C:\Users\Hernan-PC\Documents\generacion ot\venv\Scripts\Activate.ps1 porque la ejecución de scripts está deshabilitada en este sistema. Para obtener más información, consulta el tema about_Execution_Policies en https:/go.microsoft.com/fwlink/?LinkID=135170.
En línea: 1 Carácter: 1
+ venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess


se soluciona asi:

Abrir PowerShell como administrador:

Haz clic derecho en el ícono de Windows y selecciona Windows PowerShell (Administrador) o busca PowerShell en el menú de inicio y elige "Ejecutar como administrador".
Cambiar la política de ejecución: En la ventana de PowerShell que se abrió como administrador, ejecuta el siguiente comando para permitir la ejecución de scripts:

bash
Copiar código
Set-ExecutionPolicy RemoteSigned
Esto permitirá la ejecución de scripts locales y remotos firmados.

Confirma el cambio: Se te pedirá que confirmes el cambio. Escribe Y y presiona Enter.

Activar el entorno virtual




recuerda instalar las dependencias de requirements.txt

comando: pip install -r requirements.txt
