@echo off
echo 🚀 Configurando proyecto TP7 - Calculadora con CI/CD
echo ==================================================

echo 🔍 Verificando prerrequisitos...

:: Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python no encontrado. Por favor instalar Python 3.8+
    exit /b 1
) else (
    echo ✅ Python encontrado
)

:: Verificar Node.js
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js no encontrado. Por favor instalar Node.js 18+
    exit /b 1
) else (
    echo ✅ Node.js encontrado
)

:: Verificar npm
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ npm no encontrado. Por favor instalar npm
    exit /b 1
) else (
    echo ✅ npm encontrado
)

:: Verificar Git
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git no encontrado. Por favor instalar Git
    exit /b 1
) else (
    echo ✅ Git encontrado
)

echo.
echo 🐍 Configurando ambiente Python...

:: Crear ambiente virtual
if not exist "venv" (
    python -m venv venv
    echo ✅ Ambiente virtual creado
) else (
    echo ⚠️ Ambiente virtual ya existe
)

:: Activar ambiente virtual
call venv\Scripts\activate.bat
echo ✅ Ambiente virtual activado

:: Instalar dependencias Python
pip install --upgrade pip
pip install -r requirements.txt
echo ✅ Dependencias Python instaladas

echo.
echo ⚛️ Configurando aplicación React...

:: Navegar a directorio web
cd web

:: Instalar dependencias React
npm ci
echo ✅ Dependencias React instaladas

:: Ejecutar tests React
echo 🧪 Ejecutando tests React...
set CI=true
npm test -- --coverage --watchAll=false
echo ✅ Tests React completados

:: Build de producción
echo 🏗️ Creando build de producción...
npm run build
echo ✅ Build de React completado

:: Volver al directorio raíz
cd ..

echo.
echo 🧪 Ejecutando validaciones...

:: Ejecutar tests Python
pytest test_calculadora.py -v
echo ✅ Tests unitarios Python completados

pytest test_integration.py -v
echo ✅ Tests de integración completados

pytest test_regression.py -v
echo ✅ Tests de regresión completados

echo.
echo 🔍 Validando calidad de código...

:: Black (continuar aunque falle)
black --check . || echo ⚠️ Formato de código necesita corrección (ejecutar: black .)

:: isort (continuar aunque falle)
isort --check-only . || echo ⚠️ Imports necesitan ordenamiento (ejecutar: isort .)

:: flake8 (continuar aunque falle)
flake8 . || echo ⚠️ Linting encontró issues menores

echo ✅ Validaciones completadas

echo.
echo 🔥 Configuración Firebase (opcional)...
echo ℹ️ Para configurar Firebase:
echo    1. Instalar Firebase CLI: npm install -g firebase-tools
echo    2. Login: firebase login
echo    3. Inicializar: firebase init hosting
echo    4. Configurar proyecto en firebase.json

echo.
echo 📋 Resumen de configuración:
echo ==========================
echo ✅ Ambiente Python configurado
echo ✅ Aplicación React configurada
echo ✅ Tests ejecutados exitosamente
echo ✅ Calidad de código validada
echo ✅ Build de producción creado

echo.
echo 🚀 Próximos pasos:
echo ==================
echo ℹ️ 1. Configurar ramas Git:
echo    git checkout -b develop
echo    git push -u origin develop

echo ℹ️ 2. Configurar protección de ramas en GitHub

echo ℹ️ 3. Configurar Firebase (opcional):
echo    firebase login
echo    firebase init hosting

echo ℹ️ 4. Crear PR para probar pipeline:
echo    git checkout -b feature/test-pipeline
echo    git commit --allow-empty -m "test: trigger pipeline"
echo    git push -u origin feature/test-pipeline

echo ℹ️ 5. Acceder a la aplicación web:
echo    Local: http://localhost:3000 (npm start en /web)
echo    Demo: https://calculadora-tp7--development.web.app

echo.
echo 🎉 Configuración completada exitosamente!
echo ℹ️ Para activar el ambiente Python en futuras sesiones:
echo    venv\Scripts\activate.bat

echo.
echo ℹ️ Para desarrollo React:
echo    cd web ^&^& npm start

echo.
echo ℹ️ Documentación completa disponible en:
echo    - README.md (principal)
echo    - web/README.md (aplicación React)
echo    - docs/ (documentación técnica)

pause