# Notas y Tips: Documentación de Código 📚

## 🎯 Propósito de este documento

Este archivo contiene tips prácticos, mejores prácticas y trucos para aprovechar al máximo GitHub Copilot en la generación y mantenimiento de documentación de código.

---

## 💡 Tips Generales

### 1. Selecciona bien el código antes de pedir documentación
- **✅ Hacer**: Selecciona la función/clase completa incluyendo la definición
- **❌ Evitar**: Seleccionar solo el nombre o parte del código
- **Tip**: Usa `Ctrl+Shift+[` para seleccionar todo el bloque en VS Code

### 2. Sé específico con el formato que necesitas
```
❌ "documenta esto"
✅ "Add JSDoc comments with @param and @returns"
✅ "Add Python docstring in Google style"
✅ "Add XML documentation comments for C#"
```

### 3. Pide ejemplos de uso cuando sea apropiado
```
"Add docstring with usage examples"
"Include code examples in the documentation"
```

---

## 🔧 Comandos Útiles de Copilot

### Comando `/doc`
El comando más directo para documentar código:
```
/doc
```
- Genera documentación automáticamente para el código seleccionado
- Se adapta al lenguaje y estándares del archivo
- Incluye parámetros, tipos de retorno y descripciones

### Prompts Específicos por Lenguaje

**Python:**
```
"Add docstring in Google style"
"Add docstring in NumPy style"
"Add docstring with type hints"
"Add comprehensive docstring with Args, Returns, Raises, and Examples"
```

**JavaScript/TypeScript:**
```
"Add JSDoc comments"
"Add JSDoc with @example"
"Add TypeScript JSDoc with @template"
```

**Java:**
```
"Add Javadoc comments"
"Add Javadoc with @param, @return, and @throws"
```

**C#:**
```
"Add XML documentation comments"
"Add summary and remarks XML docs"
```

---

## 📋 Checklist: ¿Qué debe incluir buena documentación?

### Para Funciones:
- [ ] Descripción clara de qué hace (una línea)
- [ ] Explicación detallada del comportamiento (si es complejo)
- [ ] Parámetros: nombre, tipo, descripción
- [ ] Valor de retorno: tipo y descripción
- [ ] Excepciones/errores que puede lanzar
- [ ] Ejemplo de uso (para funciones públicas)
- [ ] Complejidad temporal si es relevante (O(n), O(log n), etc.)
- [ ] Efectos secundarios (modificación de estado, I/O, etc.)

### Para Clases:
- [ ] Propósito de la clase
- [ ] Responsabilidades principales
- [ ] Parámetros del constructor
- [ ] Ejemplo de uso básico
- [ ] Relaciones con otras clases (si es relevante)

### Para Módulos/Archivos:
- [ ] Descripción general del módulo
- [ ] Principales funcionalidades que exporta
- [ ] Dependencias importantes
- [ ] Ejemplo de uso del módulo

---

## 🎨 Patrones de Documentación por Lenguaje

### Python - Google Style
```python
def calcular_descuento(precio, descuento, minimo=0):
    """Calcula el precio final después de aplicar un descuento.
    
    Esta función aplica un descuento porcentual al precio solo si
    el precio cumple con el mínimo requerido.
    
    Args:
        precio (float): Precio original del producto en la moneda local.
        descuento (float): Porcentaje de descuento a aplicar (0-100).
        minimo (float, optional): Compra mínima para aplicar descuento.
            Por defecto es 0.
    
    Returns:
        float: Precio final después del descuento. Si no se cumple
            el mínimo, retorna el precio original.
    
    Raises:
        ValueError: Si el descuento es negativo o mayor a 100.
    
    Examples:
        >>> calcular_descuento(100, 20)
        80.0
        
        >>> calcular_descuento(50, 20, minimo=100)
        50.0
    
    Note:
        Esta función no redondea el resultado. Si necesitas
        redondeo, aplícalo al valor retornado.
    """
    # Implementación...
```

### JavaScript - JSDoc
```javascript
/**
 * Calcula el precio final después de aplicar un descuento.
 * 
 * @param {number} precio - Precio original del producto
 * @param {number} descuento - Porcentaje de descuento (0-100)
 * @param {number} [minimo=0] - Compra mínima para aplicar descuento
 * @returns {number} Precio final después del descuento
 * @throws {Error} Si el descuento es inválido
 * 
 * @example
 * // Aplicar 20% de descuento
 * const precioFinal = calcularDescuento(100, 20);
 * console.log(precioFinal); // 80
 * 
 * @example
 * // No aplica descuento si no cumple el mínimo
 * const precioFinal = calcularDescuento(50, 20, 100);
 * console.log(precioFinal); // 50
 */
function calcularDescuento(precio, descuento, minimo = 0) {
    // Implementación...
}
```

### TypeScript - JSDoc con Tipos
```typescript
/**
 * Opciones de configuración para el cálculo de descuento
 */
interface DescuentoConfig {
    /** Porcentaje de descuento a aplicar */
    descuento: number;
    /** Compra mínima requerida */
    minimo?: number;
    /** Si se debe redondear el resultado */
    redondear?: boolean;
}

/**
 * Calcula el precio final aplicando configuración de descuento.
 * 
 * @param precio - Precio original del producto
 * @param config - Configuración del descuento
 * @returns Precio final calculado
 * 
 * @example
 * ```ts
 * const precio = calcularDescuento(100, { descuento: 20 });
 * console.log(precio); // 80
 * ```
 */
function calcularDescuento(precio: number, config: DescuentoConfig): number {
    // Implementación...
}
```

---

## 🚀 Trucos Avanzados

### 1. Regenerar documentación obsoleta
Cuando el código cambia:
```
"Update the documentation to match the current implementation"
"Regenerate docstring with new parameters"
```

