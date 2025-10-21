# TuPrimeraPagina-Castro
TechBlog

TechBlog es un proyecto web que hice con Django como práctica para aprender sobre desarrollo web. La idea es crear un blog de tecnología donde se puedan publicar y buscar artículos sobre temas como inteligencia artificial, desarrollo, criptomonedas, robótica y otros temas relacionados. El diseño de la página lo generé con ayuda de una inteligencia artificial, y después lo adapté para que funcione bien con Django y Tailwind CSS.

El sitio tiene un sistema de registro e inicio de sesión. Cualquier usuario puede registrarse llenando un formulario con su nombre, correo y contraseña, y luego iniciar sesión con esos mismos datos. Una vez que inicia sesión correctamente, el usuario es redirigido al inicio donde puede ver todas las publicaciones del blog.

Por ahora, los posts se crean desde el panel de administración de Django (http://127.0.0.1:8000/admin
). Para crear un post hay que tener un usuario administrador, entrar al panel, ir a la sección “Posts” y cargar los campos necesarios: el título, el contenido, la categoría y la fecha de creación. Las categorías también se pueden agregar desde el mismo panel, en la parte de “Categorías”.

No sé todavía cómo hacer para subir imágenes desde Django usando Python, así que las imágenes de los posts se generan automáticamente con enlaces precargados que me dio la inteligencia artificial. Por eso, algunas no tienen relación directa con el tema del artículo (por ejemplo, puede aparecer una imagen de una computadora en un post sobre inteligencia artificial o viceversa).

El sitio permite buscar publicaciones por nombre o por categoría usando una barra de búsqueda. Además, cuando el usuario inicia sesión correctamente o hay algún error, se muestran mensajes automáticos para avisar lo que pasó.


el superusuario es: roman
la contraseña es: roman12345