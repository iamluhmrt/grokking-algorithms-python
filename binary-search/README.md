# Binary Search

Implementation of the binary search algorithm from Chapter 1 of Grokking Algorithms.

## How it works

Binary search works on **sorted lists**. Instead of checking every element one by one, it starts at the middle and eliminates half of the remaining elements on each step.

Given a sorted list of `n` elements, binary search finds the target in at most **log₂(n)** steps.

## Complexity

|              | Time     | Space |
| ------------ | -------- | ----- |
| Best case    | O(1)     | O(1)  |
| Average case | O(log n) | O(1)  |
| Worst case   | O(log n) | O(1)  |

## Example

```python
binary_search([1, 3, 5, 7, 9], 7)  # returns index 3
binary_search([1, 3, 5, 7, 9], 4)  # returns None
```

## Notes

- Input list must be sorted — binary search does not work on unsorted data
- Returns the index of the target if found, `None` otherwise
