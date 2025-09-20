# Guía de Configuración de Ramas - Git Flow

## 1. Estructura de Ramas

### Configuración Inicial del Repositorio

Para implementar el Git Flow en tu repositorio, sigue estos pasos:

## 2. Comandos de Configuración

### 2.1 Crear rama develop
```bash
# Crear rama develop desde main
git checkout main
git checkout -b develop
git push -u origin develop
```

### 2.2 Configurar ramas de protección (GitHub)

**Para la rama `main`:**
- Settings → Branches → Add rule
- Branch name pattern: `main`
- ✅ Restrict pushes that create files larger than 100MB
- ✅ Require a pull request before merging
  - ✅ Require approvals: 2
  - ✅ Dismiss stale PR approvals when new commits are pushed
  - ✅ Require review from code owners
- ✅ Require status checks to pass before merging
  - ✅ Require branches to be up to date before merging
  - Required status checks: `test`, `lint`, `format-check`
- ✅ Require conversation resolution before merging
- ✅ Include administrators

**Para la rama `develop`:**
- Settings → Branches → Add rule
- Branch name pattern: `develop`
- ✅ Require a pull request before merging
  - ✅ Require approvals: 1
  - ✅ Dismiss stale PR approvals when new commits are pushed
- ✅ Require status checks to pass before merging
  - Required status checks: `test`, `lint`, `format-check`
- ✅ Include administrators

## 3. Convenciones de Nombres de Ramas

### 3.1 Feature Branches
```bash
feature/YYYY-MM-DD-descripcion-corta
# Ejemplo: feature/2024-03-15-calculadora-exponencial
```

### 3.2 Hotfix Branches
```bash
hotfix/YYYY-MM-DD-descripcion-problema
# Ejemplo: hotfix/2024-03-15-division-por-cero
```

### 3.3 Release Branches
```bash
release/vX.X.X
# Ejemplo: release/v1.2.0
```

## 4. Flujos de Trabajo

### 4.1 Desarrollo de Nueva Funcionalidad
```bash
# 1. Actualizar develop
git checkout develop
git pull origin develop

# 2. Crear feature branch
git checkout -b feature/2024-03-15-nueva-funcionalidad

# 3. Desarrollar y commitear
git add .
git commit -m "feat: agregar nueva funcionalidad X"

# 4. Push y crear PR
git push -u origin feature/2024-03-15-nueva-funcionalidad
# Crear PR en GitHub: feature/... → develop
```

### 4.2 Proceso de HOTFIX
```bash
# 1. Crear hotfix desde main
git checkout main
git pull origin main
git checkout -b hotfix/2024-03-15-error-critico

# 2. Implementar corrección
git add .
git commit -m "fix: corregir error crítico en producción"

# 3. Push y crear PR urgente
git push -u origin hotfix/2024-03-15-error-critico
# Crear PR en GitHub: hotfix/... → main (proceso acelerado)

# 4. Después del merge a main, también merge a develop
# Esto se puede automatizar con GitHub Actions
```

### 4.3 Release Process
```bash
# 1. Crear release branch desde develop
git checkout develop
git pull origin develop
git checkout -b release/v1.2.0

# 2. Preparar release (version bumps, changelog, etc.)
git add .
git commit -m "chore: prepare release v1.2.0"

# 3. PR a main para release
git push -u origin release/v1.2.0
# Crear PR: release/v1.2.0 → main

# 4. Después del merge, crear tag
git checkout main
git pull origin main
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0
```

## 5. Configuración Automática de Branch Protection

Puedes usar este script para configurar automáticamente las reglas de protección:

```bash
# Archivo: scripts/setup-branch-protection.sh
#!/bin/bash

# Configurar protección para main
curl -X PUT \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/USERNAME/REPO/branches/main/protection" \
  -d '{
    "required_status_checks": {
      "strict": true,
      "contexts": ["test", "lint", "format-check"]
    },
    "enforce_admins": true,
    "required_pull_request_reviews": {
      "required_approving_review_count": 2,
      "dismiss_stale_reviews": true,
      "require_code_owner_reviews": true
    },
    "restrictions": null
  }'

# Configurar protección para develop
curl -X PUT \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/USERNAME/REPO/branches/develop/protection" \
  -d '{
    "required_status_checks": {
      "strict": true,
      "contexts": ["test", "lint", "format-check"]
    },
    "enforce_admins": true,
    "required_pull_request_reviews": {
      "required_approving_review_count": 1,
      "dismiss_stale_reviews": true
    },
    "restrictions": null
  }'
```

## 6. Commit Message Conventions

Seguir el estándar [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Tipos de commits:
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Cambios de formato (no afectan lógica)
- `refactor`: Refactoring de código
- `test`: Agregar o modificar tests
- `chore`: Tareas de mantenimiento

### Ejemplos:
```bash
feat(calculadora): agregar función logaritmo
fix(division): corregir error de división por cero
docs(readme): actualizar instrucciones de instalación
test(integration): agregar pruebas de integración
chore(deps): actualizar dependencias de pytest
```

## 7. Hooks de Git (Opcional)

### Pre-commit hook para formateo automático:
```bash
# .git/hooks/pre-commit
#!/bin/bash
# Ejecutar black y flake8 antes de cada commit
black --check .
flake8 .
pytest --co -q
```

## 8. Integración con IDEs

### VS Code - Configuración recomendada:
```json
// .vscode/settings.json
{
  "git.defaultCloneDirectory": "./repos",
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "git.suggestSmartCommit": true,
  "gitlens.defaultDateStyle": "relative",
  "gitlens.blame.compact": true
}
```

Esta configuración te permitirá manejar efectivamente el flujo de Git según el plan de desarrollo y mantenimiento establecido.