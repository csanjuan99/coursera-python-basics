import pandas as pd

a = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

print(a)
print(a.describe())

b = pd.DataFrame({
    "Letters": ["A", "B", "C", "D", "E", "F"],
    "Numbers": [12, 8, 1, 11, 4, 9]})

print(b.sort_values(by="Numbers", ascending=False))

b = b.assign(new_value=b['Numbers'] * 3)
print(b)
