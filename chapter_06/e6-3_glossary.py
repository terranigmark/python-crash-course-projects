
def main():
    glossary = {
        'algoritmo': 'Conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo y hallar la solución de un tipo de problemas.',
        'DOM': 'El DOM (Document Objet Model por sus siglas en inglés) es la estructura de objetos generada por el navegador al cargar un documento que puede ser modificada mediante un lenguaje de programación para cambiar dinámicamente los contenidos y aspecto de la página.',
        'HTML': 'Lenguaje de marcado para la elaboración de páginas web. HyperText Markup Language (lenguaje de marcas de hipertexto) por sus siglas en ingles.',
        'JavaScript': 'JavaScript (abreviado comúnmente JS) es un lenguaje de programación interpretado, dialecto del estándar ECMAScript. Se define como orientado a objetos, es basado en prototipos, imperativo, débilmente tipado y dinámico.',
        'Python': 'Lenguaje de programación de alto nivel y de propósito general, caracterizado por la exigencia de uso de la indentación como forma de estructura del código lo que logra una mejor lectura del mismo. Muy usado actualmente para ciencia de datos y machine learning.'
    }

    for word in glossary:
        print(f"{word}:\n\t{glossary[word]}\n")

if __name__ == "__main__":
    main()