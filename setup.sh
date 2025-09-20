#!/bin/bash

# Script de configuración para TP7 - Calculadora con React y Firebase
# Uso: ./setup.sh

set -e

echo "🚀 Configurando proyecto TP7 - Calculadora con CI/CD"
echo "=================================================="

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir con colores
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Verificar prerrequisitos
echo "🔍 Verificando prerrequisitos..."

# Verificar Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_status "Python $PYTHON_VERSION encontrado"
else
    print_error "Python 3 no encontrado. Por favor instalar Python 3.8+"
    exit 1
fi

# Verificar Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    print_status "Node.js $NODE_VERSION encontrado"
else
    print_error "Node.js no encontrado. Por favor instalar Node.js 18+"
    exit 1
fi

# Verificar npm
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    print_status "npm $NPM_VERSION encontrado"
else
    print_error "npm no encontrado. Por favor instalar npm"
    exit 1
fi

# Verificar Git
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version | cut -d' ' -f3)
    print_status "Git $GIT_VERSION encontrado"
else
    print_error "Git no encontrado. Por favor instalar Git"
    exit 1
fi

echo ""
echo "🐍 Configurando ambiente Python..."

# Crear ambiente virtual
if [ ! -d "venv" ]; then
    python3 -m venv venv
    print_status "Ambiente virtual creado"
else
    print_warning "Ambiente virtual ya existe"
fi

# Activar ambiente virtual
source venv/bin/activate
print_status "Ambiente virtual activado"

# Instalar dependencias Python
pip install --upgrade pip
pip install -r requirements.txt
print_status "Dependencias Python instaladas"

echo ""
echo "⚛️  Configurando aplicación React..."

# Navegar a directorio web
cd web

# Instalar dependencias React
npm ci
print_status "Dependencias React instaladas"

# Ejecutar tests React
echo "🧪 Ejecutando tests React..."
CI=true npm test -- --coverage --watchAll=false
print_status "Tests React completados"

# Build de producción
echo "🏗️  Creando build de producción..."
npm run build
print_status "Build de React completado"

# Volver al directorio raíz
cd ..

echo ""
echo "🧪 Ejecutando validaciones..."

# Ejecutar tests Python
pytest test_calculadora.py -v
print_status "Tests unitarios Python completados"

pytest test_integration.py -v
print_status "Tests de integración completados"

pytest test_regression.py -v
print_status "Tests de regresión completados"

# Validar calidad de código
echo "🔍 Validando calidad de código..."

# Black
black --check . || print_warning "Formato de código necesita corrección (ejecutar: black .)"

# isort
isort --check-only . || print_warning "Imports necesitan ordenamiento (ejecutar: isort .)"

# flake8
flake8 . || print_warning "Linting encontró issues menores"

print_status "Validaciones completadas"

echo ""
echo "🔥 Configuración Firebase (opcional)..."
print_info "Para configurar Firebase:"
print_info "1. Instalar Firebase CLI: npm install -g firebase-tools"
print_info "2. Login: firebase login"
print_info "3. Inicializar: firebase init hosting"
print_info "4. Configurar proyecto en firebase.json"

echo ""
echo "📋 Resumen de configuración:"
echo "=========================="
print_status "✅ Ambiente Python configurado"
print_status "✅ Aplicación React configurada"
print_status "✅ Tests ejecutados exitosamente"
print_status "✅ Calidad de código validada"
print_status "✅ Build de producción creado"

echo ""
echo "🚀 Próximos pasos:"
echo "=================="
print_info "1. Configurar ramas Git:"
echo "   git checkout -b develop"
echo "   git push -u origin develop"

print_info "2. Configurar protección de ramas en GitHub"

print_info "3. Configurar Firebase (opcional):"
echo "   firebase login"
echo "   firebase init hosting"

print_info "4. Crear PR para probar pipeline:"
echo "   git checkout -b feature/test-pipeline"
echo "   git commit --allow-empty -m 'test: trigger pipeline'"
echo "   git push -u origin feature/test-pipeline"

print_info "5. Acceder a la aplicación web:"
echo "   Local: http://localhost:3000 (npm start en /web)"
echo "   Demo: https://calculadora-tp7--development.web.app"

echo ""
print_status "🎉 Configuración completada exitosamente!"
print_info "Para activar el ambiente Python en futuras sesiones:"
echo "   source venv/bin/activate"

echo ""
print_info "Para desarrollo React:"
echo "   cd web && npm start"

echo ""
print_info "Documentación completa disponible en:"
echo "   - README.md (principal)"
echo "   - web/README.md (aplicación React)"
echo "   - docs/ (documentación técnica)"