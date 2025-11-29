def es_cero(x: float) -> bool:
    return abs(x) < 1e-7

def es_cercano(x: float, y: float) -> bool:
    return abs(x - y) < 1e-7