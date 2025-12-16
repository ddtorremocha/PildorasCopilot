# Solución de Problemas - GitHub Copilot 🔧

Esta guía te ayudará a resolver los problemas más comunes con GitHub Copilot en Visual Studio Code.

---

## 🔍 Diagnóstico Rápido

### Paso 1: Verificar el Estado de Copilot

1. **Revisa el ícono en la barra de estado** (inferior derecha)
2. **Haz clic en el ícono de Copilot**
3. **Selecciona "Check Copilot Status"**

### Estados Posibles:

| Estado | Significado | Acción |
|--------|-------------|--------|
| ✅ "Copilot is ready" | Todo funciona | Ninguna |
| ⚠️ "Copilot is starting" | Iniciando | Espera unos segundos |
| ❌ "Not signed in" | No autenticado | Inicia sesión |
| ❌ "Network error" | Sin conexión | Revisa Internet |
| ❌ "Disabled for this file" | Deshabilitado | Revisa configuración |

---

## 🚨 Problemas Comunes y Soluciones

### Problema 1: Copilot no aparece / Ícono no visible

**Síntomas:**
- No hay ícono de Copilot en la barra de estado
- La extensión parece no estar instalada

**Soluciones:**

#### Solución A: Verificar instalación
```
1. Ctrl+Shift+X (abrir extensiones)
2. Buscar "GitHub Copilot"
3. Si dice "Install", la extensión no está instalada
4. Si dice "Disable", está instalada pero deshabilitada
5. Asegúrate de que esté "Enabled"
```

#### Solución B: Reinstalar extensión
```
1. Desinstala ambas extensiones:
   - GitHub Copilot
   - GitHub Copilot Chat
2. Reinicia VS Code completamente
3. Reinstala ambas extensiones
4. Reinicia VS Code de nuevo
```

#### Solución C: Revisar workspace
```
Copilot puede estar deshabilitado para el workspace actual:
1. Ctrl+Shift+P
2. "Preferences: Open Workspace Settings"
3. Busca "copilot"
4. Verifica que "GitHub Copilot: Enable" esté activado
```

---

### Problema 2: No recibo sugerencias de código

**Síntomas:**
- El ícono está visible pero no aparece código sugerido
- No hay texto en gris (ghost text)

**Soluciones:**

#### Solución A: Verificar configuración de sugerencias
```json
// Settings.json
{
  "github.copilot.enable": {
    "*": true
  },
  "github.copilot.inlineSuggest.enable": true,
  "editor.inlineSuggest.enabled": true
}
```

#### Solución B: Forzar sugerencia
```
1. Escribe un comentario descriptivo
2. Presiona Alt+\ (forzar sugerencia)
3. Si no funciona, presiona Enter y espera
```

#### Solución C: Verificar tipo de archivo
```
Copilot puede estar deshabilitado para ese tipo de archivo:
1. Verifica la extensión del archivo
2. Algunos archivos de configuración no tienen soporte
3. Intenta con un archivo .js, .py, o .ts
```

#### Solución D: Revisar filtros de lenguaje
```
Settings > GitHub Copilot > Enable

Asegúrate de que tu lenguaje no esté en la lista de exclusiones
```

---

### Problema 3: Error de autenticación

**Síntomas:**
- "Not authorized"
- "Sign in to use GitHub Copilot"
- El ícono tiene una X roja

**Soluciones:**

#### Solución A: Re-autenticar
```
1. Ctrl+Shift+P
2. "GitHub Copilot: Sign Out"
3. Espera confirmación
4. Ctrl+Shift+P
5. "GitHub Copilot: Sign In"
6. Completa el proceso en el navegador
```

#### Solución B: Verificar suscripción
```
1. Ve a: https://github.com/settings/copilot
2. Verifica que tu suscripción esté activa
3. Si no aparece, actívala desde: https://github.com/github-copilot/signup
4. Espera 5 minutos para que se propague
5. Reinicia VS Code
```

#### Solución C: Limpiar caché
```
Windows:
1. Cierra VS Code
2. Ve a: %APPDATA%\Code\User\globalStorage
3. Elimina carpetas que empiecen con "github.copilot"
4. Reinicia VS Code
5. Vuelve a autenticar

Mac:
1. Cierra VS Code
2. Ve a: ~/Library/Application Support/Code/User/globalStorage
3. Elimina carpetas "github.copilot*"
4. Reinicia VS Code

Linux:
1. Cierra VS Code
2. Ve a: ~/.config/Code/User/globalStorage
3. Elimina carpetas "github.copilot*"
4. Reinicia VS Code
```

