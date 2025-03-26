# String Comparison
String comparison in Python means comparing two strings using comparison operators to check their relationship. Python provides several operators for string comparison, including:

`==`, `!=`, `>`, `<`, `>=`, `<=`

## How String Comparison Works

**1. Lexicographical Order:** 
- Python compares strings based on their Unicode (ASCII) values.
- Characters are compared one by one from left to right.
- The comparison stops as soon as it finds a difference.

**2. Case-Sensitive:**
- Lowercase letters have higher Unicode values than uppercase letters (`"a" > "A"`).

**3. Length Matters:**
- If all characters are identical but one string is longer, the longer string is considered greater.
- Example: `"abc" < "abcd"`.
