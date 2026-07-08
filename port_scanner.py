import socket
import sys


def scan_port(host, port):
    
    try:
        # Crea una conexion
        socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_conn.settimeout(1)  # Espera 1 segundo máximo
        
        result = socket_conn.connect_ex((host, port))
        socket_conn.close()
        
        if result == 0:
            return f"☀︎ Port {port}: OPEN"
        else:
            return f"☾ Port {port}: CLOSED"
    
    except socket.gaierror:
        return f"ERROR: Couldn't resolve with {host}"
    except socket.error:
        return f"ERROR: Couldn't connect to {host}"


if __name__ == "__main__":
    print("=" * 50)
    print("₍^. .^₎⟆ SIMPLE PORT SCANNER")
    print("=" * 50)
    
    
    target = "localhost"
    ports = [22, 80, 443, 8080, 3306] 
    
    print(f"\nScanning: {target}")
    print(f"Ports to verify: {ports}\n")
    
    for port in ports:
        print(scan_port(target, port))
    
    print("\n" + "=" * 50)
    print("𓆝 𓆟 𓆞 𓆝 Scan Completed 𓆝 𓆟 𓆞 𓆝")
    print("=" * 50)