---

### Problema 4: Chat de Copilot no funciona

**Síntomas:**
- El panel de chat no se abre
- Chat abierto pero no responde
- Error al enviar mensaje

**Soluciones:**

#### Solución A: Verificar extensión de Chat
```
1. Ctrl+Shift+X
2. Busca "GitHub Copilot Chat"
3. Debe estar instalada y habilitada
4. Si no está, instálala
5. Reinicia VS Code
```

#### Solución B: Actualizar extensiones
```
1. Ambas extensiones deben estar actualizadas
2. Ctrl+Shift+X
3. Busca "GitHub Copilot"
4. Si hay botón "Update", actualiza
5. Reinicia VS Code
```

#### Solución C: Limpiar historial de chat
```
1. Ctrl+Shift+P
2. "GitHub Copilot: Clear Chat History"
3. Confirma
4. Intenta usar chat de nuevo
```

#### Solución D: Probar diferentes métodos de chat
```
- Panel de Chat: Ctrl+Shift+I
- Inline Chat: Ctrl+I
- Quick Chat: Ctrl+Shift+Alt+I

Si uno no funciona, prueba otro
```

---

### Problema 5: Sugerencias muy lentas

**Síntomas:**
- Copilot tarda mucho en responder
- Delay notable entre escribir y ver sugerencias

**Soluciones:**

#### Solución A: Verificar conexión
```
1. Prueba tu velocidad de Internet
2. Copilot requiere conexión estable
3. Si estás detrás de proxy, configúralo en VS Code
```

#### Solución B: Desactivar extensiones conflictivas
```
Extensiones que pueden causar conflictos:
- Otras extensiones de IA (Tabnine, Kite, etc.)
- Extensiones de autocompletado agresivas
- Linters muy pesados

Desactívalas temporalmente para probar
```

#### Solución C: Optimizar VS Code
```json
// Settings para mejor rendimiento
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/**": true,
    "**/.hg/store/**": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/*.code-search": true
  }
}
```

#### Solución D: Reducir tamaño de workspace
```
- Cierra carpetas grandes que no uses
- Excluye node_modules y carpetas pesadas
- Trabaja con workspaces específicos
```

---

### Problema 6: Copilot sugiere código en idioma incorrecto

**Síntomas:**
- Comentarios en inglés cuando esperas español
- O viceversa

**Soluciones:**

#### Solución A: Configurar idioma
```json
{
  "github.copilot.chat.localeOverride": "es"
}
```

#### Solución B: Usar comentarios en el idioma deseado
```javascript
// Copilot responde en el idioma de tus comentarios
// Escribe comentarios en español para recibir código en español

// función para calcular el área de un círculo
// ✅ Responderá en español

// function to calculate the area of a circle
// ✅ Responderá en inglés
```

---

### Problema 7: Código sugerido tiene errores

**Síntomas:**
- El código de Copilot no compila
- Hay errores de sintaxis
- Lógica incorrecta

**Soluciones:**

#### Solución A: Revisar y no aceptar ciegamente
```
⚠️ IMPORTANTE: 
Copilot es una herramienta de asistencia, no reemplaza al desarrollador.
SIEMPRE revisa el código antes de aceptarlo.
```

#### Solución B: Mejorar el contexto
```javascript
// ❌ Poco contexto
// validar email

// ✅ Mejor contexto
// función para validar email usando regex RFC 5322
// debe retornar true si es válido, false si no lo es
// debe manejar casos como: usuario@dominio.com, name+tag@dominio.co.uk
```

#### Solución C: Usar Chat para correcciones
```
1. Selecciona el código con error
2. Ctrl+I (Inline Chat)
3. Escribe: "fix the syntax errors"
4. O usa el comando: /fix
```

#### Solución D: Pedir alternativas
```
- Presiona Alt+] para ver otras sugerencias
- A menudo la 2da o 3ra sugerencia es mejor
- No te quedes con la primera opción
```

---

### Problema 8: Copilot deshabilitado para un tipo de archivo

**Síntomas:**
- El ícono muestra "Disabled for this file type"
- No funciona en archivos .txt, .md, etc.

