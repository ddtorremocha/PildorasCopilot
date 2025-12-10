"""
Ejemplo de código legacy complejo que necesita explicación
Este archivo contiene código sin documentación que es difícil de entender
"""
import re

def process_data(data, config=None):
    result = []
    for item in data:
        if not config or (config.get('filter') and item.get(config['filter']['key']) == config['filter']['value']):
            processed = {
                'id': item['id'],
                'value': item['value'] * (config.get('multiplier', 1) if config else 1),
                'metadata': {
                    'original': item['value'],
                    'timestamp': item.get('ts', None)
                }
            }
            if config and config.get('transform'):
                processed['value'] = config['transform'](processed['value'])
            result.append(processed)
    return result


def calculate_metrics(data_points, window=5):
    metrics = []
    for i in range(len(data_points) - window + 1):
        window_data = data_points[i:i + window]
        avg = sum(w['value'] for w in window_data) / window
        max_val = max(w['value'] for w in window_data)
        min_val = min(w['value'] for w in window_data)
        volatility = max_val - min_val
        
        metrics.append({
            'window_start': i,
            'avg': round(avg, 2),
            'max': max_val,
            'min': min_val,
            'volatility': round(volatility, 2),
            'trend': 'up' if window_data[-1]['value'] > window_data[0]['value'] else 'down'
        })
    
    return metrics




def parse_expression(expr):
    # Esta regex es compleja y necesita explicación
    pattern = r'(?P<func>\w+)\((?P<args>[^)]+)\)|(?P<var>\w+)|(?P<op>[+\-*/])|(?P<num>\d+\.?\d*)'
    tokens = []
    for match in re.finditer(pattern, expr):
        if match.group('func'):
            tokens.append({'type': 'function', 'name': match.group('func'), 'args': match.group('args').split(',')})
        elif match.group('var'):
            tokens.append({'type': 'variable', 'name': match.group('var')})
        elif match.group('op'):
            tokens.append({'type': 'operator', 'value': match.group('op')})
        elif match.group('num'):
            tokens.append({'type': 'number', 'value': float(match.group('num'))})
    return tokens


class DataProcessor:
    def __init__(self, cache_size=100):
        self._cache = {}
        self._cache_size = cache_size
        self._hits = 0
        self._misses = 0
    
    def get_or_compute(self, key, compute_fn, *args, **kwargs):
        if key in self._cache:
            self._hits += 1
            return self._cache[key]
        
        self._misses += 1
        result = compute_fn(*args, **kwargs)
        
        if len(self._cache) >= self._cache_size:
            # LRU eviction - remove first item
            self._cache.pop(next(iter(self._cache)))
        
        self._cache[key] = result
        return result
    
    def stats(self):
        total = self._hits + self._misses
        hit_rate = (self._hits / total * 100) if total > 0 else 0
        return {
            'hits': self._hits,
            'misses': self._misses,
            'hit_rate': f'{hit_rate:.1f}%',
            'cache_size': len(self._cache)
        }


# Algoritmo complejo sin explicación
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


# === MAIN - Pruebas ===
if __name__ == "__main__":
    print("=== Ejemplos de Código Complejo ===\n")
    
    # 1. Probar process_data
    print("1. process_data - Procesamiento de datos con filtros y transformaciones:")
    data = [
        {'id': 1, 'value': 10, 'status': 'active', 'ts': '2024-01-01'},
        {'id': 2, 'value': 20, 'status': 'inactive', 'ts': '2024-01-02'},
        {'id': 3, 'value': 15, 'status': 'active', 'ts': '2024-01-03'},
        {'id': 4, 'value': 25, 'status': 'active', 'ts': '2024-01-04'},
    ]
    
    # Sin configuración
    result1 = process_data(data)
    print(f"   Sin config: {len(result1)} items procesados")
    
    # Con filtro
    config_filter = {
        'filter': {'key': 'status', 'value': 'active'},
        'multiplier': 2
    }
    result2 = process_data(data, config_filter)
    print(f"   Con filtro 'active' y multiplicador 2:")
    for item in result2:
        print(f"      ID {item['id']}: {item['metadata']['original']} → {item['value']}")
    
    # Con transformación (sin filtro)
    print(f"   Con transformación (x^2) - procesando sin filtro:")
    config_transform = {
        'transform': lambda x: round(x ** 2, 2)
    }
    # Procesar sin config primero, luego transformar manualmente para demostrar
    temp_data = [{'id': item['id'], 'value': item['value']} for item in data]
    result3_values = [config_transform['transform'](item['value']) for item in temp_data]
    print(f"      Ejemplo: 10 → {result3_values[0]}, 20 → {result3_values[1]}")
    
    # 2. Probar calculate_metrics
    print("\n2. calculate_metrics - Análisis de ventanas deslizantes:")
    data_points = [
        {'value': 10}, {'value': 15}, {'value': 12}, 
        {'value': 18}, {'value': 20}, {'value': 17},
        {'value': 22}, {'value': 19}
    ]
    
    metrics = calculate_metrics(data_points, window=3)
    print(f"   Métricas calculadas con ventana de 3:")
    for m in metrics[:3]:  # Mostrar solo las primeras 3
        print(f"      Ventana {m['window_start']}: avg={m['avg']}, "
              f"volatilidad={m['volatility']}, tendencia={m['trend']}")
    
    # 3. Probar parse_expression
    print("\n3. parse_expression - Parser de expresiones matemáticas:")
    expressions = [
        "sum(a,b,c)",
        "x + y * 2",
        "calculate(10.5, 20)"
    ]
    
    for expr in expressions:
        tokens = parse_expression(expr)
        print(f"   '{expr}':")
        for token in tokens:
            print(f"      {token}")
    
    # 4. Probar DataProcessor con cache
    print("\n4. DataProcessor - Sistema de cache con LRU:")
    processor = DataProcessor(cache_size=3)
    
    # Función de cálculo costosa
    def expensive_calculation(n):
        return n ** 2
    
    # Realizar cálculos
    results = []
    for i in [1, 2, 3, 2, 1, 4, 2]:
        result = processor.get_or_compute(f"calc_{i}", expensive_calculation, i)
        results.append(result)
    
    print(f"   Resultados: {results}")
    stats = processor.stats()
    print(f"   Estadísticas del cache:")
    print(f"      Hits: {stats['hits']}, Misses: {stats['misses']}")
    print(f"      Hit rate: {stats['hit_rate']}")
    print(f"      Cache size: {stats['cache_size']}")
    
    # 5. Probar quickselect
    print("\n5. quickselect - Encontrar k-ésimo elemento más pequeño:")
    arr = [7, 10, 4, 3, 20, 15, 8, 2]
    print(f"   Array: {arr}")
    
    for k in [0, 3, 7]:
        result = quickselect(arr.copy(), k)
        sorted_arr = sorted(arr)
        print(f"   k={k}: {result} (elemento en posición {k} del array ordenado: {sorted_arr[k]})")
    
    print("\n=== ¡Todas las pruebas completadas! ===")
    print("Este código es complejo y difícil de entender sin explicaciones.")
    print("Usa GitHub Copilot para obtener explicaciones detalladas de cada función.")
