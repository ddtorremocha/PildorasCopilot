<p align="center"> <img src="../resources/logo.png" alt="GenAI H&PS" style="width: 80px; height: 80px;"/></p>


# ADOPCION_0: Instalación y Configuración de GitHub Copilot 🚀

## 📋 Descripción

Esta fase inicial te guiará a través del proceso completo de **instalación, configuración y verificación** de GitHub Copilot en Visual Studio Code. Es fundamental completar esta fase antes de comenzar con las píldoras de adopción.

---

## 🎯 Objetivos

Al finalizar esta fase, habrás:

1. ✅ Instalado GitHub Copilot en VS Code
2. ✅ Configurado tu cuenta de GitHub
3. ✅ Verificado que Copilot funciona correctamente
4. ✅ Personalizado las configuraciones según tus preferencias
5. ✅ Conocido los comandos básicos y atajos de teclado

**Tiempo estimado: 15-20 minutos**

---

## 📋 Requisitos Previos

### 1. Cuenta Corporativa de GitHub de Accenture
- Necesitas una cuenta de GitHub activa gestionada con Accenture

### 2. Visual Studio Code
- Versión mínima recomendada: 1.85 o superior
- Descarga desde: https://code.visualstudio.com/

### 3. Conexión a Internet
- Necesaria para autenticación y funcionamiento de Copilot

---

## 📥 Paso 1: Instalación de GitHub Copilot

### Opción A: Desde VS Code (Recomendado)

1. **Abre Visual Studio Code**

2. **Accede a las Extensiones**
   - Haz clic en el ícono de extensiones en la barra lateral (o presiona `Ctrl+Shift+X`)

3. **Busca "GitHub Copilot"**
   - Escribe "GitHub Copilot" en la barra de búsqueda
   - Verás dos extensiones principales:
     - **GitHub Copilot**: La extensión principal (obligatoria)
     - **GitHub Copilot Chat**: Para conversaciones con Copilot (recomendada)

4. **Instala ambas extensiones**
   - Haz clic en "Install" en ambas
   - Espera a que se completen las instalaciones

### Opción B: Desde el Marketplace

1. Visita: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot
2. Haz clic en "Install"
3. Permite que se abra en VS Code
4. Repite para GitHub Copilot Chat

---

## 🔐 Paso 2: Autenticación

### Proceso de Autenticación

1. **Notificación de Inicio de Sesión**
   - Después de instalar, verás una notificación para iniciar sesión
   - Haz clic en "Sign in to GitHub"

2. **Autorización en el Navegador**
   - Se abrirá tu navegador web
   - Inicia sesión en GitHub si no lo has hecho
   - Autoriza GitHub Copilot para acceder a tu cuenta

3. **Confirmar en VS Code**
   - VS Code detectará automáticamente la autenticación
   - Verás una confirmación de que estás conectado

### ⚠️ Solución de Problemas de Autenticación

**Si no se abre el navegador:**
1. Abre la Paleta de Comandos (`Ctrl+Shift+P`)
2. Escribe "GitHub Copilot: Sign In"
3. Sigue el proceso manualmente

**Si ya iniciaste sesión pero no funciona:**
1. Cierra VS Code completamente
2. Abre VS Code de nuevo
3. Verifica el estado en la barra inferior

---

## ✅ Paso 3: Verificación de Instalación

### Verificar que Copilot está Activo

1. **Revisa la Barra de Estado**
   - En la parte inferior derecha de VS Code
   - Deberías ver el ícono de GitHub Copilot ![Copilot Icon]
   - El ícono NO debe tener una X o una señal de prohibido

2. **Prueba Básica de Autocompletado**
   - Crea un archivo nuevo (ej: `test.js`)
   - Escribe un comentario:
     ```javascript
     // función para calcular el área de un círculo
     ```
   - Presiona Enter
   - Copilot debería sugerir código automáticamente en gris

3. **Prueba de Copilot Chat**
   - Abre Copilot Chat: `Ctrl+Shift+I` (Windows/Linux) o `Cmd+Shift+I` (Mac)
   - Escribe una pregunta simple: "¿Qué es JavaScript?"
   - Deberías recibir una respuesta

### Estados del Ícono de Copilot

| Ícono | Estado | Significado |
|-------|--------|-------------|
| ![Copilot Normal] | Normal | Funcionando correctamente |
| ![Copilot Warning] | Advertencia | Problema menor, puede seguir funcionando |
| ![Copilot Error] | Error | No está funcionando, revisa autenticación |
| ![Copilot Disabled] | Deshabilitado | Copilot está desactivado para este archivo/lenguaje |