**Soluciones:**

#### Solución A: Habilitar para ese tipo
```json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": true,
    "markdown": true,
    "yaml": true
  }
}
```

#### Solución B: Revisar lista de exclusiones
```
Settings > GitHub Copilot > Enable

Verifica que el tipo de archivo no esté explícitamente excluido
```

---

### Problema 9: Proxy o Firewall corporativo

**Síntomas:**
- "Network error"
- Funciona en casa pero no en la oficina

**Soluciones:**

#### Solución A: Configurar proxy
```json
{
  "http.proxy": "http://proxy.empresa.com:8080",
  "http.proxyStrictSSL": false
}
```

#### Solución B: Certificados corporativos
```
Si tu empresa usa certificados SSL propios:
1. Exporta el certificado corporativo
2. Settings > Http: Proxy Support
3. Configura "http.systemCertificates": true
```

#### Solución C: Whitelist de URLs
```
Solicita a IT que permita acceso a:
- *.github.com
- *.githubusercontent.com
- api.github.com
- copilot-proxy.githubusercontent.com
```

---

### Problema 10: Error después de actualización de VS Code

**Síntomas:**
- Copilot dejó de funcionar después de actualizar VS Code
- Extensiones muestran errores

**Soluciones:**

#### Solución A: Actualizar extensiones
```
1. Ctrl+Shift+X
2. Busca ambas extensiones de Copilot
3. Si hay updates disponibles, actualiza
4. Reinicia VS Code
```

#### Solución B: Downgrade temporal
```
Si la nueva versión tiene bugs:
1. Click derecho en la extensión
2. "Install Another Version"
3. Selecciona versión anterior estable
4. Espera a que salga fix
```

#### Solución C: Reinstalación limpia
```
1. Desinstala extensiones
2. Cierra VS Code
3. Elimina caché (ver Problema 3, Solución C)
4. Reinicia VS Code
5. Reinstala extensiones
```

---

### Problema 11: Live Share no inicia sesión

**Síntomas:**
- No aparece ícono de Live Share en barra de estado
- Error al intentar iniciar sesión colaborativa
- "Extension is not installed" aunque esté instalada

**Soluciones:**

#### Solución A: Verificar instalación de Live Share
```
1. Ctrl+Shift+X (abrir extensiones)
2. Buscar "Live Share"
3. Verifica que esté instalada la extensión de Microsoft
4. Si no está, instala "Live Share" o "Live Share Extension Pack"
5. Reinicia VS Code
```

#### Solución B: Autenticar correctamente
```
1. Haz clic en ícono Live Share (o busca en paleta de comandos)
2. Selecciona "Sign In"
3. Elige entre:
   - Microsoft Account (recomendado para corporativo)
   - GitHub Account
4. Completa autenticación en navegador
5. Confirma en VS Code
```

#### Solución C: Reinstalar Live Share
```
1. Desinstala la extensión Live Share
2. Cierra VS Code completamente
3. Reinicia VS Code
4. Reinstala Live Share
5. Reinicia VS Code de nuevo
```

#### Solución D: Limpiar caché de Live Share
```
Windows:
1. Cierra VS Code
2. Ve a: %USERPROFILE%\.vscode\extensions
3. Busca carpetas que contengan "vsliveshare"
4. Elimínalas
5. Reinstala extensión

Mac/Linux:
1. Cierra VS Code
2. Ve a: ~/.vscode/extensions
3. Elimina carpetas "ms-vsliveshare.*"
4. Reinstala extensión
```

---

### Problema 12: No puedo compartir sesión de Live Share

**Síntomas:**
- Error al hacer clic en "Start Collaboration Session"
- "Unable to start session"
- Enlace no se genera

**Soluciones:**

#### Solución A: Verificar autenticación
```
1. Verifica que has iniciado sesión en Live Share
2. Click en ícono Live Share > "Sign Out"
3. Vuelve a iniciar sesión
4. Intenta compartir de nuevo
```

#### Solución B: Verificar conexión a Internet
```
1. Live Share requiere conexión estable
2. Verifica que no estés detrás de un proxy restrictivo
3. Prueba desactivar VPN temporalmente
4. Verifica firewall corporativo
```

#### Solución C: Configurar proxy (si aplica)
```json
// En settings.json
{
  "liveshare.connectionMode": "relay",
  "http.proxy": "http://proxy.empresa.com:8080",
  "http.proxyStrictSSL": false
}
```

