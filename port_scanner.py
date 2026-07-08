import socket
import sys

# ========================================
# SIMPLE PORT SCANNER
# Un programa que verifica si puertos están abiertos
# ========================================

def scan_port(host, port):
    """
    Intenta conectarse a un puerto en un servidor.
    Si lo logra, el puerto está ABIERTO.
    Si no, está CERRADO.
    """
    try:
        # Crear una conexión
        socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_conn.settimeout(1)  # Esperar 1 segundo máximo
        
        result = socket_conn.connect_ex((host, port))
        socket_conn.close()
        
        if result == 0:
            return f"✓ Puerto {port}: ABIERTO"
        else:
            return f"✗ Puerto {port}: CERRADO"
    
    except socket.gaierror:
        return f"ERROR: No se pudo resolver {host}"
    except socket.error:
        return f"ERROR: No se pudo conectar a {host}"

# ========================================
# MAIN: El programa principal
# ========================================

if __name__ == "__main__":
    print("=" * 50)
    print("📡 SIMPLE PORT SCANNER")
    print("=" * 50)
    
    # Puedes probar con localhost (tu propia PC)
    target = "localhost"  # o "127.0.0.1"
    ports = [22, 80, 443, 8080, 3306]  # Puertos comunes a escanear
    
    print(f"\nEscaneando: {target}")
    print(f"Puertos a verificar: {ports}\n")
    
    for port in ports:
        print(scan_port(target, port))
    
    print("\n" + "=" * 50)
    print("Escaneo completado ✓")
    print("=" * 50)