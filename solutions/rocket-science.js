var v_e = 2550  // rocket exhaust velocity [m/s]
var M = 250000  // rocket dry mass [kg]

function rocket_fuel(v) {
  var fuel_mass = M * (Math.exp(v / v_e) - 1);
  return fuel_mass;
}