#### Solución D: Cambiar modo de conexión
```json
// Si tienes problemas de red, prueba relay mode
{
  "liveshare.connectionMode": "relay"
}

// Por defecto es "auto", otras opciones: "direct"
```

---

### Problema 13: Invitado no puede editar en Live Share

**Síntomas:**
- El invitado puede ver código pero no editarlo
- Cursor del invitado no aparece
- "Read-only mode" activo sin quererlo

**Soluciones:**

#### Solución A: Verificar permisos
```
Como anfitrión:
1. Click en ícono Live Share
2. Verás lista de participantes
3. Click en nombre del participante
4. Selecciona "Change Role to Read/Write"
5. O al inicio, selecciona "Share (Read/Write)"
```

#### Solución B: Reiniciar sesión con permisos correctos
```
1. Anfitrión: Detener sesión actual
2. Iniciar nueva sesión
3. Al compartir, selecciona explícitamente "Read/Write"
4. Comparte nuevo enlace
```

#### Solución C: Verificar configuración de workspace
```json
{
  "liveshare.guestApprovalRequired": false,
  "liveshare.anonymousGuestApproval": "accept"
}
```

---

### Problema 14: No veo cursor de otros participantes en Live Share

**Síntomas:**
- Estoy en sesión de Live Share pero no veo cursores
- No sé dónde están los otros participantes
- "Follow Mode" no funciona

**Soluciones:**

#### Solución A: Verificar que están en el mismo archivo
```
1. Ambos participantes deben abrir el mismo archivo
2. Usa Follow Mode para sincronizar:
   - Click en nombre del participante
   - Se activará "Following [nombre]"
3. Tu vista se sincronizará con el anfitrión
```

#### Solución B: Actualizar extensiones
```
1. Ambos participantes deben tener Live Share actualizado
2. Versiones incompatibles pueden causar problemas
3. Ctrl+Shift+X > Busca "Live Share"
4. Actualiza si hay nueva versión
5. Reinicia VS Code
```

#### Solución C: Verificar configuración de presencia
```json
{
  "liveshare.presence": true,
  "liveshare.focusBehavior": "prompt"
}
```

#### Solución D: Reiniciar sesión completamente
```
1. Anfitrión: Detener sesión
2. Ambos: Cerrar VS Code
3. Ambos: Reabrir VS Code
4. Anfitrión: Iniciar nueva sesión
5. Invitado: Unirse con nuevo enlace
```

---

### Problema 15: Live Share con lag o muy lento

**Síntomas:**
- Delay notable en ver cambios de otros
- Escritura se congela
- Desconexiones frecuentes

**Soluciones:**

#### Solución A: Verificar conexión de ambos
```
1. Ambos participantes necesitan conexión estable
2. Prueba velocidad de Internet
3. Cierra aplicaciones pesadas
4. Desactiva descargas/uploads grandes
```

#### Solución B: Reducir tamaño de workspace
```
1. No compartas proyectos enormes
2. Cierra carpetas innecesarias
3. Excluye node_modules, build, etc.
```

#### Solución C: Cambiar modo de conexión
```json
{
  "liveshare.connectionMode": "direct"
}
// Direct mode es más rápido pero requiere mejor red
// Si no funciona, vuelve a "relay" o "auto"
```

#### Solución D: Limitar participantes
```
- Máximo recomendado: 5-6 participantes
- Más participantes = más lag
- Para demos grandes, usa Read-Only mode
```

#### Solución E: Desactivar compartición innecesaria
```json
{
  "liveshare.autoShareServers": false,
  "liveshare.autoShareTerminals": false
}
```

---

### Problema 16: Copilot no funciona para invitados en Live Share

**Síntomas:**
- Anfitrión ve sugerencias de Copilot
- Invitados no ven sugerencias
- "Copilot not available" para invitados

**Soluciones:**

#### Solución A: Cada usuario necesita Copilot
```
⚠️ IMPORTANTE:
- Live Share NO comparte la suscripción de Copilot
- Cada participante necesita su propia suscripción activa
- Verifica que todos tengan Copilot instalado y autenticado
```

#### Solución B: Verificar autenticación individual
```
Cada participante debe:
1. Tener GitHub Copilot instalado
2. Estar autenticado con su propia cuenta
3. Tener suscripción activa de Copilot
4. Ver el ícono de Copilot en su barra de estado
```

