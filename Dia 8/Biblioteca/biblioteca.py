def agregar_libro(self, libro):
    self._libros.append({
        "titulo": libro.titulo,
        "autor": libro.autor,
        "cantidad_de_paginas": libro.cantidad_de_paginas,
        "genero": libro.genero,
        "sinopsis": libro.sinopsis,
    })