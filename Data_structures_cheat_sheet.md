# 🧠 Python Data Structures Cheat Sheet
---

## 🔹 Core Data Structures

| Type             | Description                         | When to Use                               | Key Operations (Time)                            | Common Use Cases                                             |
|------------------|-------------------------------------|--------------------------------------------|--------------------------------------------------|--------------------------------------------------------------|
| `list`           | Ordered, mutable array              | Need ordering or index-based access        | `append`: O(1), `pop()`: O(1), `in`: O(n)        | Sequences, sorting, sliding windows                          |
| `set`            | Unordered, unique elements          | Fast membership test, remove duplicates    | `add`: O(1), `in`: O(1), `union`, `diff`: O(n)   | Deduplication, seen tracking, set operations                 |
| `dict`           | Key-value mapping (hash map)        | Map IDs to values, fast lookup             | `get/set`: O(1), `in`: O(1)                      | Frequency maps, ID lookups, JSON-like objects                |
| `Counter`        | Subclass of `dict` for counting     | Count frequency of items                   | `counts[key]`: O(1), `most_common`: O(k log k)   | Frequency counts, histogram-style queries                    |
| `defaultdict`    | Dict with default values            | Grouping or counting without key errors    | Same as `dict`                                   | Group by keys, multi-mapping, aggregations                   |
| `deque`          | Double-ended queue                  | Fast add/remove from both ends             | `append`: O(1), `popleft()`: O(1)                | Sliding windows, queues, BFS                                 |
| `tuple`          | Immutable ordered values            | Hashable keys, fixed structure             | `indexing`: O(1)                                 | Map keys, coordinates, lightweight records                   |
| `heapq` (heap)   | Min-heap priority queue             | Fast access to smallest/largest items      | `heappush`: O(log n), `heappop`: O(log n)        | Top-k problems, scheduling, streaming median                 |
| `pandas.DataFrame` | 2D tabular data (like SQL table) | Tabular data analysis and manipulation     | `loc`, `groupby`, `merge`, etc.                 | Joins, filtering, aggregations, EDA                          |
| `numpy.array`    | N-dimensional numeric array         | Fast math on large arrays                  | Vectorized ops                                   | Matrix math, vector ops, simulations                         |

---

## 🔹 Common Patterns and What to Use

| Problem Type                        | Use This             | Why                                                                 |
|------------------------------------|----------------------|----------------------------------------------------------------------|
| Deduplication                      | `set`                | Unique elements + fast lookup                                       |
| Frequency count                    | `Counter`, `defaultdict(int)` | Clean syntax, O(1) updates                                 |
| Map keys to values                 | `dict`               | Fast lookup                                                         |
| Track seen items                   | `set`                | Fast membership check                                               |
| Grouping by key                    | `defaultdict(list)`  | Clean and safe multi-key mapping                                    |
| Sliding window                     | `deque`              | Efficient pop from both ends                                        |
| Top-K elements                     | `heapq`              | Efficient access to min/max                                         |
| Ordered processing                 | `list` or `deque`    | Lists for index access, deque for queue behavior                    |
| Matrix / vector ops                | `numpy.array`        | Fast numeric computation                                            |
| Tabular data + joins               | `pandas.DataFrame`   | SQL-like functionality in Python                                    |

---