#### Solución C: Modo de trabajo alternativo
```
Si solo el anfitrión tiene Copilot:
1. Anfitrión usa Copilot normalmente
2. Invitados ven las sugerencias en tiempo real
3. Discuten y aprueban sugerencias
4. Anfitrión acepta/rechaza según consenso
```

---

## 🔍 Comandos de Diagnóstico

### Ver Logs de Copilot

```
1. Ctrl+Shift+P
2. "GitHub Copilot: View Logs"
3. Revisa errores en rojo
4. Copia el error para buscar solución
```

### Ver Output de Copilot

```
1. View > Output (Ctrl+Shift+U)
2. En el dropdown selecciona "GitHub Copilot"
3. Revisa mensajes de error o advertencias
```

### Comando de Estado

```
1. Ctrl+Shift+P
2. "GitHub Copilot: Check Status"
3. Muestra información detallada del estado
```

---

## 📞 Contactar Soporte

Si ninguna solución funciona:

### 1. Recopila información

```
- Versión de VS Code (Help > About)
- Versión de extensiones Copilot
- Sistema operativo
- Logs de error (Output panel)
- Pasos para reproducir el problema
```

### 2. Reporta el problema

- **GitHub Issues**: https://github.com/github/copilot-docs/issues
- **GitHub Support**: https://support.github.com/
- **Community Forum**: https://github.com/orgs/community/discussions/categories/copilot

### 3. Template de reporte

```markdown
**Descripción del problema:**
[Describe qué no funciona]

**Pasos para reproducir:**
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

**Comportamiento esperado:**
[Qué debería pasar]

**Comportamiento actual:**
[Qué está pasando]

**Entorno:**
- VS Code version: [X.XX.X]
- Copilot version: [X.XX.X]
- OS: [Windows/Mac/Linux]

**Logs:**
[Pega logs relevantes aquí]
```

---

## ✅ Checklist de Solución de Problemas

### Copilot

Antes de contactar soporte, verifica que hayas intentado:

- [ ] Reiniciar VS Code
- [ ] Cerrar sesión y volver a autenticar
- [ ] Verificar suscripción de Copilot activa
- [ ] Actualizar extensiones a última versión
- [ ] Verificar configuración de enable/disable
- [ ] Limpiar caché de Copilot
- [ ] Probar con archivo nuevo de prueba
- [ ] Revisar logs y output
- [ ] Desactivar otras extensiones temporalmente
- [ ] Verificar conexión a Internet

### Live Share (si aplica)

- [ ] Verificar extensión Live Share instalada
- [ ] Autenticación completada (Microsoft/GitHub)
- [ ] Reiniciar VS Code después de instalar
- [ ] Verificar permisos de sesión (Read-Only vs Read/Write)
- [ ] Probar con proyecto más pequeño
- [ ] Verificar que todos tengan versiones actualizadas
- [ ] Revisar configuración de connectionMode
- [ ] Verificar que cada usuario tenga su propia suscripción de Copilot
- [ ] Comprobar firewall/proxy corporativo
- [ ] Probar en red diferente

---

## 🎯 Prevención de Problemas

### Mejores Prácticas:

1. **Mantén actualizado:**
   - VS Code
   - Extensiones de Copilot y Live Share
   - Sistema operativo

2. **Revisa configuración regularmente:**
   - Settings de Copilot
   - Settings de Live Share (permisos, connectionMode)
   - Exclusiones de archivos
   - Configuración de proxy (si aplica)

3. **Monitorea el estado:**
   - Revisa el ícono de Copilot periódicamente
   - Verifica suscripción mensualmente
   - Lee release notes de actualizaciones
   - Prueba Live Share antes de sesiones importantes

4. **Backup de configuración:**
   - Exporta tus settings.json
   - Documenta configuraciones personalizadas
   - Guarda tu configuración de atajos

5. **Seguridad en Live Share:**
   - No compartas datos sensibles (API keys, contraseñas)
   - Cierra sesiones cuando termines
   - Usa Read-Only para demos públicas
   - Verifica identidad de participantes

---

**Última actualización:** Diciembre 2025  
**Versión:** 1.1

---

➡️ **[Volver a ADOPCION_0](./README.md)** | **[Ir a ADOPCION_I](../ADOPCION_I/README.md)**
