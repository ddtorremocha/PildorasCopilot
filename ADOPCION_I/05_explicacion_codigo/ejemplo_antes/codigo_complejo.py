"""
Ejemplo de código legacy complejo que necesita explicación
Este archivo contiene código sin documentación que es difícil de entender
"""

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


import re

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
