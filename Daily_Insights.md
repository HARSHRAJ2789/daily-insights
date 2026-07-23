# Daily Coding & Security Notes

A personal collection of snippets, tips, and best practices I am logging for C++, Python, and Cybersecurity.

---




### 2026-07-12 05:15:21
- **C++**: Use `std::array` or `std::vector` over C-style raw arrays for safety and functionality.

### 2026-07-12 05:15:26
- **Python**: Use `*args` and `**kwargs` for flexible function signatures.

### 2026-07-12 09:45:48
- **Security**: Sanitize and validate all user inputs to mitigate XSS and SQL Injection vulnerabilities.

### 2026-07-12 20:37:55
- **Security**: Implement the Principle of Least Privilege (PoLP). Give a process or user only the minimum access necessary.

### 2026-07-13 10:54:24
- **C++**: `auto` type deduction makes code cleaner, especially with complex iterator types.

### 2026-07-13 20:52:51
- **C++**: Avoid using `#include <bits/stdc++.h>` in production code as it slows down compilation and increases binary size.

### 2026-07-14 09:51:25
- **C++**: `auto` type deduction makes code cleaner, especially with complex iterator types.

### 2026-07-14 20:53:56
- **Python**: Use `enumerate()` instead of `range(len())` to iterate over a list and its indices.

### 2026-07-15 09:55:42
- **Python**: Use `*args` and `**kwargs` for flexible function signatures.

### 2026-07-15 20:53:11
- **Python**: Use `enumerate()` instead of `range(len())` to iterate over a list and its indices.

### 2026-07-16 10:02:23
- **Security**: Sanitize and validate all user inputs to mitigate XSS and SQL Injection vulnerabilities.

### 2026-07-16 20:51:32
- **C++**: Prefer `std::array` or `std::vector` over C-style raw arrays for safety and functionality.

### 2026-07-17 09:51:33
- **Python**: Context managers (`with` statement) are the preferred way to handle resource allocation like opening files.

### 2026-07-17 20:46:27
- **Security**: Avoid using MD5 or SHA-1 for cryptography. Use SHA-256 or bcrypt/Argon2 for passwords.

### 2026-07-18 09:18:13
- **Python**: Use `*args` and `**kwargs` for flexible function signatures.

### 2026-07-18 20:40:02
- **Security**: Implement the Principle of Least Privilege (PoLP). Give a process or user only the minimum access necessary.

### 2026-07-19 09:47:04
- **C++**: Use `std::make_unique` and `std::make_shared` instead of bare `new` to prevent memory leaks.

### 2026-07-19 20:39:35
- **Python**: Use `enumerate()` instead of `range(len())` to iterate over a list and its indices.

### 2026-07-20 10:45:27
- **Security**: Sanitize and validate all user inputs to mitigate XSS and SQL Injection vulnerabilities.

### 2026-07-20 21:05:03
- **C++**: Use `std::make_unique` and `std::make_shared` instead of bare `new` to prevent memory leaks.

### 2026-07-21 10:20:41
- **C++**: Avoid using `#include <bits/stdc++.h>` in production code as it slows down compilation and increases binary size.

### 2026-07-21 21:00:30
- **Security**: Always salt your hashes! A cryptographic salt makes rainbow table attacks computationally infeasible.

### 2026-07-22 10:19:58
- **Python**: Use `enumerate()` instead of `range(len())` to iterate over a list and its indices.

### 2026-07-22 20:58:52
- **Security**: Sanitize and validate all user inputs to mitigate XSS and SQL Injection vulnerabilities.

### 2026-07-23 10:14:26
- **C++**: Use ranged-based for loops: `for (const auto& item : container)` for safer and cleaner iteration.

### 2026-07-23 20:55:44
- **C++**: Remember the Rule of Three/Five/Zero for classes managing resources (memory, file handles, etc.).
