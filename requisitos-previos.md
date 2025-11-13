# 📋 Requisitos Previos - Píldoras Formativas GitHub Copilot

Este documento detalla todos los requisitos necesarios para aprovechar al máximo las píldoras formativas de GitHub Copilot.

---

## 🖥️ Software y Herramientas Requeridas

### ✅ Obligatorios

#### 1. Visual Studio Code
- **Versión mínima:** 1.85 o superior
- **Recomendado:** Última versión estable
- **Descarga:** [code.visualstudio.com](https://code.visualstudio.com/)

#### 2. GitHub Copilot
- **Licencia activa** (Individual, Business o Enterprise)
- **Extensión VS Code:** GitHub Copilot
- **Extensión VS Code:** GitHub Copilot Chat
- **Cómo obtenerlo:** [github.com/features/copilot](https://github.com/features/copilot)

**Verificar instalación:**
```bash
# En VS Code, presiona Ctrl+Shift+P y busca:
# "GitHub Copilot: Check Status"
```

#### 3. Git
- **Versión mínima:** 2.30 o superior
- **Descarga:** [git-scm.com](https://git-scm.com/)

**Verificar instalación:**
```powershell
git --version
```

---

## 🔧 Configuración de VS Code

### Extensiones Recomendadas

#### Obligatorias:
- ✅ **GitHub Copilot** (GitHub.copilot)
- ✅ **GitHub Copilot Chat** (GitHub.copilot-chat)

#### Altamente Recomendadas:
- 🔹 **Python** (ms-python.python) - Para píldoras de Python
- 🔹 **ESLint** (dbaeumer.vscode-eslint) - Para píldoras de JavaScript
- 🔹 **Prettier** (esbenp.prettier-vscode) - Formateo de código
- 🔹 **Thunder Client** o **REST Client** - Para píldoras de APIs

#### Opcionales pero Útiles:
- 📦 **GitLens** (eamodio.gitlens) - Mejor integración con Git
- 📦 **Error Lens** (usernamehw.errorlens) - Ver errores inline
- 📦 **Better Comments** (aaron-bond.better-comments) - Comentarios destacados

**Instalar extensiones:**
```
Ctrl+Shift+X → Buscar → Instalar
```

### Configuración Recomendada de VS Code

Agrega esto a tu `settings.json` (Ctrl+Shift+P → "Preferences: Open Settings (JSON)"):

```json
{
    // GitHub Copilot
    "github.copilot.enable": {
        "*": true,
        "yaml": true,
        "plaintext": false,
        "markdown": false
    },
    "github.copilot.editor.enableAutoCompletions": true,
    
    // Editor
    "editor.inlineSuggest.enabled": true,
    "editor.suggestSelection": "first",
    "editor.tabSize": 4,
    "editor.formatOnSave": true,
    
    // Terminal
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    
    // Formateo
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true
    }
}
```

---

## 💻 Entornos de Desarrollo por Lenguaje

### Para Python (Píldoras 1, 2, 4, 5, 6, 7, 9, 10, 13, 14, 16)

#### Python Runtime
- **Versión mínima:** Python 3.8
- **Recomendado:** Python 3.11 o superior
- **Descarga:** [python.org](https://www.python.org/downloads/)

**Verificar instalación:**
```powershell
python --version
# o
python3 --version
```

#### Paquetes Python Esenciales
```powershell
# Actualizar pip
python -m pip install --upgrade pip

# Herramientas básicas
pip install pytest pytest-cov black flake8 mypy

# Para píldoras específicas (opcional)
pip install pandas numpy requests flask fastapi sqlalchemy
```

#### Entorno Virtual (Recomendado)
```powershell
# Crear entorno virtual
python -m venv venv

# Activar (Windows)
.\venv\Scripts\activate

# Activar (Linux/Mac)
source venv/bin/activate
```

---

### Para JavaScript/TypeScript (Píldoras 1, 3, 4, 8, 11, 12, 14)

#### Node.js y npm
- **Versión mínima:** Node.js 16.x
- **Recomendado:** Node.js 18.x LTS o superior
- **Descarga:** [nodejs.org](https://nodejs.org/)

**Verificar instalación:**
```powershell
node --version
npm --version
```

#### Paquetes npm Globales Útiles
```powershell
# Herramientas de desarrollo
npm install -g typescript ts-node nodemon

# Linters y formatters
npm install -g eslint prettier

# Testing
npm install -g jest
```

#### Inicializar Proyecto Node.js
```powershell
# Crear package.json
npm init -y

# Instalar dependencias comunes
npm install express dotenv
npm install -D jest @types/node @types/jest eslint prettier
```

---

### Para Java (Píldora 3, 8)

#### JDK (Java Development Kit)
- **Versión mínima:** JDK 11
- **Recomendado:** JDK 17 LTS o JDK 21
- **Descarga:** [oracle.com/java](https://www.oracle.com/java/technologies/downloads/) o [OpenJDK](https://openjdk.org/)

**Verificar instalación:**
```powershell
java -version
javac -version
```

#### Extensiones VS Code para Java
- Extension Pack for Java (vscjava.vscode-java-pack)

---

### Para C# (Píldora 3)

#### .NET SDK
- **Versión mínima:** .NET 6
- **Recomendado:** .NET 8
- **Descarga:** [dotnet.microsoft.com](https://dotnet.microsoft.com/download)

**Verificar instalación:**
```powershell
dotnet --version
```

#### Extensiones VS Code para C#
- C# (ms-dotnettools.csharp)
- C# Dev Kit (ms-dotnettools.csdevkit)

---

## 🗄️ Bases de Datos (Píldoras 9, 13)

### SQLite (Recomendado para comenzar)
- Ya incluido en Python
- No requiere instalación adicional

### PostgreSQL (Opcional)
- **Descarga:** [postgresql.org](https://www.postgresql.org/download/)
- **Cliente:** DBeaver, pgAdmin, o extensión de VS Code

### MySQL (Opcional)
- **Descarga:** [mysql.com](https://dev.mysql.com/downloads/)

### Extensión VS Code para SQL
- SQLTools (mtxr.sqltools)
- SQLite Viewer (alexcvzz.vscode-sqlite)

---

## 🌐 Para Píldoras de APIs y Testing

### Testing E2E (Píldora 14)

#### Playwright
```powershell
npm install -D @playwright/test
npx playwright install
```

#### Selenium (Alternativa)
```powershell
pip install selenium webdriver-manager
```

### Clientes HTTP

#### Thunder Client (VS Code Extension)
- Recomendado para probar APIs REST
- No requiere instalación adicional

#### Postman (Alternativa)
- **Descarga:** [postman.com](https://www.postman.com/downloads/)

---

## 📚 Conocimientos Previos Recomendados

### 🟢 Para ADOPCIÓN I (Nivel Básico)

**Conocimientos mínimos:**
- ✅ Programación básica en al menos un lenguaje
- ✅ Uso básico de VS Code
- ✅ Conceptos de funciones y variables
- ✅ Lectura de código simple

**NO requieres:**
- ❌ Experiencia con IA generativa
- ❌ Conocimientos avanzados de programación
- ❌ Múltiples lenguajes de programación

**Tiempo de experiencia:** 3-6 meses programando

---

### 🟡 Para ADOPCIÓN II (Nivel Intermedio)

**Conocimientos recomendados:**
- ✅ ADOPCIÓN I completada
- ✅ Experiencia con frameworks web (Express, Flask, etc.)
- ✅ Conocimientos de testing básico
- ✅ APIs REST (conceptos básicos)
- ✅ SQL básico
- ✅ Git y control de versiones

**Tiempo de experiencia:** 1-2 años programando

---

### 🔴 Para ADOPCIÓN III (Nivel Avanzado)

**Conocimientos requeridos:**
- ✅ ADOPCIÓN I y II completadas
- ✅ Arquitectura de software
- ✅ Patrones de diseño
- ✅ Testing avanzado (E2E, integración)
- ✅ Optimización de rendimiento
- ✅ Trabajo en equipo y code reviews

**Tiempo de experiencia:** 3+ años programando

---

## 🎓 Recursos de Preparación

### Si no cumples todos los requisitos:

#### Aprender Programación Básica
- [freeCodeCamp](https://www.freecodecamp.org/)
- [Codecademy](https://www.codecademy.com/)
- [W3Schools](https://www.w3schools.com/)

#### Aprender VS Code
- [VS Code Docs](https://code.visualstudio.com/docs)
- [VS Code Tips](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

#### Aprender Git
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Learn Git Branching](https://learngitbranching.js.org/)

---

## ✅ Checklist de Verificación

Antes de comenzar las píldoras, verifica:

### Software Base
- [ ] VS Code instalado y actualizado
- [ ] GitHub Copilot con licencia activa
- [ ] Git instalado y configurado
- [ ] Terminal funcionando correctamente

### Lenguajes (según tus píldoras de interés)
- [ ] Python 3.8+ instalado
- [ ] Node.js 16+ instalado
- [ ] Java JDK 11+ instalado (si aplica)
- [ ] .NET SDK instalado (si aplica)

### Configuración VS Code
- [ ] Extensiones obligatorias instaladas
- [ ] Copilot activado y funcionando
- [ ] Settings.json configurado
- [ ] Terminal integrada funcional

### Conocimientos
- [ ] Nivel de programación adecuado para el nivel elegido
- [ ] Familiaridad con VS Code
- [ ] Conceptos básicos de tu lenguaje principal

---

## 🆘 Solución de Problemas Comunes

### Copilot no sugiere código
```
1. Verificar licencia: Ctrl+Shift+P → "Copilot: Check Status"
2. Recargar VS Code: Ctrl+Shift+P → "Reload Window"
3. Re-autenticar: Ctrl+Shift+P → "Copilot: Sign Out" → "Sign In"
```

### Python no se encuentra
```powershell
# Windows: Agregar a PATH en Variables de Entorno
# Verificar:
where python
# o
python --version
```

### npm no funciona
```powershell
# Reinstalar Node.js con opción "Add to PATH"
# Verificar:
where npm
npm --version
```

### Extensiones no cargan
```
1. Ctrl+Shift+P → "Developer: Reload Window"
2. Si persiste: Desinstalar y reinstalar extensión
```

---

## 📞 Soporte y Ayuda

### Documentación Oficial
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [VS Code Docs](https://code.visualstudio.com/docs)

### Comunidad
- [GitHub Community](https://github.com/community)
- [VS Code Community](https://code.visualstudio.com/community)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/github-copilot)

---

## 🎯 Recomendaciones Finales

### Antes de Empezar

1. **Dedica 30 minutos** a configurar tu entorno correctamente
2. **Verifica cada requisito** de la checklist
3. **Prueba Copilot** con un archivo simple para confirmar que funciona
4. **Ten paciencia** - La primera configuración puede tomar tiempo

### Durante las Píldoras

1. **Usa un proyecto de prueba** - No tu proyecto productivo
2. **Experimenta libremente** - No tengas miedo de probar
3. **Guarda ejemplos** - Crea una carpeta de aprendizajes
4. **Practica diariamente** - 15-30 minutos al día es mejor que 3 horas una vez

---

## ✨ ¡Listo para Empezar!

Si cumples los requisitos de esta página, estás listo para:

👉 **[Comenzar con ADOPCIÓN I](./ADOPCION_I/README.md)**

O revisar el **[Índice Principal](./README.md)**

---

**Última actualización:** 13 de noviembre de 2025  
**Versión:** 1.0