---

## ⚙️ Paso 4: Configuración Básica

### Acceder a la Configuración

1. **Abrir Configuración**
   - Menú: `File > Preferences > Settings` (o `Ctrl+,`)
   - Busca "Copilot" en la barra de búsqueda

2. **Configuraciones Esenciales**

#### GitHub Copilot: Enable
```
✅ Activado por defecto
```
Habilita/deshabilita Copilot globalmente.

#### GitHub Copilot: Enable Auto Completions
```
✅ Recomendado: Activado
```
Muestra sugerencias automáticamente mientras escribes.

#### GitHub Copilot: Inline Suggest: Enable
```
✅ Recomendado: Activado
```
Muestra sugerencias inline (en gris) en el editor.

---

## 🎨 Paso 5: Configuraciones Avanzadas (Opcional)

### Configuraciones Recomendadas

Abre `settings.json` (`Ctrl+Shift+P` > "Preferences: Open Settings (JSON)") y agrega:

```json
{
  // GitHub Copilot - Configuraciones básicas
  "github.copilot.enable": {
    "*": true,
    "yaml": true,
    "plaintext": false,
    "markdown": true
  },
  
  // Sugerencias inline
  "github.copilot.inlineSuggest.enable": true,
  
  // Editor - Mejoras para trabajar con Copilot
  "editor.inlineSuggest.enabled": true,
  "editor.quickSuggestions": {
    "comments": "on",
    "strings": "on",
    "other": "on"
  },
  
  // Chat
  "github.copilot.chat.localeOverride": "es",
  
  // Copilot para lenguajes específicos
  "github.copilot.advanced": {
    "debug.overrideEngine": "gpt-4",
    "debug.testOverrideProxyUrl": "",
    "debug.overrideProxyUrl": ""
  }
}
```

### Configuraciones por Lenguaje

Si quieres desactivar Copilot para lenguajes específicos:

```json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": false,
    "scminput": false
  }
}
```

---

## ⌨️ Paso 6: Atajos de Teclado Esenciales

### Autocompletado

