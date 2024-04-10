# cache_utils.py
from django.core.cache import cache


def cached_query(query, key, timeout=None):
    """
    Cache the results of a query to improve performance.
    """
    cached_results = cache.get(key)

    if cached_results is not None:
        return cached_results

    results = query()
    cache.set(key, results, timeout=timeout)

    return results
