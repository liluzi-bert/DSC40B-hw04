def knn_distance(arr, q, k):
    """Return (distance, value) where value is the k-th closest point in arr to q.
       Expected time Θ(n). Modifies arr in-place."""
    if not (1 <= k <= len(arr)):
        raise ValueError("k out of range")

    def key(v):
        return abs(v - q)

    def partition(lo, hi, p):
        pv = key(arr[p])
        arr[p], arr[hi] = arr[hi], arr[p]        # move pivot to end
        store = lo
        for i in range(lo, hi):
            if key(arr[i]) < pv:                 # ties go to the right (arbitrary tie rule)
                arr[store], arr[i] = arr[i], arr[store]
                store += 1
        arr[store], arr[hi] = arr[hi], arr[store]  # pivot to final place
        return store

    def quickselect(lo, hi, idx):
        while True:
            if lo == hi:
                return arr[lo]
            p = (lo + hi) // 2
            p = partition(lo, hi, p)
            if idx == p:
                return arr[p]
            elif idx < p:
                hi = p - 1
            else:
                lo = p + 1

    # k-th closest by distance corresponds to index k-1 after sorting by |x-q|
    val = quickselect(0, len(arr) - 1, k - 1)
    return (abs(val - q), val)
