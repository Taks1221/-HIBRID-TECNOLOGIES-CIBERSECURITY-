from sklearn.ensemble import IsolationForest
import numpy as np

class ThreatAnalyzer:
    """Analizador de amenazas con IA"""
    
    PALABRAS_CLAVE = {
        'escaneo': ['nmap', 'masscan', 'scan', 'port', 'vuln'],
        'inyeccion': ['select', 'insert', 'drop', 'union', 'sql', '`', "'", '--'],
        'acceso_remoto': ['ssh', 'rdp', 'rsh', 'telnet', 'login', 'password'],
        'malware': ['eval', 'exec', 'system', 'shell', 'cmd', 'bash'],
        'xss': ['script', 'javascript', 'onerror', 'onload', '<iframe'],
        'ddos': ['flood', 'syn', 'ack', 'udp', 'icmp']
    }
    
    SEVERIDAD_MAPA = {
        'escaneo': 'media',
        'inyeccion': 'critica',
        'acceso_remoto': 'alta',
        'malware': 'critica',
        'xss': 'alta',
        'ddos': 'critica'
    }
    
    def analizar(self, payload):
        """Analizar payload y detectar tipo de amenaza"""
        payload_lower = payload.lower()
        
        # Buscar palabras clave
        for tipo, palabras in self.PALABRAS_CLAVE.items():
            if any(palabra in payload_lower for palabra in palabras):
                severidad = self.SEVERIDAD_MAPA.get(tipo, 'media')
                return tipo, severidad
        
        # Si no hay coincidencia, es anomalía
        return 'anomalia', 'baja'
