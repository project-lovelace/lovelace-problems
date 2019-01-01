function logistic_map(r) {
  let x = [0.5];
  for (let i = 0; i < 50; i++) {
    let last = x[x.length - 1];
    x.push(r * last * (1 - last));
  }
  return [x];
}