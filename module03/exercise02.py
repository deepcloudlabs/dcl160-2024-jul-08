"""
immutable -> object pooling/caching -> memory footprint
"""
name1 = "jack bauer"
name2 = "jack bauer"
name3 = "jack bauer"
name3.upper()
# Garbage Collection
name1 = "jack shephard"
