#!/usr/bin/env python3
"""
🎯 SIMULADOR DE ATAQUES - Prueba del Sistema HIBRID
Simula diferentes tipos de amenazas para validar detección
"""

import socket
import threading
import time
import random
import requests
from datetime import datetime
import sys

class AttackSimulator:
    """Simula ataques para pruebas"""
    
    def __init__(self, target_host="localhost", ports=[22, 23, 80, 443, 3306, 5432, 27017]):
        self.target_host = target_host
        self.ports = ports
        self.attacks_count = 0
        
    def log(self, message):
        """Imprime con timestamp"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
    
    # ============================================
    # TIPOS DE ATAQUES SIMULADOS
    # ============================================
    
    def attack_port_scan(self, port):
        """🔍 Simula escaneo de puertos (Nmap-like)"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target_host, port))
            sock.close()
            
            if result == 0:
                self.log(f"✅ [ESCANEO] Puerto {port} ABIERTO")
                self.attacks_count += 1
            return result == 0
        except Exception as e:
            self.log(f"❌ Error escaneo puerto {port}: {e}")
            return False
    
    def attack_ssh_bruteforce(self):
        """🔐 Simula intento SSH fuerza bruta"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            
            # Intenta múltiples veces (simulando fuerza bruta)
            for attempt in range(5):
                try:
                    sock.connect((self.target_host, 22))
                    payload = b"SSH-2.0-OpenSSH_7.4\r\n"
                    sock.send(payload)
                    response = sock.recv(1024)
                    self.log(f"⚠️  [SSH BRUTEFORCE] Intento {attempt+1}/5")
                    self.attacks_count += 1
                    time.sleep(0.5)
                except:
                    pass
            sock.close()
        except Exception as e:
            self.log(f"Error SSH: {e}")
    
    def attack_sql_injection(self):
        """💉 Simula SQL Injection"""
        payloads = [
            "' OR '1'='1",
            "'; DROP TABLE users--",
            "1' UNION SELECT NULL--",
            "admin' --",
            "1'; DELETE FROM threats--"
        ]
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((self.target_host, 3306))
            
            for payload in payloads:
                sock.send(payload.encode())
                self.log(f"💉 [SQL INJECTION] Payload: {payload[:30]}...")
                self.attacks_count += 1
                time.sleep(0.3)
            
            sock.close()
        except Exception as e:
            self.log(f"Error SQL: {e}")
    
    def attack_xss_payload(self):
        """❌ Simula XSS (Cross-Site Scripting)"""
        payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror='alert(1)'>",
            "<iframe src='javascript:alert(1)'></iframe>",
            "<svg onload=alert('XSS')>",
        ]
        
        for payload in payloads:
            self.log(f"❌ [XSS] Payload: {payload[:40]}...")
            self.attacks_count += 1
            time.sleep(0.2)
    
    def attack_ddos_simulation(self):
        """💥 Simula ataque DDoS (conexiones rápidas)"""
        self.log("💥 [DDoS] Iniciando simulación...")
        
        for i in range(10):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                sock.connect((self.target_host, 80))
                sock.send(b"GET / HTTP/1.1\r\n\r\n")
                sock.close()
                self.attacks_count += 1
            except:
                pass
            
            if (i + 1) % 5 == 0:
                self.log(f"💥 [DDoS] {i+1}/10 conexiones enviadas")
    
    def attack_telnet_login(self):
        """🔐 Simula intento Telnet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((self.target_host, 23))
            
            sock.send(b"admin\r\n")
            time.sleep(0.2)
            sock.send(b"password123\r\n")
            
            self.log("🔐 [TELNET] Intento de login simulado")
            self.attacks_count += 1
            sock.close()
        except Exception as e:
            self.log(f"Error Telnet: {e}")
    
    def attack_mongodb_scan(self):
        """📊 Simula escaneo MongoDB"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((self.target_host, 27017))
            
            # Payload MongoDB específico
            payload = b"\x3a\x00\x00\x00\x3a\x00\x00\x00\x00\x00"
            sock.send(payload)
            
            self.log("📊 [MONGODB] Intento de conexión detectado")
            self.attacks_count += 1
            sock.close()
        except Exception as e:
            self.log(f"Error MongoDB: {e}")
    
    def attack_malware_signature(self):
        """🦠 Simula ejecución de código malicioso"""
        signatures = [
            "eval(base64_decode())",
            "system('rm -rf /')",
            "exec('nc -e /bin/sh')",
            "ShellCode_Execution",
            "/dev/tcp/attacker/port"
        ]
        
        for sig in signatures:
            self.log(f"🦠 [MALWARE] Firma detectada: {sig}")
            self.attacks_count += 1
            time.sleep(0.2)
    
    # ============================================
    # EJECUTAR SIMULACIÓN COMPLETA
    # ============================================
    
    def run_full_simulation(self):
        """Ejecuta todos los ataques simulados"""
        self.log("=" * 60)
        self.log("🎯 INICIANDO SIMULACIÓN DE ATAQUES - HIBRID SECURITY")
        self.log("=" * 60)
        
        # Escaneo de puertos
        self.log("\n[FASE 1] Escaneo de Puertos...")
        threads = []
        for port in self.ports:
            t = threading.Thread(target=self.attack_port_scan, args=(port,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        time.sleep(2)
        
        # SSH Fuerza Bruta
        self.log("\n[FASE 2] Intento SSH Fuerza Bruta...")
        self.attack_ssh_bruteforce()
        time.sleep(2)
        
        # SQL Injection
        self.log("\n[FASE 3] Ataques SQL Injection...")
        self.attack_sql_injection()
        time.sleep(2)
        
        # XSS
        self.log("\n[FASE 4] Ataques XSS...")
        self.attack_xss_payload()
        time.sleep(2)
        
        # DDoS
        self.log("\n[FASE 5] Simulación DDoS...")
        self.attack_ddos_simulation()
        time.sleep(2)
        
        # Telnet
        self.log("\n[FASE 6] Intento Telnet...")
        self.attack_telnet_login()
        time.sleep(2)
        
        # MongoDB
        self.log("\n[FASE 7] Escaneo MongoDB...")
        self.attack_mongodb_scan()
        time.sleep(2)
        
        # Malware
        self.log("\n[FASE 8] Detección de Malware...")
        self.attack_malware_signature()
        
        # Resultado final
        self.log("\n" + "=" * 60)
        self.log(f"✅ SIMULACIÓN COMPLETADA")
        self.log(f"📊 Total de ataques simulados: {self.attacks_count}")
        self.log("=" * 60)
        
        return self.attacks_count

def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="🎯 Simulador de Ataques para HIBRID Security"
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host objetivo (default: localhost)"
    )
    parser.add_argument(
        "--ports",
        default="22,23,80,443,3306,5432,27017",
        help="Puertos a escanear (default: 22,23,80,443,3306,5432,27017)"
    )
    
    args = parser.parse_args()
    
    ports = [int(p.strip()) for p in args.ports.split(",")]
    
    # Crear y ejecutar simulador
    simulator = AttackSimulator(target_host=args.host, ports=ports)
    simulator.run_full_simulation()

if __name__ == "__main__":
    main()
