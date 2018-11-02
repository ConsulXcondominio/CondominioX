# CondominioX
Código fuente y estructura de un Sistema de Gestión para un Condominio,
Es un Proyecto para la materia de Gestion de Calidad

Primer proyecto en HTML,CSS,BOOTSTRAP,PHP,PYTHON  Y framework DJANGO

El proyecto consistia en hacer un sistema de administracion para condominios, en el cual el propietario se pudiera registrar y luego ingresar con sus credenciales (Usuario y Contraseña). 

El proyecto usó HTML (con PHP), CSS y JavaScript para las validaciones, PHP para los controladores y MySql (MariaDB) para las BBDD, es necesario tener instalado Apache, MySql (con PhpMyAdmin) y PHP (o simplemente usar Xampp)

Para su uso:

(1) Clonar o descargar el proyecto desde GitHub y guardar
en htdocs;

(2) Iniciar el servidor Apache
	*En linux abrir terminal (ctrl + alt + t)
	y con el comando "/opt/lampp/lampp start" iniciarlo;
	*En windows abrir la interfaz grafica de Xampp y 
	clickear el boton de Iniciar;

(3) Dirigirse a "http://localhost/" y entrar en PhpMyAdmin;

(4) Crear una nueva base de datos llamada "condominios"
(Utilizar Cotejamiento utf8_spanish2_ci);

(5) Dentro de esa BBDD importar el script "condominios.sql"; 

(6) Ahora entrar en "http://localhost/condominios/registroCopropietario/index.php"
y comenzar a disfrutar;
