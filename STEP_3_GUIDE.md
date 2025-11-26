# Migration Step 3: Core Logic Migration

## **Step Overview and Objectives**
The objective of this step is to migrate the core business logic and algorithms from Java to Python while ensuring functional parity, readability, and maintainability. This involves translating core functions, adapting existing data structures to Python-native equivalents, and porting algorithms effectively. The migrated code will serve as the backbone of the application's functionality in Python.

---

## **Prerequisites and Dependencies**
Before beginning this step, ensure the following prerequisites are met:
1. **Environment Setup**:
   - Python 3.10+ installed.
   - An IDE or code editor (e.g., PyCharm, VS Code) configured for Python development.
   - Necessary Python libraries installed (e.g., NumPy, Pandas) if required for algorithms.
   
   ```bash
   pip install numpy pandas
   ```

2. **Source Code Access**:
   - Full access to the Java repository.
   - Java codebase documentation (if available) for understanding business logic.

3. **Prepared Repository**:
   - A Python repository initialized in Git and ready for development.
   - Folder structure defined for the Python project.

4. **Understanding of Business Requirements**:
   - Clarification on the purpose of each function and algorithm to be migrated.

5. **Dependencies**:
   - Dependencies identified and mapped from Java to Python (e.g., libraries for math, data manipulation, etc.).

---

## **Detailed Implementation Instructions**

### **Task 1: Translate Core Functions**
#### **Step 1.1: Identify Key Functions**
- Locate core business logic functions in the Java codebase. For example:
  ```java
  public int calculateRevenue(int[] sales, int unitPrice) {
      int revenue = 0;
      for (int sale : sales) {
          revenue += sale * unitPrice;
      }
      return revenue;
  }
  ```

#### **Step 1.2: Translate into Python**
- Convert the Java syntax into Python-native syntax, using Python features like list comprehensions for simplicity.
  
**Python Example**:
```python
def calculate_revenue(sales: list[int], unit_price: int) -> int:
    revenue = sum(sale * unit_price for sale in sales)
    return revenue
```

#### **Step 1.3: Ensure Type Compatibility**
- Use Python's type hints (via `typing` module) for function signatures to mirror Java's type safety.

#### **Step 1.4: Comment and Document**
- Add docstrings to each function for clarity:
```python
def calculate_revenue(sales: list[int], unit_price: int) -> int:
    """
    Calculate total revenue based on sales and unit price.

    Args:
        sales (list[int]): List of sales quantities.
        unit_price (int): Price per unit sold.

    Returns:
        int: Total revenue.
    """
    revenue = sum(sale * unit_price for sale in sales)
    return revenue
```

---

### **Task 2: Adapt Data Structures**
#### **Step 2.1: Replace Java-Specific Structures**
Java has data structures like `ArrayList`, `HashMap`, or `LinkedList`. Replace these with Python equivalents:
| Java Structure   | Python Equivalent |
|------------------|-------------------|
| `ArrayList`      | `list`            |
| `HashMap`        | `dict`            |
| `LinkedList`     | `collections.deque` |

#### **Step 2.2: Example Conversion**
**Java Code (Using HashMap)**:
```java
import java.util.HashMap;

public void countOccurrences(String[] words) {
    HashMap<String, Integer> wordCount = new HashMap<>();
    for (String word : words) {
        wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
    }
}
```

**Python Code**:
```python
from collections import Counter

def count_occurrences(words: list[str]) -> dict[str, int]:
    """
    Count occurrences of each word in the given list.

    Args:
        words (list[str]): List of words.

    Returns:
        dict[str, int]: Dictionary with words as keys and their counts as values.
    """
    word_count = Counter(words)
    return dict(word_count)
```

---

### **Task 3: Port Algorithms**
#### **Step 3.1: Understand Algorithm Logic**
Carefully analyze the algorithm and confirm its purpose. Break it into smaller logical chunks if necessary.

#### **Step 3.2: Optimize Using Python**
Python often has more compact ways to express algorithms due to its rich standard library. For example:
**Java Sorting Algorithm**:
```java
import java.util.Arrays;

public int[] sortArray(int[] arr) {
    Arrays.sort(arr);
    return arr;
}
```

**Python Equivalent**:
```python
def sort_array(arr: list[int]) -> list[int]:
    """
    Sort an array in ascending order.

    Args:
        arr (list[int]): Array of integers.

    Returns:
        list[int]: Sorted array.
    """
    return sorted(arr)
```

---

## **Common Pitfalls and How to Avoid Them**
### **Pitfall 1: Type Conversion Issues**
- Java is statically typed; Python is dynamically typed. Ensure inputs are validated and type hints are used properly.
- Use `typing` module for type hints.

### **Pitfall 2: Variable Scope**
- Python's scoping rules differ slightly from Java. Pay attention to global vs local variables.

### **Pitfall 3: Overuse of Loops**
- Avoid directly porting Java loops; use Python's built-in functions (e.g., `map`, `filter`).

### **Pitfall 4: Performance Bottlenecks**
- Be mindful of Python's slower execution speed for heavy computations. Use optimized libraries like NumPy for numerical calculations.

---

## **Testing Checklist**
1. Verify that all migrated functions and algorithms produce identical outputs as their Java counterparts.
2. Ensure edge cases are handled appropriately (e.g., empty lists, null values).
3. Integrate unit tests for each function using a framework like `pytest`.

**Example Unit Test**:
```python
import pytest
from mymodule import calculate_revenue

def test_calculate_revenue():
    assert calculate_revenue([10, 20, 30], 5) == 300
    assert calculate_revenue([], 5) == 0
```

---

## **Validation Criteria**
1. All functions and algorithms are functionally equivalent to Java implementations.
2. The code adheres to Python best practices (PEP 8 compliance, use of Pythonic constructs).
3. Unit tests pass with 100% coverage.
4. Code is reviewed and approved by peers.

---

## **Troubleshooting Guide**
### **Issue: Incorrect Output**
- Double-check algorithm logic after migration. Ensure Python's zero-based indexing is accounted for.

### **Issue: Performance Degradation**
- Profile code using `cProfile` or `timeit`. Optimize using vectorized operations in libraries like NumPy.

### **Issue: Syntax Errors**
- Use linting tools like `flake8` or `pylint` to catch syntax problems early.

---

## **Resources and References**
1. [Python Official Documentation](https://docs.python.org/3/)
2. [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
3. [NumPy Documentation](https://numpy.org/doc/)
4. [Collections Module](https://docs.python.org/3/library/collections.html)

---

## **Next Steps**
- Proceed to Step 4: **Integration and Dependency Mapping**.
- Integrate migrated logic with other components and ensure the application behaves as expected.

---

### **Time Estimate**
- Small functions: 1-2 hours each.
- Complex algorithms: 4-6 hours each.