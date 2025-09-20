# Configuración de Protección de Ramas

Este archivo contiene las configuraciones necesarias para proteger las ramas principales del repositorio.

## Configuración Manual en GitHub

### 1. Rama `main` (Producción)

Ir a: **Settings → Branches → Add rule**

**Branch name pattern:** `main`

**Configuraciones obligatorias:**
- ✅ **Restrict pushes that create files larger than 100MB**
- ✅ **Require a pull request before merging**
  - ✅ **Require approvals:** `2`
  - ✅ **Dismiss stale PR approvals when new commits are pushed**
  - ✅ **Require review from code owners**
- ✅ **Require status checks to pass before merging**
  - ✅ **Require branches to be up to date before merging**
  - **Required status checks:**
    - `quality-checks`
    - `unit-tests`
    - `integration-tests`
    - `build`
    - `security-scan`
- ✅ **Require conversation resolution before merging**
- ✅ **Include administrators**
- ✅ **Restrict pushes that create files larger than 100MB**

### 2. Rama `develop` (Desarrollo)

**Branch name pattern:** `develop`

**Configuraciones obligatorias:**
- ✅ **Require a pull request before merging**
  - ✅ **Require approvals:** `1`
  - ✅ **Dismiss stale PR approvals when new commits are pushed**
- ✅ **Require status checks to pass before merging**
  - **Required status checks:**
    - `quality-checks`
    - `unit-tests`
    - `build`
- ✅ **Include administrators**

## Configuración Automática via GitHub CLI

```bash
# Instalar GitHub CLI si no está instalado
# Windows: winget install --id GitHub.cli
# macOS: brew install gh
# Linux: sudo apt install gh

# Autenticarse
gh auth login

# Configurar protección para main
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["quality-checks","unit-tests","integration-tests","build","security-scan"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":2,"dismiss_stale_reviews":true,"require_code_owner_reviews":true}' \
  --field restrictions=null

# Configurar protección para develop
gh api repos/:owner/:repo/branches/develop/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["quality-checks","unit-tests","build"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null
```

## Configuración via GitHub Actions (Automatizada)

Crear workflow para configurar automáticamente:

```yaml
# .github/workflows/setup-branch-protection.yml
name: Setup Branch Protection

on:
  workflow_dispatch:  # Manual trigger only

jobs:
  setup-protection:
    runs-on: ubuntu-latest
    steps:
    - name: Setup Main Branch Protection
      uses: actions/github-script@v6
      with:
        script: |
          await github.rest.repos.updateBranchProtection({
            owner: context.repo.owner,
            repo: context.repo.repo,
            branch: 'main',
            required_status_checks: {
              strict: true,
              contexts: ['quality-checks', 'unit-tests', 'integration-tests', 'build', 'security-scan']
            },
            enforce_admins: true,
            required_pull_request_reviews: {
              required_approving_review_count: 2,
              dismiss_stale_reviews: true,
              require_code_owner_reviews: true
            },
            restrictions: null
          });

    - name: Setup Develop Branch Protection
      uses: actions/github-script@v6
      with:
        script: |
          await github.rest.repos.updateBranchProtection({
            owner: context.repo.owner,
            repo: context.repo.repo,
            branch: 'develop',
            required_status_checks: {
              strict: true,
              contexts: ['quality-checks', 'unit-tests', 'build']
            },
            enforce_admins: true,
            required_pull_request_reviews: {
              required_approving_review_count: 1,
              dismiss_stale_reviews: true
            },
            restrictions: null
          });
```

## CODEOWNERS File

Crear archivo `.github/CODEOWNERS` para definir revisores automáticos:

```
# Global owners
* @technical-lead @senior-developer

# Python code
*.py @python-expert @technical-lead

# CI/CD workflows
.github/workflows/ @devops-engineer @technical-lead

# Documentation
docs/ @technical-writer @technical-lead

# Critical files require additional review
calculadora_python.py @technical-lead @senior-developer @qa-lead
```

## Configuración de Teams y Permisos

### 1. Crear Teams en GitHub

1. **Technical Leads** - Admin access
2. **Senior Developers** - Write access  
3. **Developers** - Write access
4. **QA Team** - Write access
5. **DevOps** - Admin access

### 2. Permisos por Rama

**main branch:**
- Solo Technical Leads pueden hacer merge directo (emergencias)
- Todos los demás via PR con 2 aprobaciones

**develop branch:**
- Developers pueden hacer merge via PR con 1 aprobación
- Technical Leads pueden hacer merge directo

**feature branches:**
- Cualquier developer puede crear y pushear
- Merge solo via PR

**hotfix branches:**
- Solo Technical Leads y Senior Developers pueden crear
- Proceso acelerado pero con validaciones

## Scripts de Verificación

### Verificar Configuración Actual
```bash
# Verificar protección de main
gh api repos/:owner/:repo/branches/main/protection

# Verificar protección de develop  
gh api repos/:owner/:repo/branches/develop/protection

# Listar todas las ramas protegidas
gh api repos/:owner/:repo/branches --jq '.[] | select(.protected == true) | .name'
```

### Testing de Protecciones
```bash
# Intentar push directo (debería fallar)
git checkout main
echo "test" >> test.txt
git add test.txt
git commit -m "test direct push"
git push origin main  # Should fail

# Crear PR correctamente
git checkout -b test-branch
git push -u origin test-branch
gh pr create --title "Test PR" --body "Testing branch protection"
```

## Troubleshooting

### Problema: Status checks no aparecen
**Solución:** Ejecutar el workflow al menos una vez para que GitHub registre los status checks.

### Problema: No se pueden configurar protecciones
**Solución:** Verificar que tienes permisos de Admin en el repositorio.

### Problema: CODEOWNERS no funciona
**Solución:** 
1. Verificar sintaxis del archivo
2. Asegurar que los usuarios/teams existen
3. El archivo debe estar en `.github/CODEOWNERS`

## Validación Final

Después de configurar todo, verificar:
1. ✅ No se puede pushear directamente a `main`
2. ✅ No se puede pushear directamente a `develop`  
3. ✅ Los PRs requieren las aprobaciones configuradas
4. ✅ Los status checks se ejecutan automáticamente
5. ✅ Los CODEOWNERS son asignados automáticamente