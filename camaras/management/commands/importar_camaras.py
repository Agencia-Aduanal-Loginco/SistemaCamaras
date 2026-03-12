"""
Comando para importar cámaras desde un archivo CSV.

Uso:
    python manage.py importar_camaras ruta/al/archivo.csv

El CSV debe tener las columnas: Empresa,Nombre,Modelo,Serie,Ip,MAC
"""

import csv
import re
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from camaras.models import Camara

MAC_REGEX = re.compile(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$')

# Valores que indican dato ausente
_SIN_VALOR = {'sin mac', 'sin mac', 'sin numero serie', ''}


def _normalizar_mac(valor: str) -> str:
    """Retorna la MAC en mayúsculas si es válida, o el valor original."""
    v = valor.strip()
    if MAC_REGEX.match(v):
        return v.upper()
    return v


class Command(BaseCommand):
    help = 'Importa cámaras desde un archivo CSV con columnas: Empresa,Nombre,Modelo,Serie,Ip,MAC'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Ruta al archivo CSV')
        parser.add_argument(
            '--omitir-duplicados',
            action='store_true',
            default=True,
            help='Omite filas cuya combinación empresa+nombre ya existe (por defecto: activado)',
        )

    def handle(self, *args, **options):
        csv_path = Path(options['csv_path'])

        if not csv_path.exists():
            raise CommandError(f'No se encontró el archivo: {csv_path}')

        importadas = 0
        omitidas = []

        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for i, fila in enumerate(reader, start=2):  # start=2 porque la fila 1 es el header
                empresa = fila.get('Empresa', '').strip()
                nombre = fila.get('Nombre', '').strip()
                modelo = fila.get('Modelo', '').strip()
                serie = fila.get('Serie', '').strip()
                ip = fila.get('Ip', '').strip()
                mac = _normalizar_mac(fila.get('MAC', ''))

                # Saltar filas sin datos esenciales
                if not empresa or not nombre:
                    omitidas.append((i, empresa or '(vacío)', nombre or '(vacío)', 'Empresa o Nombre vacíos'))
                    continue

                # Verificar duplicado por empresa+nombre
                if options['omitir_duplicados']:
                    if Camara.objects.filter(empresa=empresa, nombre=nombre).exists():
                        omitidas.append((i, empresa, nombre, 'Ya existe en la base de datos'))
                        continue

                # Crear el registro (sin pasar por el form para permitir datos incompletos del CSV)
                Camara.objects.create(
                    empresa=empresa,
                    nombre=nombre,
                    modelo=modelo or 'Sin modelo',
                    serie=serie or 'Sin serie',
                    ip=ip or '0.0.0.0',
                    mac=mac or 'SIN MAC',
                )
                importadas += 1
                self.stdout.write(f'  ✓ {empresa} — {nombre}')

        # Resumen
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(f'Importadas: {importadas}'))

        if omitidas:
            self.stdout.write(self.style.WARNING(f'Omitidas:   {len(omitidas)}'))
            for fila_num, emp, nom, razon in omitidas:
                self.stdout.write(f'  Fila {fila_num}: {emp} — {nom} → {razon}')
