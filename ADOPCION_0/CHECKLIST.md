# Checklist de Verificación - GitHub Copilot ✅

## 📋 Pre-Instalación

- [ ] Tengo una cuenta de GitHub activa
- [ ] Tengo acceso a GitHub Copilot (verificado en github.com/settings/copilot)
- [ ] Visual Studio Code instalado (v1.85 o superior)
- [ ] Conexión a Internet estable

---

## 🔧 Instalación

### Extensiones Instaladas

- [ ] Extensión "GitHub Copilot" instalada
- [ ] Extensión "GitHub Copilot Chat" instalada
- [ ] Ambas extensiones están habilitadas (no deshabilitadas)
- [ ] Versión de las extensiones actualizada a la más reciente

### Autenticación

- [ ] He iniciado sesión en GitHub desde VS Code
- [ ] He autorizado GitHub Copilot en el navegador
- [ ] El ícono de Copilot aparece en la barra de estado (inferior derecha)
- [ ] El ícono NO muestra error (X roja o señal de prohibido)

---

## ✅ Verificación de Funcionamiento

### Autocompletado

Crea un archivo `test.js` y prueba:

- [ ] Al escribir un comentario descriptivo, Copilot sugiere código
- [ ] Las sugerencias aparecen en color gris (ghost text)
- [ ] Puedo aceptar sugerencias con `Tab`
- [ ] Puedo rechazar sugerencias con `Esc`
- [ ] Puedo ver múltiples sugerencias con `Alt+]` y `Alt+[`

**Código de prueba:**
```javascript
// función para calcular el factorial de un número
```

**¿Copilot sugirió una función?** ✅ ❌

### Chat de Copilot

- [ ] Puedo abrir Chat con `Ctrl+Shift+I` (o `Cmd+Shift+I` en Mac)
- [ ] El panel de Chat se abre correctamente
- [ ] Puedo hacer preguntas y recibo respuestas
- [ ] Puedo usar comandos como `/explain`, `/doc`, `/fix`

**Pregunta de prueba:**
```
¿Qué es una función en programación?
```

**¿Recibí una respuesta coherente?** ✅ ❌

### Inline Chat

- [ ] Puedo abrir Inline Chat con `Ctrl+I` (o `Cmd+I` en Mac)
- [ ] Aparece un campo de texto inline en el editor
- [ ] Puedo pedir modificaciones al código seleccionado
- [ ] Los cambios se aplican correctamente

**Prueba de prueba:**
1. Selecciona una función
2. Presiona `Ctrl+I`
3. Escribe: "agrega comentarios"

**¿Funcionó correctamente?** ✅ ❌

---

## ⚙️ Configuración

### Settings Básicos

Verifica en `File > Preferences > Settings` (busca "copilot"):

- [ ] `GitHub Copilot: Enable` está activado
- [ ] `GitHub Copilot: Enable Auto Completions` está activado
- [ ] `Editor: Inline Suggest: Enable` está activado
- [ ] Configurado idioma preferido (opcional)

### Atajos de Teclado

Prueba que funcionan:

| Atajo | Acción | Funciona |
|-------|--------|----------|
| `Tab` | Aceptar sugerencia | ☐ |
| `Esc` | Rechazar sugerencia | ☐ |
| `Alt+]` | Siguiente sugerencia | ☐ |
| `Alt+[` | Anterior sugerencia | ☐ |
| `Ctrl+Shift+I` | Abrir Chat | ☐ |
| `Ctrl+I` | Inline Chat | ☐ |

---

## 🧪 Ejercicio de Verificación Completa

### Parte 1: Autocompletado de Función

Crea `verificacion.js` y escribe:

```javascript
// función para validar si una cadena es un email válido
```

**Expectativa:** Copilot debería sugerir una función completa de validación.

**Resultado:** ✅ Funciona correctamente | ❌ No funciona

---

### Parte 2: Generación de Clase

Escribe:

```javascript
// clase Usuario con propiedades nombre, email y método de validación
```

**Expectativa:** Copilot debería sugerir una clase completa.

**Resultado:** ✅ Funciona correctamente | ❌ No funciona

---

### Parte 3: Chat - Explicación

1. Selecciona el código generado en Parte 1
2. Abre Chat (`Ctrl+Shift+I`)
3. Escribe: `/explain`

**Expectativa:** Deberías recibir una explicación detallada del código.

**Resultado:** ✅ Funciona correctamente | ❌ No funciona

---

### Parte 4: Chat - Documentación

1. Selecciona la clase de Parte 2
2. En Chat, escribe: `/doc`

**Expectativa:** Copilot debería generar documentación JSDoc.

**Resultado:** ✅ Funciona correctamente | ❌ No funciona

---

### Parte 5: Inline Chat - Modificación

1. Selecciona la función de validación (Parte 1)
2. Presiona `Ctrl+I`
3. Escribe: "agrega manejo de errores"

