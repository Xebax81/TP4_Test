# Plan de Desarrollo y Mantenimiento
*Trabajo Práctico 7 - Ingeniería de Software*

## 1. Introducción

Este documento establece las políticas, procedimientos y estándares para el desarrollo y mantenimiento del software, con especial énfasis en el **mantenimiento correctivo (HOTFIX)** para incidencias críticas en producción.

## 2. Estrategia de Ramas (Git Flow)

### 2.1 Estructura de Ramas
- **main**: Rama de producción (código estable y probado)
- **develop**: Rama de desarrollo e integración
- **feature/***: Ramas para nuevas funcionalidades
- **release/***: Ramas para preparación de versiones
- **hotfix/***: Ramas para correcciones críticas de producción

### 2.2 Flujo Normal de Desarrollo
1. Crear rama `feature/` desde `develop`
2. Desarrollo y pruebas locales
3. Pull Request hacia `develop`
4. **Pipeline Automático**: Se ejecuta automáticamente al crear el PR
5. Revisión de código (mínimo 2 revisores)
6. Merge a `develop` tras aprobación y pipeline exitoso
7. Despliegue automático a ambiente de desarrollo (post-merge)

## 3. Plan de Mantenimiento Correctivo (HOTFIX)

### 3.1 ¿Cómo se gestiona el cambio?

**Proceso de HOTFIX:**
1. **Detección y Reporte**: Identificación de incidencia crítica en producción
2. **Evaluación de Impacto**: El Technical Lead evalúa severidad y urgencia
3. **Conformación de Equipo**: 
   - Technical Lead (coordinador)
   - Desarrollador Senior (implementación)
   - QA Engineer (validación)
   - DevOps Engineer (despliegue)
4. **Creación de Rama**: `hotfix/YYYY-MM-DD-descripcion-breve` desde `main`
5. **Implementación**: Desarrollo de la solución mínima viable
6. **Validación Acelerada**: Ejecución de pruebas críticas
7. **Despliegue**: Deploy directo a producción tras aprobación
8. **Retroalimentación**: Merge a `main` y `develop`

### 3.2 ¿Hay proceso de revisión? ¿Cuál?

**Revisión Acelerada para HOTFIX:**
- **Revisión de Código**: 1 revisor técnico senior (mínimo)
- **Revisión de Impacto**: Technical Lead debe aprobar la solución
- **Validación QA**: Pruebas de regresión automáticas + validación manual crítica
- **Aprobación de Despliegue**: Product Owner o Technical Manager

**Criterios de Revisión:**
- ✅ Solución mínima que resuelve el problema específico
- ✅ No introduce nuevos riesgos
- ✅ Pasa todas las pruebas de regresión
- ✅ Documentación de cambios actualizada

### 3.3 ¿Cómo se gestiona el aseguramiento de la calidad?

**Estrategia de QA para HOTFIX:**

**Pruebas Automatizadas (Prioritarias):**
- ✅ Pruebas unitarias relacionadas al cambio
- ✅ Pruebas de regresión críticas (core business)
- ✅ Pruebas de integración de componentes afectados
- ✅ Smoke tests para funcionalidades principales

**Pruebas Manuales (Críticas):**
- ✅ Validación de la corrección del problema reportado
- ✅ Verificación de flujos críticos del negocio
- ✅ Pruebas de compatibilidad en ambiente productivo

**Análisis de Código:**
- ✅ Análisis estático (linting) automático
- ✅ Verificación de estándares de código
- ✅ Revisión de seguridad básica

### 3.4 ¿Por cuáles ambientes debe pasar el cambio?

**Ambientes para HOTFIX:**
1. **Desarrollo Local**: Validación inicial del desarrollador
2. **Staging/Pre-producción**: 
   - Copia exacta del ambiente productivo
   - Ejecución de pruebas de regresión completas
   - Validación final de QA
3. **Producción**: Despliegue final tras todas las validaciones

**Nota**: Se omite el ambiente de desarrollo compartido por urgencia temporal.

### 3.5 ¿El despliegue a producción es automatizado o manual?

**Estrategia Híbrida para HOTFIX:**

**Automatizado con Validaciones Manuales:**
- ✅ Pipeline automatizado para build y pruebas
- ✅ Despliegue automatizado a staging
- ✅ **Aprobación manual requerida** para producción
- ✅ Despliegue automatizado a producción tras aprobación
- ✅ Rollback automatizado disponible

**¿Requiere aprobación? ¿De quién?**
- **Aprobación Técnica**: Technical Lead
- **Aprobación de Negocio**: Product Owner (para cambios con impacto funcional)
- **Aprobación de Despliegue**: DevOps Lead o Technical Manager

## 4. Pipeline de HOTFIX vs Desarrollo Normal

### 4.1 Pipeline de Desarrollo Normal
```
Pull Request → develop (trigger automático)
├── Análisis estático completo (30 min)
├── Pruebas unitarias (10 min)
├── Pruebas de integración (20 min)
├── Verificación de formato (5 min)
├── Análisis de seguridad (10 min)
├── Build y verificación (10 min)
├── Revisión de código (2+ revisores)
└── Post-merge: Despliegue a desarrollo

Tiempo estimado: 2-4 horas
Trigger: SOLO Pull Requests hacia develop
```

### 4.2 Pipeline de HOTFIX
```
hotfix/* → main (staging → producción)
├── Análisis estático básico (5 min)
├── Pruebas unitarias críticas (5 min)
├── Pruebas de regresión (15 min)
├── Revisión de código (1 revisor senior)
├── Smoke tests en staging (10 min)
├── Aprobación manual
└── Despliegue a producción

Tiempo estimado: 45-60 minutos
```

## 5. Roles y Responsabilidades

### 5.1 Technical Lead
- Evaluar severidad de incidencias
- Coordinar equipo de HOTFIX
- Aprobar soluciones técnicas
- Autorizar despliegues críticos

### 5.2 Desarrollador Senior
- Implementar solución mínima viable
- Ejecutar pruebas locales
- Documentar cambios realizados

### 5.3 QA Engineer
- Ejecutar pruebas de regresión
- Validar corrección en staging
- Aprobar calidad de la solución

### 5.4 DevOps Engineer
- Gestionar despliegues
- Monitorear infraestructura
- Ejecutar rollbacks si es necesario

### 5.5 Product Owner
- Aprobar cambios con impacto funcional
- Comunicar a stakeholders
- Priorizar correcciones

## 6. Métricas y Monitoreo

### 6.1 SLAs para HOTFIX
- **Tiempo de Respuesta**: Máximo 2 horas desde reporte
- **Tiempo de Solución**: Máximo 4 horas para incidencias críticas
- **Disponibilidad**: Mínimo 99.9% uptime

### 6.2 Métricas de Calidad
- **Tasa de Éxito**: Porcentaje de HOTFIX sin rollback
- **Tiempo de Detección**: Tiempo promedio para identificar incidencias
- **Cobertura de Pruebas**: Mínimo 80% en código modificado

## 7. Herramientas y Tecnologías

### 7.1 Gestión de Código
- **Git**: Control de versiones
- **GitHub**: Repositorio y colaboración
- **GitHub Actions**: CI/CD automatizado

### 7.2 Calidad de Código
- **pytest**: Pruebas unitarias
- **flake8**: Análisis estático
- **black**: Formateo automático
- **coverage**: Cobertura de pruebas

### 7.3 Monitoreo y Alertas
- **GitHub Issues**: Tracking de incidencias
- **Slack/Teams**: Comunicación del equipo
- **Logs centralizados**: Análisis de errores

## 8. Procedimientos de Emergencia

### 8.1 Rollback Inmediato
En caso de que un HOTFIX cause nuevos problemas:
1. Ejecutar rollback automático
2. Notificar al equipo inmediatamente
3. Analizar causa raíz
4. Implementar nueva solución

### 8.2 Escalamiento
Si el HOTFIX no resuelve la incidencia en tiempo esperado:
1. Escalar a Technical Manager
2. Evaluar soluciones alternativas
3. Considerar rollback a versión estable anterior
4. Comunicar impacto a stakeholders

---

**Documento aprobado por**: Technical Team  
**Fecha de vigencia**: [Fecha actual]  
**Próxima revisión**: Cada 6 meses