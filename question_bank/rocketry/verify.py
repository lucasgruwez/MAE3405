"""Recompute rocket-bank results with aide-memoire Tables 1, 3, 5, 12 and 13."""
from math import exp, isclose, log, pi, radians, sin, sqrt


def ideal_nozzle(temperature, molecular_weight, exit_pressure):
    gamma, chamber_pressure, throat_area = 1.15, 3e6, 0.1
    gas_constant = 8314 / molecular_weight
    speed = sqrt(2 * gamma * gas_constant * temperature / (gamma - 1)
                 * (1 - (exit_pressure / chamber_pressure) ** ((gamma - 1) / gamma)))
    flow = throat_area * chamber_pressure / sqrt(gas_constant * temperature) * sqrt(gamma) \
        * (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))
    return speed, flow


def burnout(speed, flow, duration, final_mass, angle):
    ratio = (final_mass + flow * duration) / final_mass
    angle = radians(angle)
    velocity = speed * log(ratio) - 9.81 * duration * sin(angle)
    distance = speed * duration * (1 - log(ratio) / (ratio - 1)) \
        - 0.5 * 9.81 * duration ** 2 * sin(angle)
    return velocity, distance * sin(angle)


def lossy_sonic_nozzle(temperature, cp, gas_constant):
    gamma = cp / (cp - gas_constant)
    pressure = 7e6 * (1 - (gamma - 1) / (0.95 * (gamma + 1))) ** (gamma / (gamma - 1))
    exit_temperature = 2 * temperature / (gamma + 1)
    speed = sqrt(gamma * gas_constant * exit_temperature)
    area = pi * 0.5 ** 2 / 4
    flow = pressure * area * speed / (gas_constant * exit_temperature)
    thrust = flow * speed + (pressure - 5474.8887) * area
    assert isclose(cp * (temperature - exit_temperature), speed ** 2 / 2)
    return flow, thrust


def check():
    for name, temperature, molecular_weight, target, target_coast in (
        ('Q01 kerosene', 3623, 25.29, 3061.161310, 1940093.456273),
        ('Q01 hydrogen', 2980, 10.08, 4397.484621, 3431553.021557),
    ):
        speed, flow = ideal_nozzle(temperature, molecular_weight, 12044.5709)
        assert isclose(speed, target, rel_tol=1e-8)
        assert isclose(speed * flow, 537399.965602, rel_tol=1e-8)
        velocity, height = burnout(speed, flow, 50, 1550, 80)
        radius = 6378e3  # Earth radius from Table 3, not the earlier 6371 km estimate.
        vertical_velocity = velocity * sin(radians(80))
        coast_altitude = 1 / (1 / (radius + height) - vertical_velocity ** 2 / (2 * 9.81 * radius ** 2)) - radius
        assert isclose(coast_altitude, target_coast, rel_tol=1e-8)
        print(name, 'speed, flow, burnout speed, vertical height, apogee:', speed, flow, velocity, height, coast_altitude)

    speed, flow = ideal_nozzle(3023.15, 22, 101325)
    _, height = burnout(speed, flow, 75, 3100, 85)
    assert isclose(speed * flow, 448382.430250, rel_tol=1e-8)
    assert isclose(height, 87345.223844, rel_tol=1e-8)
    print('Q02 thrust, height:', speed * flow, height)

    for stages, target_payload, target_propellant in ((1, 8.002139958, 916.997860042),
                                                     (2, 45.412001996, 863.605429023)):
        carried_fraction = exp(-11200 / (4500 * stages)) - 0.075
        initial_masses = [1000 * carried_fraction ** k for k in range(stages)]
        payload = 1000 * carried_fraction ** stages
        structure = 0.075 * sum(initial_masses)
        propellant = (1 - 0.075 - carried_fraction) * sum(initial_masses)
        assert isclose(payload, target_payload, rel_tol=1e-8)
        assert isclose(propellant, target_propellant, rel_tol=1e-8)
        assert isclose(payload + structure + propellant, 1000)
        print('Q03 stages, payload, propellant:', stages, payload, propellant)

    temperature = 298.15 + (0.9 * 241.827e6 - 48 * (2.016 * 14209.1 + 16.005 * 921.6)) / (18.015 * 1872.3)
    flow, thrust = lossy_sonic_nozzle(temperature, 1872.3, 461.52)
    assert isclose(thrust, 1669285.968100, rel_tol=1e-8)
    gamma = 1872.3 / (1872.3 - 461.52)
    cd_speed = sqrt(2 * 0.95 * 1872.3 * temperature
                    * (1 - (5474.8887 / 7e6) ** ((gamma - 1) / gamma)))
    assert isclose(flow * cd_speed, 2254056.893696, rel_tol=1e-8)
    print('Q04 chamber temperature, flow, converging/CD thrust:', temperature, flow, thrust, flow * cd_speed)

    product_heat_capacity = 528.12 * 841.8 + 234.195 * 1872.3
    temperature = 298.15 + (0.9 * 7575030e3 - 48 * (170 * 2000 + 592.185 * 921.6)) / product_heat_capacity
    flow, thrust = lossy_sonic_nozzle(temperature, product_heat_capacity / 762.315, 8314 / 30.4926)
    assert isclose(thrust, 1666846.799335, rel_tol=1e-8)
    assert isclose(flow / 0.95, 633.962174497, rel_tol=1e-8)
    print('Q05 chamber temperature, thrust, total flow:', temperature, thrust, flow / 0.95)
    print('All rocket checks passed.')


if __name__ == '__main__':
    check()