**Expectativa:** El código debería actualizarse con try-catch o validaciones.

**Resultado:** ✅ Funciona correctamente | ❌ No funciona

---

### Parte 6: Live Share (Opcional pero Recomendado)

**Instalación:**

- [ ] Extensión "Live Share" instalada
- [ ] Autenticación completada (Microsoft/GitHub)
- [ ] Ícono de Live Share visible en barra de estado

**Prueba como Anfitrión:**

1. Haz clic en "Live Share" en la barra de estado
2. Selecciona "Start collaboration session"
3. Se copia un enlace al portapapeles

- [ ] Sesión iniciada exitosamente
- [ ] Enlace generado y copiado

**Prueba como Invitado:**

1. Usa el enlace generado (o pide uno a un compañero)
2. Únete a la sesión desde otro VS Code o cuenta

- [ ] Puedo unirme a una sesión
- [ ] Veo el código compartido
- [ ] Puedo ver el cursor del anfitrión

**Prueba de Colaboración:**

Ejercicio en pareja:
1. Anfitrión crea archivo `test-liveshare.js`
2. Escribe: `// función para sumar dos números`
3. Copilot sugiere código
4. Invitado observa la sugerencia en tiempo real
5. Invitado activa "Follow Mode" (click en nombre del anfitrión)

- [ ] Ambos ven las sugerencias de Copilot
- [ ] Follow Mode funciona correctamente
- [ ] Invitado puede editar (si tiene permisos Read/Write)

**Expectativa:** Colaboración fluida con Copilot visible para ambos participantes.

**Resultado:** ✅ Funciona correctamente | ❌ No funciona | ⏭️ Omitido

---

## 🐛 Solución de Problemas

Si algo no funciona, marca el problema:

- [ ] El ícono de Copilot muestra error
  - **Solución:** Cierra sesión y vuelve a autenticar

- [ ] No aparecen sugerencias
  - **Solución:** Verifica configuración "Enable Auto Completions"

- [ ] Las sugerencias son muy lentas
  - **Solución:** Verifica conexión a Internet, reinicia VS Code

- [ ] Chat no responde
  - **Solución:** Verifica que instalaste "GitHub Copilot Chat"

- [ ] Error de autenticación
  - **Solución:** Ve a github.com/settings/copilot y verifica suscripción

- [ ] Live Share no inicia sesión
  - **Solución:** Verifica extensión instalada, cierra sesión y vuelve a iniciar

- [ ] No veo cursor de otros participantes en Live Share
  - **Solución:** Verifica que ambos están en el mismo archivo, desactiva/activa Follow Mode

---

## 📊 Resumen Final

### Puntuación de Verificación

Cuenta cuántos ítems marcaste como ✅:

- **Pre-Instalación:** ___/4
- **Instalación:** ___/7
- **Autocompletado:** ___/5
- **Chat:** ___/4
- **Inline Chat:** ___/4
- **Configuración:** ___/4
- **Atajos:** ___/6
- **Ejercicios:** ___/5
- **Live Share (opcional):** ___/8

**Total Copilot (obligatorio):** ___/39
**Total con Live Share (recomendado):** ___/47

### Interpretación

**Solo Copilot (39 puntos):**
- **35-39 puntos**: ✅ Instalación perfecta, estás listo
- **30-34 puntos**: ⚠️ Funciona bien, pero revisa algunos detalles
- **25-29 puntos**: ⚠️ Funciona básicamente, pero hay problemas menores
- **< 25 puntos**: ❌ Necesitas revisar la instalación, hay problemas

**Con Live Share (47 puntos):**
- **43-47 puntos**: ✅ Instalación completa perfecta, listo para colaboración
- **38-42 puntos**: ⚠️ Muy bien, revisa detalles de Live Share
- **33-37 puntos**: ⚠️ Copilot funciona, Live Share necesita atención
- **< 33 puntos**: ❌ Revisa instalación de ambas herramientas

---

## ✅ Declaración Final

Una vez que hayas completado esta checklist satisfactoriamente:

> **Yo, _________________, confirmo que:**
> - GitHub Copilot está correctamente instalado en mi VS Code
> - He probado y verificado todas las funcionalidades básicas
> - Comprendo cómo usar los comandos y atajos principales
> - *(Opcional)* Live Share está instalado y funcionando para colaboración
> - Estoy listo/a para comenzar con ADOPCION_I
>
> **Fecha:** ___/___/______
> **Firma:** ________________

---

## ➡️ Siguiente Paso

Si completaste esta checklist exitosamente:

👉 **[Comienza con ADOPCION_I](../ADOPCION_I/README.md)**

Si tuviste problemas:

👉 **[Revisa la Guía de Solución de Problemas](./TROUBLESHOOTING.md)**

---

**Nota:** Guarda esta checklist completada como referencia. Si en el futuro tienes problemas con Copilot, puedes volver a revisar esta lista para identificar qué dejó de funcionar.
