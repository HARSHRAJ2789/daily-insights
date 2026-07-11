import random
import datetime
import os

# A collection of Python, C++, and Security tips
TIPS = [
    "**Python**: Use `enumerate()` instead of `range(len())` to iterate over a list and its indices.",
    "**C++**: Use `std::make_unique` and `std::make_shared` instead of bare `new` to prevent memory leaks.",
    "**Security**: Always salt your hashes! A cryptographic salt makes rainbow table attacks computationally infeasible.",
    "**Python**: The `collections` module provides specialized container datatypes like `Counter`, `defaultdict`, and `deque`.",
    "**C++**: `const` correctness is a powerful tool. Use `const` for variables, references, and member functions that do not modify state.",
    "**Security**: Never commit secrets or API keys to version control. Use environment variables or a secrets manager.",
    "**Python**: `zip()` is extremely useful for iterating over multiple iterables simultaneously.",
    "**C++**: Remember the Rule of Three/Five/Zero for classes managing resources (memory, file handles, etc.).",
    "**Security**: Implement the Principle of Least Privilege (PoLP). Give a process or user only the minimum access necessary.",
    "**Python**: Context managers (`with` statement) are the preferred way to handle resource allocation like opening files.",
    "**C++**: Prefer `std::array` or `std::vector` over C-style raw arrays for safety and functionality.",
    "**Security**: Sanitize and validate all user inputs to mitigate XSS and SQL Injection vulnerabilities.",
    "**Python**: Use `*args` and `**kwargs` for flexible function signatures.",
    "**C++**: `auto` type deduction makes code cleaner, especially with complex iterator types.",
    "**Security**: Avoid using MD5 or SHA-1 for cryptography. Use SHA-256 or bcrypt/Argon2 for passwords.",
    "**Python**: List comprehensions `[x for x in data if condition]` are often more Pythonic than `map` and `filter`.",
    "**C++**: Use ranged-based for loops: `for (const auto& item : container)` for safer and cleaner iteration.",
    "**Security**: Keep your dependencies updated to patch known vulnerabilities (CVEs).",
    "**Python**: The `itertools` module is a hidden gem for efficient looping constructs.",
    "**C++**: Avoid using `#include <bits/stdc++.h>` in production code as it slows down compilation and increases binary size.",
]

def main():
    tip = random.choice(TIPS)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Ensure we are appending to the markdown file in the current directory
    file_path = "Daily_Insights.md"
    
    with open(file_path, "a") as f:
        f.write(f"### {now}\n")
        f.write(f"- {tip}\n\n")

if __name__ == "__main__":
    main()
