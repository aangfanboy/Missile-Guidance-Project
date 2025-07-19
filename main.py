import config

from core.missile import Missile

if __name__ == "__main__":
    # Test importing missile from main.py
    missile = Missile((5.0, 10.0, 15.0), (2.0, 3.0, 4.0), config.MissileConfig.MISSILE_MASS)
    print(f"Missile imported and created: position {missile.position}, velocity {missile.velocity}, mass {missile.mass}")