### 2. Mejorar documentación existente
```
"Improve this docstring by adding examples"
"Add more detailed parameter descriptions"
"Expand the documentation with edge cases"
```

### 3. Documentar código legacy
```
"Add comprehensive documentation explaining what this complex code does"
"Document this function including its side effects"
"Explain this algorithm in the documentation"
```

### 4. Generar documentación multiidioma
```
"Add docstring in Spanish"
"Translate documentation to English"
```

### 5. Documentación de APIs
```
"Add OpenAPI documentation for this endpoint"
"Document REST API parameters and responses"
"Add Swagger documentation"
```

---

## ⚡ Atajos de Teclado Útiles

### VS Code
- `Ctrl+Shift+I`: Abrir Copilot Chat en línea
- `Ctrl+I`: Abrir Copilot inline chat
- Seleccionar código + `/doc`: Documentación rápida
- `Ctrl+.`: Quick fix (puede sugerir agregar documentación)

### Snippets Personalizados
Crea snippets para tu estándar de documentación favorito:

**Python (settings.json):**
```json
{
  "python.docstringFormat": "google"
}
```

---

## 🎯 Mejores Prácticas

### ✅ Hacer

1. **Documenta la intención, no la implementación**
   - ❌ "Este código hace un for loop y suma los valores"
   - ✅ "Calcula el total sumando todos los valores válidos"

2. **Usa verbos en presente**
   - ✅ "Calcula", "Retorna", "Valida"
   - ❌ "Calculará", "Va a retornar"

3. **Sé específico con los tipos**
   - ❌ `@param data - Los datos`
   - ✅ `@param data {Object[]} - Array de objetos usuario con propiedades id y name`

4. **Incluye unidades cuando aplique**
   - ✅ `@param timeout - Tiempo de espera en milisegundos`
   - ✅ `@returns Precio en USD con dos decimales`

5. **Documenta valores por defecto**
   - ✅ `@param retries - Número de reintentos. Por defecto: 3`

6. **Menciona efectos secundarios**
   - ✅ "Nota: Esta función modifica el array original"
   - ✅ "Advertencia: Realiza una llamada HTTP a la API"

### ❌ Evitar

1. **Documentación obvia**
   ```javascript
   // ❌ Mal
   /** Obtiene el nombre */
   function getName() { return this.name; }
   
   // ✅ Mejor no documentar si es obvio
   // O agregar contexto útil:
   /** Obtiene el nombre formateado del usuario (Apellido, Nombre) */
   ```

2. **Documentación que repite el código**
   ```python
   # ❌ Mal
   def suma(a, b):
       """Suma a y b"""
       return a + b
   ```

3. **Documentación desactualizada**
   - Es peor que no tener documentación
   - Usa Copilot para mantenerla actualizada

4. **Exceso de documentación**
   - No documentes cada variable local
   - Enfócate en APIs públicas y lógica compleja

---

## 📊 Cuándo Documentar (Prioridades)

### 🔴 Prioridad Alta (siempre documentar)
- APIs públicas
- Funciones exportadas de módulos
- Clases y sus métodos públicos
- Algoritmos complejos
- Código con comportamiento no obvio
- Funciones con efectos secundarios

### 🟡 Prioridad Media (documentar si ayuda)
- Funciones auxiliares importantes
- Métodos protegidos
- Configuraciones y constantes importantes
- Código que usa técnicas avanzadas

### 🟢 Prioridad Baja (opcional)
- Getters/setters simples
- Funciones privadas obvias
- Variables locales autoexplicativas
- Código autoexplicativo por nombres claros

---

## 🔍 Verificación de Calidad

### Checklist rápida antes de commit:
- [ ] ¿Todas las funciones públicas están documentadas?
- [ ] ¿Los parámetros y retornos están descritos?
- [ ] ¿Se mencionan las excepciones posibles?
- [ ] ¿Hay ejemplos para APIs complejas?
- [ ] ¿La documentación es clara para alguien nuevo?
- [ ] ¿Los tipos están correctamente especificados?
- [ ] ¿Se mencionan las limitaciones o casos edge?

### Herramientas útiles:
- **Python**: `pydocstyle`, `pylint`
- **JavaScript**: `ESLint` con plugins de JSDoc
- **TypeScript**: Validación de JSDoc integrada
- **Java**: `checkstyle` con reglas de Javadoc

---

## 💻 Ejercicio Práctico

**Desafío**: Toma una función sin documentar y practica diferentes prompts:

1. Básico: `/doc`
2. Específico: `Add docstring in Google style with examples`
3. Detallado: `Add comprehensive documentation including edge cases and performance notes`

Compara los resultados y aprende qué tipo de prompt da mejor documentación para tu caso.

---

## 🔗 Recursos Adicionales

### Guías de Estilo
- **Python**: [PEP 257](https://peps.python.org/pep-0257/), [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
- **JavaScript**: [JSDoc](https://jsdoc.app/), [TSDoc](https://tsdoc.org/)
- **Java**: [Oracle Javadoc Guide](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)
- **C#**: [XML Documentation](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/)

### Herramientas de Generación de Docs
- **Python**: Sphinx, MkDocs, pdoc
- **JavaScript**: JSDoc, TypeDoc, Docusaurus
- **Multi-lenguaje**: Doxygen

---

## 📝 Notas Finales

> **Recuerda**: La mejor documentación es la que ayuda a otros (y a tu yo futuro) a entender el código rápidamente. No documentes por documentar, documenta para comunicar.

> **Tip Pro**: Usa Copilot no solo para generar documentación inicial, sino también para mantenerla actualizada cuando el código cambia. Un simple "update documentation" puede ahorrar mucho tiempo.

---

**Última actualización**: Diciembre 2025  
**Versión**: 1.0
