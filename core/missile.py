import numpy as np
from numpy.typing import NDArray

floatMatrix = NDArray[np.float64]

"""

@brief Missile class for simulating missile behavior in the simulation.
@file core/missile.py

@details This class handles the initialization of a missile's position and velocity.

@param initPosition: Initial position of the missile as a tuple (x, y, z).
@param initVelocity: Initial velocity of the missile as a tuple (vx, vy, vz).

"""

class Missile:
    def __init__(self, initPosition: tuple[float, float, float], initVelocity: tuple[float, float, float], mass: float, inertiaMatrix: floatMatrix):
        self.position: tuple[float, float, float] = initPosition # Initial position of the missile
        self.velocity: tuple[float, float, float] = initVelocity # Initial velocity of the missile
        self.acceleration: tuple[float, float, float] = (0.0, 0.0, 0.0)  # Default acceleration is zero

        self.mass: float = mass  # Mass of the missile, can be set from configuration
        self.inertiaMatrix: floatMatrix = inertiaMatrix  # Inertia matrix of the missile

if __name__ == "__main__":
    # Example usage
    missile = Missile((0.0, 0.0, 0.0), (1.0, 1.0, 1.0), 100.0, np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype=np.float64)) # type: ignore
    print(f"Missile initialized at position {missile.position} with velocity {missile.velocity}, mass {missile.mass}, and inertia matrix:\n{missile.inertiaMatrix}.")