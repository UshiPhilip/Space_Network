from space_network_lib import *
import time


class Satellite(SpaceEntity):

    def receive_signal(self, packet: Packet):
        print(f"[{self.name}] Received: {packet}.")

def transmission_attempt(packet):
    spaceship = SpaceNetwork(level=2)
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