| Acción | Windows/Linux | Mac | Descripción |
|--------|---------------|-----|-------------|
| **Aceptar sugerencia** | `Tab` | `Tab` | Acepta la sugerencia completa |
| **Rechazar sugerencia** | `Esc` | `Esc` | Cierra la sugerencia |
| **Siguiente sugerencia** | `Alt+]` | `Option+]` | Muestra siguiente alternativa |
| **Anterior sugerencia** | `Alt+[` | `Option+[` | Muestra anterior alternativa |
| **Activar sugerencias** | `Alt+\` | `Option+\` | Fuerza una sugerencia |

### Copilot Chat

| Acción | Windows/Linux | Mac | Descripción |
|--------|---------------|-----|-------------|
| **Abrir Chat** | `Ctrl+Shift+I` | `Cmd+Shift+I` | Abre panel de chat |
| **Inline Chat** | `Ctrl+I` | `Cmd+I` | Chat en el editor |
| **Quick Chat** | `Ctrl+Shift+Alt+I` | `Cmd+Shift+Option+I` | Chat rápido flotante |

### Comandos Útiles

En Copilot Chat, puedes usar comandos especiales:

| Comando | Descripción |
|---------|-------------|
| `/explain` | Explica el código seleccionado |
| `/fix` | Sugiere correcciones para errores |
| `/doc` | Genera documentación |
| `/tests` | Genera tests unitarios |
| `/help` | Muestra ayuda de comandos |

---

## 🧪 Paso 7: Prueba Completa

### Ejercicio de Verificación

Vamos a verificar que todo funciona correctamente:

1. **Crea un archivo `test-copilot.js`**

2. **Prueba 1: Autocompletado de Función**
   ```javascript
   // Escribe este comentario y presiona Enter:
   // función para validar un email
   ```
   ✅ Copilot debería sugerir una función completa

3. **Prueba 2: Completado de Código**
   ```javascript
   // Escribe solo esta línea y espera sugerencias:
   function fibonacci(n) {
   ```
   ✅ Copilot debería completar la implementación

4. **Prueba 3: Copilot Chat**
   - Selecciona el código generado
   - Abre Chat (`Ctrl+Shift+I`)
   - Escribe: `/explain`
   ✅ Deberías recibir una explicación detallada

5. **Prueba 4: Inline Chat**
   - Selecciona una función
   - Presiona `Ctrl+I`
   - Escribe: "agrega validación de parámetros"
   ✅ Copilot debería modificar el código

---

## � Paso 8: Instalación y Uso de Live Share (Opcional)

### ¿Qué es Live Share?

**Live Share** es una extensión de Visual Studio Code que permite:
- ✅ Colaborar en tiempo real con otros desarrolladores
- ✅ Compartir tu sesión de VS Code (código, terminal, servidor, debugger)
- ✅ Trabajar en pair programming remoto
- ✅ Combinar con Copilot para sesiones de formación y mentoring

**Casos de uso con Copilot:**
- Demostrar capacidades de Copilot a tu equipo
- Sesiones de pair programming con IA
- Formación y onboarding remoto
- Code reviews en tiempo real con asistencia de Copilot

---

### Instalación de Live Share

#### Opción A: Desde VS Code (Recomendado)

1. **Abre el panel de Extensiones**
   - Presiona `Ctrl+Shift+X` (Windows/Linux) o `Cmd+Shift+X` (Mac)

2. **Busca "Live Share"**
   - Escribe "Live Share" en la barra de búsqueda
   - Busca la extensión oficial de Microsoft

3. **Instala la extensión**
   - Extensión principal: **Live Share** (Microsoft)
   - Haz clic en "Install"
   - Espera a que complete la instalación

4. **Extensiones complementarias (opcionales pero recomendadas)**
   - **Live Share Audio**: Para llamadas de voz integradas
   - **Live Share Whiteboard**: Para diagramas colaborativos

#### Opción B: Extension Pack

Instala **Live Share Extension Pack** que incluye todo:
- Live Share
- Live Share Audio
- Live Share Whiteboard

---

### Configuración Inicial de Live Share

1. **Primera vez que uses Live Share**
   - Haz clic en el ícono "Live Share" en la barra de estado (inferior)
   - O presiona `Ctrl+Shift+P` y escribe "Live Share: Sign In"

2. **Autenticación**
   - Puedes autenticarte con:
     - ✅ **Cuenta de Microsoft** (recomendado para entorno corporativo)
     - ✅ **Cuenta de GitHub** (si ya estás autenticado con Copilot)
   
3. **Permisos**
   - Acepta los permisos necesarios en el navegador
   - VS Code confirmará la autenticación exitosa

---

### Cómo Usar Live Share

#### Como Anfitrión (Host) - Compartir tu sesión

1. **Iniciar sesión de Live Share**
   ```
   Método 1: Clic en ícono "Live Share" en barra de estado
   Método 2: Ctrl+Shift+P > "Live Share: Start Collaboration Session"
   Método 3: Clic derecho en explorador > "Start Collaboration Session"
   ```

2. **Configurar permisos**
   - **Read-Only**: Los invitados solo pueden ver (demo/presentación)
   - **Read/Write**: Los invitados pueden editar (pair programming)
   
3. **Compartir el enlace**
   - Se copia automáticamente al portapapeles
   - Ejemplo: `https://prod.liveshare.vsengsaas.visualstudio.com/join?ABC123`
   - Comparte este enlace con tus colaboradores (email, Teams, Slack)

4. **Gestionar participantes**
   - Panel de Live Share (barra lateral)
   - Ver quién está conectado
   - Cambiar permisos individuales
   - Expulsar participantes si es necesario

5. **Compartir recursos adicionales**
   - **Terminal**: Clic derecho en terminal > "Share Terminal"
   - **Servidor local**: Live Share detecta automáticamente y pregunta si compartir
   - **Debugging**: Se comparte automáticamente si está activo

#### Como Invitado (Guest) - Unirse a una sesión

1. **Unirse con el enlace**
   ```
   Método 1: Clic en el enlace recibido (se abre en VS Code)
   Método 2: Ctrl+Shift+P > "Live Share: Join Collaboration Session"
   Método 3: Pegar enlace en navegador
   ```

2. **Autenticación**
   - Si es tu primera vez, necesitarás autenticarte
   - Usa la misma cuenta (Microsoft/GitHub)

3. **Navegar en la sesión**
   - Verás el código del anfitrión
   - Tu cursor se muestra con tu nombre/color
   - Puedes navegar independientemente o seguir al anfitrión

4. **Seguir al anfitrión**
   - Haz clic en el nombre del anfitrión en el panel de Live Share
   - Se activará "Follow Mode" (sígueme)
   - Tu vista se sincronizará con la del anfitrión



## �🔧 Solución de Problemas Comunes

### Problema 1: Copilot no sugiere nada

**Posibles causas:**
- No estás autenticado correctamente
- Copilot está deshabilitado para ese tipo de archivo
- Problema de conexión a internet

**Soluciones:**
1. Verifica el ícono en la barra de estado
2. Haz clic en el ícono y selecciona "Check Status"
3. Reinicia VS Code
4. Cierra sesión y vuelve a iniciar (`Ctrl+Shift+P` > "GitHub Copilot: Sign Out")

### Problema 2: Las sugerencias son lentas

**Soluciones:**
1. Verifica tu conexión a internet
2. Cierra otros programas pesados
3. Actualiza VS Code a la última versión
4. Desactiva temporalmente otras extensiones que puedan interferir

### Problema 3: Error de autenticación

**Soluciones:**
1. Verifica que tu suscripción de Copilot está activa en GitHub
2. Cierra sesión completamente y vuelve a iniciar
3. Revisa en GitHub Settings > Copilot que tienes acceso
4. Borra el caché de VS Code:
   - Cierra VS Code
   - Elimina: `%APPDATA%\Code\User\globalStorage\github.copilot*`
   - Reinicia VS Code

### Problema 4: Chat de Copilot no responde

**Soluciones:**
1. Verifica que instalaste la extensión "GitHub Copilot Chat"
2. Actualiza ambas extensiones a la última versión
3. Reinicia VS Code

---

## 📊 Verificación Final

### Checklist de Instalación Completa

Marca cada elemento cuando lo hayas completado:

- [ ] Visual Studio Code instalado (versión 1.85+)
- [ ] Extensión GitHub Copilot instalada
- [ ] Extensión GitHub Copilot Chat instalada
- [ ] Autenticación completada exitosamente
- [ ] Ícono de Copilot visible en barra de estado (sin errores)
- [ ] Autocompletado funcionando (prueba realizada)
- [ ] Chat de Copilot funcionando (prueba realizada)
- [ ] Atajos de teclado probados
- [ ] Configuraciones personalizadas (opcional)
- [ ] Ejercicio de verificación completado
- [ ] Live Share instalado y probado (opcional pero recomendado)

---

## 🎓 Mejores Prácticas de Uso

### Consejos para Empezar

1. **Escribe comentarios claros**
   - Copilot funciona mejor con comentarios descriptivos
   - Usa lenguaje natural en tus comentarios

2. **Sé específico**
   - "función para validar email con regex" es mejor que "validar email"

3. **Revisa las sugerencias**
   - No aceptes código sin entenderlo
   - Copilot es una herramienta, tú sigues siendo el desarrollador

4. **Usa múltiples sugerencias**
   - Presiona `Alt+]` para ver alternativas
   - A veces la segunda o tercera sugerencia es mejor

5. **Combina con Chat**
   - Usa autocompletado para código rápido
   - Usa Chat para explicaciones y diseño

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [VS Code Copilot Guide](https://code.visualstudio.com/docs/editor/artificial-intelligence)

### Videos Tutoriales
- [GitHub Copilot Getting Started](https://www.youtube.com/watch?v=gdZLi9oWNZg)
- [Trucos y Tips de Copilot](https://www.youtube.com/@GitHub)

### Comunidad
- [GitHub Copilot Discussions](https://github.com/orgs/community/discussions/categories/copilot)
- [VS Code Community](https://github.com/microsoft/vscode/discussions)

---

## ➡️ Próximos Pasos

Una vez completada esta fase de instalación, estás listo para comenzar con las píldoras de adopción:

👉 **[ADOPCION_I: Fundamentos de GitHub Copilot](../ADOPCION_I/README.md)**

En ADOPCION_I comenzarás con:
- Píldora 1: Autocompletado de código
- Píldora 2: Documentación automática
- Píldora 3: Traducción entre lenguajes
- Y más...

---

## 🆘 ¿Necesitas Ayuda?

Si después de seguir esta guía sigues teniendo problemas:

1. **Revisa el estado en GitHub**
   - Ve a: https://github.com/settings/copilot
   - Verifica que tu suscripción está activa

2. **Logs de Copilot**
   - `Ctrl+Shift+P` > "GitHub Copilot: View Logs"
   - Busca mensajes de error

3. **Soporte Oficial**
   - [GitHub Support](https://support.github.com/)
   - [Report an Issue](https://github.com/github/copilot-docs/issues)

---

**¡Felicidades!** 🎉 Ahora tienes GitHub Copilot completamente configurado y listo para usar.

**Última actualización**: Diciembre 2025  
**Versión**: 1.0
