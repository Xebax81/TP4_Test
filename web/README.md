# 🧮 Calculadora Web - TP7

Interfaz web React para la calculadora Python desarrollada como parte del TP7 de Ingeniería de Software.

## 🚀 Demo en Vivo

- **Development**: https://calculadora-tp7--development.web.app
- **Staging**: https://calculadora-tp7--staging.web.app

## ✨ Características

### 🎯 Funcionalidades
- ✅ Operaciones básicas: suma, resta, multiplicación, división
- ✅ Interfaz intuitiva y responsive
- ✅ Manejo de errores (división por cero)
- ✅ Diseño moderno con efectos visuales
- ✅ Status del pipeline CI/CD en tiempo real

### 🔧 Tecnologías
- **Frontend**: React 18.2.0
- **Estilo**: CSS3 con gradientes y efectos glassmorphism
- **Testing**: Jest + React Testing Library
- **Build**: Create React App
- **Deploy**: Firebase Hosting
- **CI/CD**: GitHub Actions

## 🏗️ Arquitectura del Proyecto

```
web/
├── public/
│   └── index.html          # HTML base
├── src/
│   ├── App.js              # Componente principal
│   ├── App.css             # Estilos principales
│   ├── App.test.js         # Tests de la aplicación
│   ├── index.js            # Punto de entrada
│   ├── index.css           # Estilos globales
│   └── setupTests.js       # Configuración de tests
├── package.json            # Dependencias y scripts
└── README.md               # Esta documentación
```

## 🚀 Desarrollo Local

### Prerrequisitos
- Node.js 18+
- npm o yarn

### Instalación
```bash
cd web
npm install
```

### Desarrollo
```bash
npm start
```
Abre [http://localhost:3000](http://localhost:3000) en tu navegador.

### Tests
```bash
# Ejecutar tests una vez
npm test -- --watchAll=false

# Ejecutar tests con cobertura
npm test -- --coverage --watchAll=false

# Tests en modo watch
npm test
```

### Build de Producción
```bash
npm run build
```

## 🔄 CI/CD Pipeline

### Pipeline Principal
El pipeline se ejecuta automáticamente cuando:
- Se crea un Pull Request hacia `develop`
- Se actualiza un PR existente

**Pasos del Pipeline:**
1. 🔍 Checkout del código
2. ⚙️ Setup Node.js 18
3. 📦 Instalación de dependencias
4. 🧪 Ejecución de tests
5. 🏗️ Build de producción
6. ✅ Validación del build

### Deploy Automático
El deploy se ejecuta automáticamente cuando:
- Se hace merge a la rama `develop`

**Pasos del Deploy:**
1. 📦 Build de la aplicación React
2. 🐍 Validación del backend Python
3. 🚀 Deploy a Firebase Hosting
4. 📢 Notificación al equipo

## 🧪 Testing Strategy

### Unit Tests
- ✅ Renderizado de componentes
- ✅ Interacciones de usuario
- ✅ Operaciones matemáticas
- ✅ Manejo de errores
- ✅ Estado de la aplicación

### Integration Tests
- ✅ Flujos completos de cálculo
- ✅ Navegación entre estados
- ✅ Validación de UI/UX

### Coverage Goals
- **Statements**: > 80%
- **Branches**: > 75%
- **Functions**: > 80%
- **Lines**: > 80%

## 🎨 Design System

### Colores
- **Primary**: Gradiente azul-púrpura (#667eea → #764ba2)
- **Buttons**: Glassmorphism con transparencias
- **Operators**: Naranja (#FFA500)
- **Equals**: Verde (#00FF00)
- **Clear**: Rojo (#FF0000)

### Typography
- **Font Family**: System fonts (Apple/Segoe UI/Roboto)
- **Sizes**: 2.5rem (display), 1.5rem (buttons), 1.1rem (text)
- **Weight**: Bold para números y botones

### Effects
- **Glassmorphism**: `backdrop-filter: blur(10px)`
- **Shadows**: Multiple layers para profundidad
- **Hover**: Transform y transiciones suaves
- **Responsive**: Grid layout adaptativo

## 🔧 Configuración Firebase

### firebase.json
```json
{
  "hosting": {
    "public": "web/build",
    "rewrites": [{"source": "**", "destination": "/index.html"}],
    "headers": [
      {
        "source": "/static/**",
        "headers": [{"key": "Cache-Control", "value": "max-age=31536000"}]
      }
    ]
  }
}
```

### Deploy Channels
- **production**: Rama `main`
- **development**: Rama `develop`
- **staging**: Tags de release

## 📊 Performance

### Métricas Objetivo
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Time to Interactive**: < 3.0s
- **Bundle Size**: < 500KB

### Optimizaciones
- ✅ Code splitting automático
- ✅ Assets optimization
- ✅ Gzip compression
- ✅ CDN caching (Firebase)

## 🛠️ Desarrollo y Contribución

### Estándares de Código
- **ESLint**: Configuración React estándar
- **Prettier**: Formateo automático
- **Tests**: Obligatorios para nuevas features

### Proceso de Desarrollo
1. Crear rama desde `develop`
2. Desarrollar feature localmente
3. Escribir tests
4. Crear Pull Request
5. Pipeline automático valida cambios
6. Revisión de código
7. Merge tras aprobación

### Git Flow
```bash
# Crear nueva feature
git checkout develop
git pull origin develop
git checkout -b feature/nueva-calculadora-feature

# Desarrollo...
git add .
git commit -m "feat: add nueva feature"
git push -u origin feature/nueva-calculadora-feature

# Crear PR en GitHub hacia develop
```

## 🐛 Troubleshooting

### Problemas Comunes

**Error: Module not found**
```bash
cd web
rm -rf node_modules package-lock.json
npm install
```

**Tests fallan**
```bash
npm test -- --no-coverage --verbose
```

**Build falla**
```bash
npm run build -- --verbose
```

**Deploy falla**
- Verificar configuración de Firebase
- Revisar secrets de GitHub Actions
- Validar permisos del service account

## 📚 Recursos

- [React Documentation](https://reactjs.org/)
- [Firebase Hosting](https://firebase.google.com/docs/hosting)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Testing Library](https://testing-library.com/)

---

**Desarrollado para TP7 - Ingeniería de Software 2024**