from space_network_lib import *
import time


class Satellite(SpaceEntity):

    def receive_signal(self, packet: Packet):
        # Chacking if it's an instance
        if isinstance(packet, RelayPacket):
            # Unwrapping the message
            inner_packet = packet.data
            print(f"[{self.name}] - Unwrapping and forwarding to {inner_packet.receiver}.")
            # Sending to the receiver
            transmission_attempt(inner_packet)
        else:
            message = decryption(packet.data, b"P")
            print(f"[{self.name}]: Final destination reached: {message}")


class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(data=packet_to_relay, sender=sender, receiver=proxy)
        self.sender = sender

    def __repr__(self):
        return f"RelayPacket (Relaying [{self.data}] to {self.receiver} from {self.sender})"


class NotSatellite(SpaceEntity):
    def receive_signal(self, packet: Packet):
        pass


class EncryptedPacket(Packet):
    def __init__(self, data, sender, receiver, key):
        super().__init__(data, sender, receiver)
        self.key = key
        self.data = data
        EncryptedPacket.encryption(self)

    def encryption(self):
        if isinstance(self.data, str):
            self.data = self.data.encode()

        if len(self.key) < len(self.data):
            self.key = self.key * (len(self.data) // len(self.key) + 1)
            self.key = self.key[:len(self.data)]

        self.data = bytes([t ^ k for t, k in zip(self.data, self.key)]).decode()


def decryption(data, key):
    if isinstance(data, str):
        data = data.encode()

    if len(key) < len(data):
        key = key * (len(data) // len(key) + 1)
        key = key[:len(data)]
    return bytes([t ^ k for t, k in zip(data, key)]).decode()



def transmission_attempt(packet):
<<<<<<< HEAD
    spaceship = SpaceNetwork(level=6)
=======
    spaceship = SpaceNetwork(level=1)
>>>>>>> level-7
    while True:
        try:
            spaceship.send(packet)
            break
        except TemporalInterferenceError:
            print("Interference, waiting two seconds...")
            print("1...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
        except DataCorruptedError:
            print("Data corrupted, retrying...")
        except LinkTerminatedError:
            print("Link lost")
            raise "BrokenConnectionError"
        except OutOfRangeError:
            print("Target out of range.")
            raise "BrokenConnectionError"


def sanding_the_message(packet):
    try:
        transmission_attempt(packet)
    except:
        print("Transmission failed")


def wrapping_packet(message, sender, receiver, space_entity_list, key):
    if space_entity_list.index(sender) < space_entity_list.index(receiver):
        packet = EncryptedPacket(message, space_entity_list[space_entity_list.index(receiver)-1], receiver, key)
        for i in range(space_entity_list.index(receiver)-2, space_entity_list.index(sender)-1, -1):
            packet = RelayPacket(packet, space_entity_list[i], space_entity_list[i+1])
    else:
        packet = EncryptedPacket(message, space_entity_list[space_entity_list.index(receiver)+1], receiver, key)
        for i in range(space_entity_list.index(receiver)+1, space_entity_list.index(sender)):
            packet = RelayPacket(packet, space_entity_list[i+1], space_entity_list[i])
    sanding_the_message(packet)