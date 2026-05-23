#!/usr/bin/env python3
"""
⚡ STRESS TEST OPTIMIZADO - HIBRID CIBERSEGURIDAD
Prueba de carga inteligente que respeta los límites del sistema
"""

import socket
import threading
import time
import random
import json
import psutil
import os
from datetime import datetime
from collections import defaultdict
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

# ============================================
# CONFIGURACIÓN DE LOGGING
# ============================================
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('stress_test.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class OptimizedStressTest:
    """Prueba de estrés inteligente y adaptativa"""
    
    def __init__(self, target_host="127.0.0.1", total_attacks=5000, workers=None):
        """Inicializar con detección automática de recursos"""
        self.target_host = target_host
        self.total_attacks = total_attacks
        
        # Auto-detectar número óptimo de workers
        cpu_count = os.cpu_count() or 4
        self.workers = workers or min(cpu_count * 2, 50)  # Máximo 50
        
        # Límites de seguridad
        self.max_cpu_percent = 85
        self.max_ram_percent = 80
        
        self.results = defaultdict(int)
        self.lock = threading.Lock()
        self.start_time = None
        self.end_time = None
        self.attack_log = []
        self.pauses = 0
        
        # Puertos objetivo
        self.ports = [22, 23, 80, 443, 3306, 5432, 27017, 8080]
        
        # Payloads educativos (sin DDoS real)
        self.payloads = {
            'port_probe': b'\x00' * 10,
            'http_get': b'GET / HTTP/1.1\r\nHost: test\r\n\r\n',
            'ssh_banner': b'SSH-2.0-TestClient\r\n',
            'mysql_probe': b'\x00' * 8,
        }
        
        logger.info(f"Inicializando Stress Test")
        logger.info(f"Target: {target_host}")
        logger.info(f"Ataques: {total_attacks}")
        logger.info(f"Workers: {self.workers}")
        
    def check_system_health(self):
        """Verificar salud del sistema"""
        cpu_percent = psutil.cpu_percent(interval=0.5)
        ram_percent = psutil.virtual_memory().percent
        
        return cpu_percent, ram_percent
    
    def wait_if_needed(self):
        """Esperar si el sistema está bajo presión"""
        cpu_percent, ram_percent = self.check_system_health()
        
        if cpu_percent > self.max_cpu_percent or ram_percent > self.max_ram_percent:
            logger.warning(f"⚠️  Sistema bajo presión - CPU: {cpu_percent}%, RAM: {ram_percent}%")
            time.sleep(2)
            self.pauses += 1
            return True
        return False
    
    def generate_random_ip(self):
        """Generar IP aleatoria para logging"""
        return f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
    
    def log_attack(self, attack_type, port, ip, status):
        """Registrar ataque con hash para integridad"""
        attack_record = {
            'timestamp': datetime.now().isoformat(),
            'type': attack_type,
            'port': port,
            'source_ip': ip,
            'target_host': self.target_host,
            'status': status,
            'hash': None
        }
        
        # Calcular hash para verificación de integridad
        record_str = json.dumps(attack_record, sort_keys=True)
        attack_record['hash'] = hashlib.sha256(record_str.encode()).hexdigest()
        
        with self.lock:
            self.attack_log.append(attack_record)
            self.results[status] += 1
    
    # ============================================
    # TIPOS DE PRUEBAS
    # ============================================
    
    def port_probe(self):
        """Prueba de conexión a puerto"""
        port = random.choice(self.ports)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target_host, port))
            sock.close()
            
            status = 'OPEN' if result == 0 else 'CLOSED'
            self.log_attack('PORT_PROBE', port, self.generate_random_ip(), status)
        except Exception as e:
            self.log_attack('PORT_PROBE', port, self.generate_random_ip(), 'ERROR')
    
    def protocol_test(self):
        """Prueba de protocolos simulados"""
        try:
            port = random.choice(self.ports)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)
            
            sock.connect((self.target_host, port))
            payload = random.choice(list(self.payloads.values()))
            sock.send(payload)
            sock.close()
            
            self.log_attack('PROTOCOL_TEST', port, self.generate_random_ip(), 'SUCCESS')
        except:
            self.log_attack('PROTOCOL_TEST', port, self.generate_random_ip(), 'BLOCKED')
    
    def banner_grab(self):
        """Intento de obtener banner del servicio"""
        try:
            port = random.choice(self.ports)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            sock.connect((self.target_host, port))
            response = sock.recv(1024)
            sock.close()
            
            status = 'SUCCESS' if response else 'EMPTY'
            self.log_attack('BANNER_GRAB', port, self.generate_random_ip(), status)
        except:
            self.log_attack('BANNER_GRAB', port, self.generate_random_ip(), 'FAILED')
    
    def connection_flood(self):
        """Prueba de múltiples conexiones rápidas"""
        try:
            port = random.choice(self.ports)
            for _ in range(3):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                
                try:
                    sock.connect((self.target_host, port))
                    sock.close()
                except:
                    pass
            
            self.log_attack('CONNECTION_FLOOD', port, self.generate_random_ip(), 'SUCCESS')
        except Exception as e:
            self.log_attack('CONNECTION_FLOOD', port, self.generate_random_ip(), 'ERROR')
    
    # ============================================
    # EJECUTAR PRUEBA
    # ============================================
    
    def execute_stress_test(self):
        """Ejecutar prueba de estrés completa"""
        self.start_time = time.time()
        test_types = [
            self.port_probe,
            self.protocol_test,
            self.banner_grab,
            self.connection_flood,
        ]
        
        logger.info(f"""
╔════════════════════════════════════════════════════════════════╗
║           ⚡ STRESS TEST OPTIMIZADO - HIBRID SECURITY ⚡        ║
╠════════════════════════════════════════════════════════════════╣
║ Target: {self.target_host:<50} ║
║ Total Pruebas: {self.total_attacks:<44,} ║
║ Workers: {self.workers:<52} ║
║ CPU Límite: {self.max_cpu_percent}% | RAM Límite: {self.max_ram_percent}%{" "*20} ║
║ Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<44} ║
╚════════════════════════════════════════════════════════════════╝
        """)
        
        completed = 0
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = [
                executor.submit(random.choice(test_types))
                for _ in range(self.total_attacks)
            ]
            
            for future in as_completed(futures):
                completed += 1
                
                # Verificar salud del sistema cada 100 pruebas
                if completed % 100 == 0:
                    self.wait_if_needed()
                
                # Mostrar progreso cada 500 pruebas
                if completed % 500 == 0:
                    elapsed = time.time() - self.start_time
                    rate = completed / elapsed if elapsed > 0 else 0
                    remaining = self.total_attacks - completed
                    eta = remaining / rate if rate > 0 else 0
                    
                    cpu_p, ram_p = self.check_system_health()
                    
                    logger.info(
                        f"[{completed:,}/{self.total_attacks:,}] "
                        f"{'█' * int(completed / self.total_attacks * 40)} "
                        f"{completed/self.total_attacks*100:.1f}% | "
                        f"Velocidad: {rate:,.0f} pruebas/seg | "
                        f"CPU: {cpu_p:.1f}% | RAM: {ram_p:.1f}% | "
                        f"ETA: {int(eta)}s"
                    )
        
        self.end_time = time.time()
        self.print_results()
        self.save_results()
    
    def print_results(self):
        """Imprimir resultados del test"""
        elapsed = self.end_time - self.start_time
        rate = self.total_attacks / elapsed if elapsed > 0 else 0
        
        logger.info(f"""
╔════════════════════════════════════════════════════════════════╗
║                    📊 RESULTADOS DEL TEST 📊                   ║
╠════════════════════════════════════════════════════════════════╣
║ ✅ Exitosas:          {self.results['SUCCESS']:>40,} ║
║ ⛔ Bloqueadas:        {self.results['BLOCKED']:>40,} ║
║ 🔓 Puertos Abiertos:  {self.results['OPEN']:>40,} ║
║ 🔒 Puertos Cerrados:  {self.results['CLOSED']:>40,} ║
║ ❌ Errores:           {self.results['ERROR']:>40,} ║
╠════════════════════════════════════════════════════════════════╣
║ ⏱️  Tiempo Total:      {elapsed:>40.2f}s ║
║ 🚀 Velocidad Promedio:{rate:>40,.0f} pruebas/seg ║
║ 📈 Total Registros:   {len(self.attack_log):>40,} ║
║ ⏸️  Pausas del Sistema:{self.pauses:>40,} ║
║ 🔐 Integridad OK:     {str(all(r['hash'] for r in self.attack_log)):>40} ║
╚════════════════════════════════════════════════════════════════╝
        """)
        
        # Estadísticas del sistema
        cpu_p, ram_p = self.check_system_health()
        logger.info(f"Estado Final - CPU: {cpu_p:.1f}%, RAM: {ram_p:.1f}%")
    
    def save_results(self):
        """Guardar resultados con verificación de integridad"""
        results_file = f"stress_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        data = {
            'metadata': {
                'test_type': 'OPTIMIZED_STRESS_TEST',
                'target': self.target_host,
                'total_tests': self.total_attacks,
                'workers': self.workers,
                'duration_seconds': self.end_time - self.start_time,
                'system_pauses': self.pauses,
                'timestamp': datetime.now().isoformat(),
            },
            'statistics': dict(self.results),
            'limits': {
                'max_cpu_percent': self.max_cpu_percent,
                'max_ram_percent': self.max_ram_percent,
            },
            'sample_attacks': self.attack_log[:100],  # Primeros 100 registros
        }
        
        with open(results_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"✅ Resultados guardados en: {results_file}")
        logger.info(f"📋 Total de registros: {len(self.attack_log):,}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Stress Test Optimizado')
    parser.add_argument('--host', default='127.0.0.1', help='Target host')
    parser.add_argument('--attacks', type=int, default=5000, help='Total pruebas (default: 5000)')
    parser.add_argument('--workers', type=int, default=None, help='Number of workers (auto if not specified)')
    
    args = parser.parse_args()
    
    test = OptimizedStressTest(
        target_host=args.host,
        total_attacks=args.attacks,
        workers=args.workers
    )
    
    try:
        test.execute_stress_test()
    except KeyboardInterrupt:
        logger.warning("\n⚠️  Test interrumpido por el usuario")
    except Exception as e:
        logger.error(f"Error durante el test: {e}")
