but # Backend Developer Interview Preparation Guide (Fresher Level)
### Set 1: FastAPI / Backend Development (Top 30 Questions)
### Set 2: SQL / Database (Top 30 Questions)
### Set 3: Python Core (Top 30 Questions with Code Examples)

> Answers are written in **simple, fresher-friendly language** — easy to remember and explain confidently in an interview.

---

## SET 1: FASTAPI & BACKEND DEVELOPMENT

### 1. What is FastAPI and why do you use it?
FastAPI is a modern Python web framework used to build APIs quickly. I use it because it's fast (built on Starlette and Pydantic), it auto-generates API documentation (Swagger UI), and it supports async programming, which makes it great for high-performance backend applications.

### 2. What is the difference between FastAPI and Flask/Django?
Flask is a micro-framework with no built-in validation or async support by default. Django is a full-stack framework with built-in ORM, admin panel, etc. FastAPI is lightweight like Flask but supports async natively, has automatic data validation using Pydantic, and auto-generates interactive docs — making it faster to develop and faster in performance.

### 3. What is an API?
API (Application Programming Interface) is a way for two applications to communicate with each other. In backend development, it usually means a set of URLs (endpoints) that let the frontend or other services send/receive data from the server.

### 4. What is a REST API?
REST is an architectural style for building APIs using standard HTTP methods (GET, POST, PUT, DELETE) where each resource is identified by a URL. It's stateless, meaning each request is independent and doesn't depend on previous requests.

### 5. Explain HTTP methods: GET, POST, PUT, PATCH, DELETE.
- **GET** – fetch/read data
- **POST** – create new data
- **PUT** – update/replace full data
- **PATCH** – update partial data
- **DELETE** – remove data

### 6. What is Pydantic and why is it used in FastAPI?
Pydantic is a data validation library. In FastAPI, we use Pydantic models (BaseModel classes) to define the expected structure of request/response data. It automatically validates incoming data types and gives clear errors if something is wrong.

### 7. How do you define a path parameter and a query parameter in FastAPI?
```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
`item_id` is a **path parameter** (part of the URL), `q` is a **query parameter** (comes after `?` in URL, e.g. `?q=test`).

### 8. What is dependency injection in FastAPI?
It's a way to reuse logic (like DB connections, authentication checks) across multiple routes using the `Depends()` function, instead of writing the same code again and again in every endpoint.

### 9. How do you connect FastAPI with a database?
Usually using an ORM like SQLAlchemy or an async driver like `asyncpg`/`databases`. We create a session/engine, define models, and use dependency injection to get a DB session inside each route.

### 10. What is async/await and why does FastAPI use it?
`async`/`await` allows the server to handle other requests while waiting for a slow task (like a DB call or API call) to finish, instead of blocking. This makes FastAPI apps handle many requests concurrently and efficiently.

### 11. What is middleware in FastAPI?
Middleware is code that runs before and after every request, useful for things like logging, adding CORS headers, or authentication checks, without writing that logic in every route.

### 12. What is CORS and how do you handle it in FastAPI?
CORS (Cross-Origin Resource Sharing) is a browser security feature that blocks requests from a different domain/origin than the server. In FastAPI, we handle it using `CORSMiddleware` to allow specific frontend origins to access our API.

### 13. How does FastAPI generate automatic documentation?
FastAPI uses OpenAPI standard and generates docs automatically at `/docs` (Swagger UI) and `/redoc` (ReDoc), based on the type hints and Pydantic models we define in our code.

### 14. What is status code 200, 201, 400, 401, 404, 500? 
- **200** – Success
- **201** – Created successfully
- **400** – Bad Request (client sent wrong data)
- **401** – Unauthorized (not logged in / invalid token)
- **404** – Not Found
- **500** – Internal Server Error (something wrong on server)

### 15. How do you handle exceptions/errors in FastAPI?
Using `HTTPException` from FastAPI:
```python
from fastapi import HTTPException
raise HTTPException(status_code=404, detail="Item not found")
```
We can also write custom exception handlers using `@app.exception_handler()`.

### 16. What is JWT authentication and how would you implement it in FastAPI?
JWT (JSON Web Token) is a token-based authentication method. After login, the server generates a signed token containing user info, and the client sends this token in the `Authorization` header on future requests. FastAPI verifies the token before allowing access to protected routes.

### 17. What is the difference between synchronous and asynchronous code?
Synchronous code runs one task at a time — each task waits for the previous one to finish. Asynchronous code can start a task, move to another task while waiting, and come back later — better for I/O-heavy operations like DB or API calls.

### 18. What are Pydantic BaseModel and its use in request/response validation?
`BaseModel` is a Pydantic class we inherit to define the shape of our data (fields and types). FastAPI uses it to automatically validate incoming JSON requests and to format outgoing JSON responses.

### 19. What is Uvicorn/Gunicorn and why do we need it?
Uvicorn is an ASGI server used to actually run our FastAPI app (FastAPI itself is just a framework, not a server). Gunicorn is often used with Uvicorn workers in production to manage multiple worker processes for better performance.

### 20. What is the difference between PUT and PATCH?
PUT replaces the entire resource with new data (you must send all fields). PATCH updates only the specific fields you send, leaving the rest unchanged.

### 21. How do you handle file uploads in FastAPI?
Using `UploadFile` and `File`:
```python
from fastapi import File, UploadFile
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
```

### 22. What is idempotency in APIs?
An idempotent operation gives the same result no matter how many times you call it. GET, PUT, DELETE are idempotent. POST is generally not idempotent because it usually creates a new resource each time.

### 23. What is environment variable management and why is it important?
We store sensitive data (DB passwords, API keys) in `.env` files instead of hardcoding them in code. In FastAPI, we often use `python-dotenv` or Pydantic's `BaseSettings` to load these safely.

### 24. What is the difference between a monolithic and microservices architecture?
Monolithic means the whole application (all features) runs as a single unit/codebase. Microservices means breaking the application into small, independent services (e.g., user service, order service) that communicate over APIs.

### 25. What is caching and how can it improve backend performance?
Caching means storing frequently accessed data temporarily (like in Redis) so we don't have to query the database every time, which reduces response time and database load.

### 26. What is rate limiting and why is it used?
Rate limiting restricts how many requests a user/IP can make in a given time period, to prevent abuse, protect the server from overload, and stop DDoS-type attacks.

### 27. How do you test FastAPI applications?
Using `TestClient` from `fastapi.testclient` (built on `httpx`), we can write unit tests that simulate API calls without running a real server:
```python
from fastapi.testclient import TestClient
client = TestClient(app)
response = client.get("/items/1")
```

### 28. What is the role of `__init__.py` and project structure in a Python backend project?
`__init__.py` marks a folder as a Python package so it can be imported as a module. A clean project structure (routers, models, schemas, services, database folders) keeps large FastAPI apps organized and maintainable.

### 29. What is the difference between authentication and authorization?
Authentication verifies **who you are** (login with username/password). Authorization decides **what you're allowed to do** (like admin vs normal user permissions) after you're authenticated.

### 30. How would you deploy a FastAPI application to production?
Typical steps: use Uvicorn/Gunicorn as the server, put it behind Nginx as a reverse proxy, containerize with Docker, store secrets in environment variables, and deploy to a cloud platform (AWS/Render/Railway/Azure) with CI/CD for automated deployment.

---------------------------------------------------------------------------------------------------------------------------------------

## SET 2: SQL & DATABASE
### 1. What is a Primary Key?
A column (or set of columns) that uniquely identifies each row in a table. It cannot have NULL values and must be unique.

### 2. What is a Foreign Key?
A column that creates a link between two tables by referring to the Primary Key of another table. It's used to maintain referential integrity between related tables.

### 3. What is the difference between SQL and NoSQL databases?
SQL databases (MySQL, PostgreSQL) store data in structured tables with fixed schema and relationships. NoSQL databases (MongoDB, Redis) store data in flexible formats like documents/key-value pairs, and don't require a fixed schema — good for unstructured or fast-changing data.

### 4. What is normalization? Explain 1NF, 2NF, 3NF briefly.
Normalization is organizing data to reduce redundancy.
- **1NF** – each column has atomic (single) values, no repeating groups.
- **2NF** – 1NF + no partial dependency (non-key columns depend on the whole primary key).
- **3NF** – 2NF + no transitive dependency (non-key columns depend only on the primary key, not on other non-key columns).

### 5. What is denormalization and when would you use it?
Denormalization means intentionally adding redundant data to reduce the number of joins and improve read performance — used in reporting/analytics systems where read speed matters more than storage efficiency.

### 6. What is a JOIN? Explain types of joins.
JOIN combines rows from two or more tables based on a related column.
- **INNER JOIN** – only matching rows in both tables
- **LEFT JOIN** – all rows from left table + matching from right (NULL if no match)
- **RIGHT JOIN** – all rows from right table + matching from left
- **FULL JOIN** – all rows from both tables, matched where possible

### 7. What is the difference between WHERE and HAVING?
`WHERE` filters rows **before** grouping (used with individual rows). `HAVING` filters groups **after** the `GROUP BY` clause is applied (used with aggregate functions like COUNT, SUM).

### 8. What is an index and why is it used?
An index is a data structure that speeds up data retrieval on a table, similar to a book's index. It makes SELECT queries faster but can slow down INSERT/UPDATE slightly because the index also needs updating.

### 9. What is the difference between DELETE, TRUNCATE, and DROP?
- **DELETE** – removes specific rows (can use WHERE), can be rolled back, slower.
- **TRUNCATE** – removes all rows at once, faster, resets identity, can't use WHERE.
- **DROP** – removes the entire table structure along with data.

### 10. What is a Primary Key vs Unique Key?
Primary Key: only one per table, doesn't allow NULL. Unique Key: can have multiple per table, allows one NULL value (in most databases). Both ensure uniqueness.

### 11. What are aggregate functions in SQL?
Functions that perform a calculation on multiple rows and return a single value. Examples: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.

### 12. What is GROUP BY used for?
It groups rows that have the same values in specified columns into summary rows, often used with aggregate functions — e.g., total sales per customer.

### 13. What is a subquery?
A query nested inside another query, used to get intermediate results.
```sql
SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
```

### 14. What is the difference between a subquery and a JOIN?
A JOIN combines columns from multiple tables into one result set directly. A subquery runs a separate query first, and its result is used inside the outer query — sometimes JOINs are more efficient, but subqueries can be easier to read for certain cases.

### 15. What are SQL constraints?
Rules applied to table columns to maintain data accuracy: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `DEFAULT`.

### 16. What is ACID property in databases?
- **Atomicity** – transaction is all-or-nothing
- **Consistency** – data remains valid before/after transaction
- **Isolation** – concurrent transactions don't interfere with each other
- **Durability** – once committed, data is permanently saved even after a crash

### 17. What is a transaction in SQL?
A group of one or more SQL statements executed as a single unit — either all statements succeed (COMMIT) or none do (ROLLBACK), ensuring data integrity.

### 18. What is the difference between COMMIT and ROLLBACK?
`COMMIT` saves all changes made in the current transaction permanently. `ROLLBACK` undoes changes made in the current transaction if something goes wrong.

### 19. What is a stored procedure?
A precompiled set of SQL statements saved in the database that can be executed as a single call, useful for reusing complex logic and improving performance.

### 20. What is the difference between clustered and non-clustered index?
A **clustered index** physically sorts and stores table data in the order of the index (only one per table, usually the primary key). A **non-clustered index** creates a separate structure that points to the actual data (multiple allowed per table).

### 21. What is a view in SQL?
A virtual table created from the result of a SQL query. It doesn't store data itself but shows data from one or more tables, useful for simplifying complex queries.

### 22. What is the difference between UNION and UNION ALL?
`UNION` combines results of two queries and removes duplicate rows. `UNION ALL` combines results but keeps duplicates, making it faster since no duplicate check is done.

### 23. What is database normalization vs indexing — do they conflict?
Normalization is about organizing data to avoid redundancy, while indexing is about improving query speed. They don't conflict directly, but over-normalization can require more JOINs, and adding many indexes can slow down writes — so it's a balance based on the use case.

### 24. What is a composite key?
A primary key made up of two or more columns combined together to uniquely identify a row, used when no single column is unique enough on its own.

### 25. Explain the difference between `INNER JOIN` and `SELF JOIN`.
INNER JOIN combines rows from two different tables based on a condition. SELF JOIN is when a table is joined with itself, useful for comparing rows within the same table (e.g., finding employees and their managers in the same table).

### 26. What is SQL Injection and how do you prevent it?
SQL Injection is a security attack where malicious SQL code is inserted into input fields to manipulate the database. We prevent it by using parameterized queries/prepared statements (like SQLAlchemy ORM does automatically) instead of directly concatenating user input into SQL strings.

### 27. What is the difference between `HAVING` and aggregate functions used directly in `WHERE`?
You **cannot** use aggregate functions (like `SUM()`, `COUNT()`) directly in `WHERE` because `WHERE` executes before grouping happens. That's why `HAVING` exists — to filter after aggregation/grouping is done.

### 28. What is database sharding?
Sharding is splitting a large database into smaller, faster, more manageable pieces called "shards," often distributed across multiple servers, used to scale databases horizontally for large applications.

### 29. What is the difference between OLTP and OLAP?
**OLTP** (Online Transaction Processing) handles day-to-day transactional operations (like inserting an order) — fast, small transactions. **OLAP** (Online Analytical Processing) is used for complex analysis/reporting on large historical data (like sales trends).

### 30. How do you optimize a slow SQL query?
Common approaches: add proper indexes on frequently filtered/joined columns, avoid `SELECT *` (select only needed columns), avoid unnecessary subqueries, use `EXPLAIN`/`EXPLAIN ANALYZE` to check the query execution plan, and rewrite complex queries or add caching where possible.

---------------------------------------------------------------------------------------------------------------------------------------

## SET 3: PYTHON CORE (WITH CODE EXAMPLES)
### 1. What is the difference between list and tuple?
List is mutable (can change after creation), tuple is immutable (can't change once created). Lists use `[]`, tuples use `()`.
```python
my_list = [1, 2, 3]
my_list.append(4)      # works fine

my_tuple = (1, 2, 3)
my_tuple[0] = 5         # Error: tuple doesn't support item assignment
```

### 2. What is the difference between `is` and `==`?
`==` checks if values are equal. `is` checks if both variables point to the exact same object in memory.
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True (same values)
print(a is b)   # False (different objects in memory)
```

### 3. What are mutable and immutable data types?
Mutable = can be changed after creation (list, dict, set). Immutable = cannot be changed (int, str, tuple, frozenset).
```python
s = "hello"
s[0] = "H"     # Error, strings are immutable
s = "Hello"    # this creates a new string object instead
```

### 4. What is the difference between `*args` and `**kwargs`?
`*args` lets a function accept any number of positional arguments (as a tuple). `**kwargs` lets it accept any number of keyword arguments (as a dictionary).
```python
def demo(*args, **kwargs):
    print(args)     # (1, 2, 3)
    print(kwargs)   # {'name': 'Raj', 'age': 22}

demo(1, 2, 3, name="Raj", age=22)
```

### 5. What are Python decorators?
A decorator is a function that wraps another function to add extra functionality without changing its original code.
```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function runs
# Hello!
# After function runs
```

### 6. What are Python generators? Why use `yield`?
A generator is a function that returns values one at a time using `yield`, instead of returning all values at once. It saves memory since values are generated on the fly (lazy evaluation).
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)   # 1 2 3 4 5 one by one
```

### 7. What is the difference between `yield` and `return`?
`return` ends the function and sends back one final value. `yield` pauses the function, sends a value, and remembers where it left off — so the function can continue from there next time it's called.

### 8. What are list comprehensions?
A short, readable way to create lists in a single line.
```python
squares = [x*x for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# with condition
even = [x for x in range(10) if x % 2 == 0]
print(even)      # [0, 2, 4, 6, 8]
```

### 9. What is a lambda function?
A small, anonymous (nameless) function defined using the `lambda` keyword, used for short, one-line operations.
```python
add = lambda a, b: a + b
print(add(3, 5))   # 8

# common use with map/filter
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums))
print(squared)    # [1, 4, 9, 16]
```

### 10. What is the difference between `map()`, `filter()`, and `reduce()`?
- **map()** – applies a function to every item in a list
- **filter()** – keeps only items that satisfy a condition
- **reduce()** – combines all items into a single value (needs `functools`)
```python
from functools import reduce
nums = [1, 2, 3, 4]

print(list(map(lambda x: x*2, nums)))          # [2, 4, 6, 8]
print(list(filter(lambda x: x % 2 == 0, nums))) # [2, 4]
print(reduce(lambda a, b: a + b, nums))         # 10
```

### 11. What are `*args` unpacking and list unpacking?
```python
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)   # 1 2 [3, 4, 5]

def total(*nums):
    return sum(nums)
print(total(1, 2, 3))   # 6
```

### 12. What is the difference between `deepcopy()` and `copy()`?
`copy()` creates a shallow copy (copies the outer object, but nested objects still point to the same reference). `deepcopy()` copies everything fully, including nested objects.
```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 100
print(original)  # [[100, 2], [3, 4]] -> affected because shallow copy

deep[0][0] = 999
print(original)  # unaffected, deep copy is fully independent
```

### 13. What is exception handling in Python? (try/except)
Used to handle runtime errors gracefully instead of crashing the program.
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("This always runs")
```

### 14. What is the difference between `except Exception` and a specific exception?
A specific exception (like `ValueError`) catches only that particular error type. `except Exception` catches almost any error — it's less precise and can hide bugs, so it's better to catch specific exceptions when possible.

### 15. What are Python's data types?
Common built-in types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, `frozenset`, `NoneType`.

### 16. What is the difference between a shallow list copy using `[:]` and `=`?
Using `=` just creates another reference to the same list (both point to same memory). Using `[:]` (or `.copy()`) creates a new list object with same values.
```python
a = [1, 2, 3]
b = a          # b is same object as a
c = a[:]       # c is a new copy

b.append(4)
print(a)  # [1, 2, 3, 4] -> changed because b is same object
print(c)  # [1, 2, 3]   -> unaffected, it's a separate copy
```

### 17. What is a dictionary and how do you iterate over it?
A dictionary stores data as key-value pairs.
```python
person = {"name": "Raj", "age": 22}

for key, value in person.items():
    print(key, value)
# name Raj
# age 22
```

### 18. What is the difference between `dict.get()` and `dict[key]`?
`dict[key]` throws a `KeyError` if the key doesn't exist. `dict.get(key)` returns `None` (or a default value you specify) instead of crashing.
```python
person = {"name": "Raj"}
print(person.get("age", "Not Found"))   # Not Found
print(person["age"])                    # KeyError
```

### 19. What are Python sets and why are they used?
A set stores unique, unordered values — automatically removes duplicates, and is useful for membership tests and set operations (union, intersection).
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # union {1, 2, 3, 4}
print(a & b)   # intersection {2, 3}
```

### 20. What is `__init__` method in Python classes?
It's the constructor method, automatically called when a new object is created, used to initialize the object's attributes.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Raj", 22)
print(p1.name)   # Raj
```

### 21. What is the difference between class variables and instance variables?
Class variables are shared across all objects of a class. Instance variables are unique to each object.
```python
class Employee:
    company = "TechCorp"     # class variable

    def __init__(self, name):
        self.name = name      # instance variable

e1 = Employee("Raj")
e2 = Employee("Priya")
print(e1.company, e2.company)   # TechCorp TechCorp (shared)
print(e1.name, e2.name)         # Raj Priya (unique)
```

### 22. What is inheritance in Python? (OOP concept)
Inheritance lets a class (child) reuse the properties and methods of another class (parent).
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # Animal speaks (inherited)
d.bark()    # Dog barks
```

### 23. What is polymorphism in Python?
Polymorphism means the same method name  but behaves differently for different classes/objects.
```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

for animal in [Cat(), Dog()]:
    animal.sound()   # Meow, Woof
```

### 24. What is encapsulation in Python?
Encapsulation means restricting direct access to some of an object's data using private/protected variables (using `_` or `__` prefix), exposing only what's necessary.
```python
class Account:
    def __init__(self, balance):
        self.__balance = balance    # private variable

    def get_balance(self):
        return self.__balance

acc = Account(1000)
print(acc.get_balance())   # 1000
# print(acc.__balance)     # Error: not directly accessible
```

### 25. What is the difference between `@staticmethod` and `@classmethod`?
`@staticmethod` doesn't access class or instance data — behaves like a regular function inside a class. `@classmethod` receives the class itself (`cls`) as the first argument, and can access/modify class-level data.
```python
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def class_name(cls):
        return cls.__name__

print(MathUtil.add(2, 3))        # 5
print(MathUtil.class_name())     # MathUtil
```

### 26. What is the difference between `__str__` and `__repr__`?
`__str__` gives a readable, user-friendly string representation of an object (used with `print()`). `__repr__` gives a detailed, developer-focused representation, often used for debugging.
```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"

p = Person("Raj")
print(p)     # Person: Raj (calls __str__)
```

### 27. What is GIL (Global Interpreter Lock) in Python?
GIL is a lock that allows only one thread to execute Python code at a time, even on multi-core systems. This means Python threads aren't great for CPU-heavy tasks, but multiprocessing or async can be used instead for better performance.

### 28. What is the difference between multithreading and multiprocessing in Python?
Multithreading runs multiple threads within the same process (good for I/O-bound tasks like file/network operations, but limited by GIL). Multiprocessing runs separate processes with their own memory (good for CPU-heavy tasks since it bypasses the GIL).

### 29. What are Python modules and packages?
A module is a single `.py` file containing functions/classes. A package is a folder containing multiple modules along with an `__init__.py` file, used to organize larger codebases.
```python
# math_utils.py (module)
def add(a, b):
    return a + b

# main.py
from math_utils import add
print(add(2, 3))   # 5
```

### 30. What is the difference between `range()` and a list?
`range()` generates numbers lazily (one at a time, memory-efficient) and doesn't store all values in memory. A list stores all its values in memory at once.
```python
r = range(5)          # doesn't create [0,1,2,3,4] immediately in memory
l = list(range(5))    # [0, 1, 2, 3, 4] -> actual list created in memory
```

---------------------------------------------------------------------------------------------------------------------------------------
## Advanced Interview Questions For Python & DSA
---------------------------------------------------------------------------------------------------------------------------------------
### PART 1: PYTHON - TOP 50 QUESTIONS WITH ANSWERS
## Section 1: Python Basics (Q1-10)

### Q1: What is Python? Why use it?
**Answer:**
Python is a high-level, interpreted programming language that emphasizes code readability and simplicity. It's easy to learn because:
- English-like syntax (readable code)
- Strong community and libraries
- Works across all platforms (Windows, Mac, Linux)
- Great for beginners and large projects

**Why companies use it:**
- Fast development (less code, more functionality)
- Strong in data science, web development, automation
- Excellent for prototyping
- Large ecosystem (NumPy, Pandas, Flask, Django)

**Simple example:**
```python
# Python is simple and readable
name = "Alice"
age = 25
print(f"Hello {name}, you are {age} years old")
# Output: Hello Alice, you are 25 years old
```


### Q2: What is the difference between Python 2 and Python 3?
**Answer:**
| Feature | Python 2 | Python 3 |
|---------|----------|----------|
| Print | `print "hello"` | `print("hello")` |
| Division | `5/2 = 2` (integer) | `5/2 = 2.5` (float) |
| Strings | Unicode default issues | Full Unicode support |
| End of life | Ended 2020 | Still active |
| Library support | Older libraries | Newer, better libraries |

**For interviews:** Always say you use Python 3. Python 2 is dead.



### Q3: Explain mutable vs immutable objects in Python
**Answer:**

**Immutable (cannot change after creation):**
- int, float, string, tuple, frozenset, bool
- Once created, you cannot modify them
- Creating a "new" version creates a new object

```python
# Immutable example
name = "Alice"
name_new = name.replace("A", "B")  # Creates NEW string "Blice"
print(name)      # Still "Alice" - original unchanged
print(name_new)  # "Blice"
```

**Mutable (can change after creation):**
- list, dict, set, bytearray
- You can modify contents without creating new object

```python
# Mutable example
fruits = ["apple", "banana"]
fruits[0] = "orange"  # Changes EXISTING list
fruits.append("grape") # Modifies in place
print(fruits)  # ["orange", "banana", "grape"]
```

**Why it matters:**
- Immutable objects are safer in multi-threaded code
- Mutable objects are faster for modifications
- Immutable can be dictionary keys, mutable cannot


### Q4: What is a decorator in Python?
**Answer:**
A decorator is a function that modifies another function or class without changing its source code. It wraps a function and enhances it.

**Real-world analogy:** A decorator is like putting a frame around a painting—it doesn't change the painting, but enhances how it looks.

```python
# Simple decorator example
def greet_decorator(func):
    def wrapper(name):
        print("--- Welcome ---")
        result = func(name)  # Call original function
        print("--- Goodbye ---")
        return result
    return wrapper

@greet_decorator  # @ symbol applies the decorator
def greet(name):
    print(f"Hello {name}")

greet("Alice")
# Output:
# --- Welcome ---
# Hello Alice
# --- Goodbye ---
```

**Real use case in ThoughtWorks interview:** You might see decorators used for:
- Timing how long a function takes
- Logging function calls
- Authentication checks
- Caching results

---

### Q5: What is a generator in Python?
**Answer:**
A generator is a function that returns values one at a time using `yield` instead of `return`. It's memory efficient because it doesn't create entire list in memory.

```python
# Regular function - creates entire list in memory
def get_numbers_list():
    numbers = []
    for i in range(1000000):
        numbers.append(i)
    return numbers

# Generator - creates one number at a time
def get_numbers_generator():
    for i in range(1000000):
        yield i  # Pauses here, returns i, waits for next()

# Using generator
gen = get_numbers_generator()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# Or loop through it
for num in gen:
    if num > 5:
        break
    print(num)  # Prints 0, 1, 2, 3, 4, 5
```

**Advantage:** Uses WAY less memory. List with 1M numbers = 100+ MB. Generator = nearly 0 MB.

**When to use:** Reading large files, infinite sequences, or data pipelines.

---

### Q6: What is lambda in Python?
**Answer:**
Lambda is a way to create small anonymous functions (functions without a name) in one line.

**Syntax:** `lambda arguments: expression`

```python
# Regular function
def add(a, b):
    return a + b

# Same thing as lambda
add_lambda = lambda a, b: a + b
print(add_lambda(5, 3))  # Output: 8

# Common use: with map(), filter(), sorted()
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Sort by absolute value
numbers = [-3, 1, -2, 4]
sorted_nums = sorted(numbers, key=lambda x: abs(x))
print(sorted_nums)  # [1, -2, -3, 4]
```

**When to use:** Simple one-time operations. For complex logic, use regular functions (more readable).

---

### Q7: Explain list comprehension
**Answer:**
List comprehension is a concise way to create lists. It's more readable and faster than using loops.

```python
# Old way with loop
numbers = []
for i in range(5):
    numbers.append(i * 2)
print(numbers)  # [0, 2, 4, 6, 8]

# List comprehension - same result, one line
numbers = [i * 2 for i in range(5)]
print(numbers)  # [0, 2, 4, 6, 8]

# With condition
numbers = [i * 2 for i in range(5) if i % 2 == 0]
print(numbers)  # [0, 4, 8]

# Nested (harder to read though)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Also exists for dicts and sets:**
```python
# Dictionary comprehension
squares_dict = {i: i**2 for i in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_squares = {i**2 for i in [1, 2, 2, 3, 3, 3]}
print(unique_squares)  # {1, 4, 9}
```


### Q8: What is the difference between == and is?
**Answer:**
- **==** checks if VALUES are equal
- **is** checks if they are the SAME OBJECT in memory

```python
# == vs is
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (values are same)
print(a is b)   # False (different objects in memory)
print(a is c)   # True (c points to same object as a)

# With numbers (Python caches small integers -5 to 256)
x = 5
y = 5
print(x == y)   # True
print(x is y)   # True (Python optimization)

x = 257
y = 257
print(x == y)   # True
print(x is y)   # False (different objects)
```

**Real use case:**
```python
# Checking if something is None
value = None
if value is None:  # Correct way
    print("Value is None")

if value == None:  # Works but not Pythonic
    print("Value is None")
```

**For ThoughtWorks:** Use `is None`, `is True`, `is False` for identity checks. Use `==` for value comparisons.

---

### Q9: What is a virtual environment and why use it?
**Answer:**
A virtual environment is an isolated Python environment for each project. It lets you install different package versions for different projects without conflicts.

**Real scenario:**
- Project A needs Django 2.0
- Project B needs Django 3.0
- Without virtual environments, you can only install one version globally → conflicts!
- With virtual environments, each project gets its own isolated environment

**How to use:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Linux/Mac
myenv\Scripts\activate     # On Windows

# Install packages (only in this environment)
pip install django flask

# See installed packages
pip list

# Save dependencies to file
pip freeze > requirements.txt

# Later, someone else can install same packages
pip install -r requirements.txt

# Deactivate when done
deactivate
```

**Why ThoughtWorks cares:**
- Clean code = clean environments
- Reproducible builds
- Easy collaboration (everyone has same dependencies)


### Q10: What is *args and **kwargs?
**Answer:**
They allow functions to accept variable number of arguments.

- **\*args**: Accept any number of positional arguments as a tuple
- **\*\*kwargs**: Accept any number of keyword arguments as a dictionary

```python
# *args example
def print_all(*args):
    for arg in args:
        print(arg)

print_all(1, 2, 3, "hello", 4.5)
# Output:
# 1
# 2
# 3
# hello
# 4.5

# **kwargs example
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Alice", age=25, city="Mumbai")
# Output:
# name = Alice
# age = 25
# city = Mumbai

# Combined
def full_function(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

full_function(1, 2, 3, 4, name="Alice", age=25)
# Output:
# a=1, b=2
# args=(3, 4)
# kwargs={'name': 'Alice', 'age': 25}
```

**Real use case:**
```python
# Building flexible functions
def connect_database(*args, **kwargs):
    host = kwargs.get('host', 'localhost')
    port = kwargs.get('port', 5432)
    user = kwargs.get('user', 'admin')
    # ... connect using these values
```

---
## Section 2: Object-Oriented Programming (Q11-20)

### Q11: What is a class and object in Python?
**Answer:**
- **Class**: Blueprint for creating objects (like a cookie cutter)
- **Object**: Instance of a class (like the cookie made from the cutter)

```python
# Class definition
class Car:
    def __init__(self, brand, color):  # Constructor
        self.brand = brand  # Attribute
        self.color = color
    
    def describe(self):  # Method
        return f"This is a {self.color} {self.brand}"

# Creating objects (instances)
car1 = Car("Toyota", "red")
car2 = Car("Honda", "blue")

print(car1.describe())  # "This is a red Toyota"
print(car2.describe())  # "This is a blue Honda"
```

**Key concepts:**
- `__init__`: Constructor - runs when object is created
- `self`: Reference to the object itself
- Methods: Functions inside a class
- Attributes: Variables inside a class

---

### Q12: What is inheritance?
**Answer:**
Inheritance allows a class to inherit properties and methods from another class.

**Parent class** (base class) → **Child class** (derived class)

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child classes inherit from Animal
class Dog(Animal):
    def speak(self):  # Override parent method
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):  # Override parent method
        return f"{self.name} says Meow!"

# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # "Buddy says Woof!"
print(cat.speak())  # "Whiskers says Meow!"
```

**Benefits:**
- Code reuse (don't repeat common code)
- Organized structure
- Easy to maintain and extend

---

### Q13: What is polymorphism?
**Answer:**
Polymorphism means "many forms". Same method name, different behavior based on object type.

```python
# Different classes with same method name
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

# Polymorphism - same function works with different objects
def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
cow = Cow()

print(animal_sound(dog))   # "Woof!"
print(animal_sound(cat))   # "Meow!"
print(animal_sound(cow))   # "Moo!"

# Or loop through different animals
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())
```

---

### Q14: What is encapsulation?
**Answer:**
Encapsulation means hiding internal details and only exposing necessary information. It uses public, protected, and private attributes.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private (__ means private)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. Balance: {self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Balance: {self.__balance}"
        return "Insufficient balance"
    
    def get_balance(self):
        return self.__balance

# Using encapsulated class
account = BankAccount(1000)
print(account.deposit(500))      # "Deposited 500. Balance: 1500"
print(account.withdraw(200))     # "Withdrew 200. Balance: 1300"
print(account.get_balance())     # 1300

# Can't directly access private variable
print(account.__balance)  # Error! Cannot access private variable
```

**Benefits:**
- Data protection (can't accidentally modify)
- Control through methods (validation)
- Easy to change internal logic without affecting external code

---

### Q15: What is abstraction?
**Answer:**
Abstraction means showing only essential features and hiding complexity. User doesn't need to know how it works internally.

```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Child classes must implement abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Using abstractions
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
```

**Benefits:**
- Reduces complexity
- Forces consistent interface
- Easy to extend with new shapes

---

### Q16: What is super() function?
**Answer:**
`super()` allows child class to call methods from parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed
    
    def speak(self):
        parent_speak = super().speak()  # Call parent's speak()
        return f"{parent_speak} and is a {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())
# "Buddy makes a sound and is a Golden Retriever"
```

---

### Q17: What is static method and class method?
**Answer:**

**Static method:** Doesn't depend on instance or class. Use with `@staticmethod`

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Call without creating instance
print(MathUtils.add(5, 3))        # 8
print(MathUtils.multiply(5, 3))   # 15
```

**Class method:** Works with the class itself, not instance. Use with `@classmethod`

```python
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def reset_count(cls):
        cls.count = 0

c1 = Counter()
c2 = Counter()
print(Counter.get_count())  # 2
Counter.reset_count()
print(Counter.get_count())  # 0
```

**Difference:**
| | Static Method | Class Method | Instance Method |
|---|---|---|---|
| Access | No access to instance/class | Access to class (cls) | Access to instance (self) |
| Use case | Utility functions | Factory methods, class data | Object behavior |

---

### Q18: What is property decorator?
**Answer:**
Property decorator lets you define getter/setter methods for attributes, making code cleaner.

```python
class Person:
    def __init__(self, age):
        self._age = age  # _ indicates "internal"
    
    @property  # Getter
    def age(self):
        return self._age
    
    @age.setter  # Setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value
    
    @age.deleter  # Deleter
    def age(self):
        del self._age

# Using property
person = Person(25)
print(person.age)      # 25 (calls getter)
person.age = 30        # Sets age (calls setter)
print(person.age)      # 30
del person.age         # Deletes (calls deleter)
```

**Benefits:**
- Looks like simple attribute access but runs code
- Can add validation
- Easy to refactor later

---

### Q19: What is method overriding?
**Answer:**
Method overriding occurs when child class defines a method that already exists in parent class.

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):  # Override parent's greet
        return "Hello from Child"

child = Child()
print(child.greet())   # "Hello from Child" (child's version called)

# You can also use super() to call parent's method
class ChildWithSuper(Parent):
    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} and Child"

child2 = ChildWithSuper()
print(child2.greet())  # "Hello from Parent and Child"
```

---

### Q20: What is method overloading? Does Python support it?
**Answer:**
Method overloading = Same method name with different parameters. 

**Python doesn't support traditional overloading** (unlike Java), but you can achieve similar effect with default arguments or *args:

```python
# Python way - using default arguments
class Calculator:
    def add(self, a, b, c=0):  # c is optional
        return a + b + c

calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.add(5, 3, 2))     # 10

# Alternative - using *args
class Adder:
    def add(self, *args):
        return sum(args)

adder = Adder()
print(adder.add(1, 2))           # 3
print(adder.add(1, 2, 3, 4, 5))  # 15

# Last method wins (Python behavior)
class Example:
    def method(self, a, b):
        return a + b
    
    def method(self, a, b, c):  # Overwrites previous definition
        return a + b + c

ex = Example()
print(ex.method(1, 2, 3))  # Works
print(ex.method(1, 2))     # Error! First definition lost
```

---

## Section 3: Exception Handling & File Operations (Q21-30)

### Q21: What are exceptions? How to handle them?
**Answer:**
Exceptions are errors that occur during program execution. Proper handling prevents program crashes.

```python
# Try-except block
try:
    num = int("abc")  # Error: cannot convert "abc" to int
except ValueError:
    print("Error: Please enter a valid number")

# Multiple exceptions
try:
    file = open("nonexistent.txt")
    num = int(file.read())
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid number format")
except Exception as e:  # Catch any exception
    print(f"Unexpected error: {e}")

# Else clause (runs if no exception)
try:
    num = int("25")
except ValueError:
    print("Invalid number")
else:
    print(f"Number is {num}")  # Runs because no error

# Finally clause (always runs)
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always closes file, even if error occurs
```

**Common exceptions:**
- `ValueError`: Wrong data type
- `TypeError`: Wrong type for operation
- `KeyError`: Key not found in dictionary
- `IndexError`: Index out of range
- `FileNotFoundError`: File doesn't exist
- `ZeroDivisionError`: Division by zero

---

### Q22: How to create custom exceptions?
**Answer:**
Create custom exception by inheriting from `Exception` class.

```python
# Custom exception
class InsufficientBalanceError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

# Using custom exceptions
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Amount cannot be negative")
        if amount > self.balance:
            raise InsufficientBalanceError(f"Balance is only {self.balance}")
        self.balance -= amount
        return self.balance

# Using the class
account = BankAccount(1000)
try:
    account.withdraw(500)
except NegativeAmountError as e:
    print(f"Error: {e}")
except InsufficientBalanceError as e:
    print(f"Error: {e}")
```

---

### Q23: What is assert statement?
**Answer:**
`assert` checks if a condition is true. If false, raises AssertionError.

```python
# Simple assert
age = 25
assert age >= 18, "Must be 18 or older"  # Passes
assert age < 20, "Must be under 20"      # Fails! Raises AssertionError

# In functions
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

print(divide(10, 2))   # 5
print(divide(10, 0))   # AssertionError: Divisor cannot be zero

# Useful for catching programmer errors during development
def set_age(age):
    assert isinstance(age, int), "Age must be integer"
    assert age > 0, "Age must be positive"
    self.age = age
```

---

### Q24: How to work with files in Python?
**Answer:**
Three ways to open files: old way, context manager (recommended).

```python
# Old way (need to remember to close)
file = open("data.txt", "r")
content = file.read()
file.close()

# Context manager (recommended - auto closes)
with open("data.txt", "r") as file:
    content = file.read()
# File auto-closes after with block

# Different modes
# "r" - read (default)
# "w" - write (overwrites)
# "a" - append (add to end)
# "x" - create
# "b" - binary

# Read file
with open("data.txt", "r") as file:
    content = file.read()          # Read entire file
    lines = file.readlines()       # Read as list of lines
    line = file.readline()         # Read one line

# Write to file
with open("output.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Python is great")

# Append to file
with open("output.txt", "a") as file:
    file.write("\nAdded more text")

# Read line by line (memory efficient)
with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip())  # Process one line at a time
```

---

### Q25: What is the difference between read(), readline(), readlines()?
**Answer:**

```python
# File content:
# Line 1
# Line 2
# Line 3

# read() - returns entire file as ONE string
with open("file.txt", "r") as f:
    content = f.read()
print(repr(content))
# Output: 'Line 1\nLine 2\nLine 3\n'

# readline() - returns ONE line (with \n at end)
with open("file.txt", "r") as f:
    line1 = f.readline()  # "Line 1\n"
    line2 = f.readline()  # "Line 2\n"
print(repr(line1))  # Output: 'Line 1\n'

# readlines() - returns list of ALL lines
with open("file.txt", "r") as f:
    lines = f.readlines()
print(lines)
# Output: ['Line 1\n', 'Line 2\n', 'Line 3\n']

# Looping (most efficient for large files)
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())  # Strip removes \n
```

**Summary:**
| Method | Returns | Size |
|--------|---------|------|
| read() | One big string | All at once |
| readline() | One line | One by one |
| readlines() | List of lines | All as list |
| Loop `for line in file` | One line | Iterator (most efficient) |

---

## Section 4: Built-in Functions & Data Structures (Q26-40)

### Q26: Explain map(), filter(), reduce()
**Answer:**

**map()**: Apply function to every item in iterable

```python
numbers = [1, 2, 3, 4, 5]

# Old way
squared = []
for num in numbers:
    squared.append(num ** 2)

# Using map()
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# With regular function
def double(x):
    return x * 2
doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

**filter()**: Keep only items where function returns True

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# With function
def is_positive(x):
    return x > 0
positives = list(filter(is_positive, [-2, -1, 0, 1, 2]))
print(positives)  # [1, 2]
```

**reduce()**: Accumulate values into single result (need to import)

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Multiply all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# More readable
def add(x, y):
    return x + y
total = reduce(add, numbers)
print(total)  # 15
```

---

### Q27: What is enumerate() and zip()?
**Answer:**

**enumerate()**: Get both index and value

```python
fruits = ["apple", "banana", "cherry"]

# Without enumerate
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (better)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Starting from different number
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry
```

**zip()**: Combine multiple iterables

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Mumbai", "Delhi", "Bangalore"]

# Zip them together
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Convert to list of tuples
paired = list(zip(names, ages))
print(paired)
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Unzip (reverse operation)
names, ages = zip(*paired)
print(names)  # ('Alice', 'Bob', 'Charlie')
print(ages)   # (25, 30, 35)
```

---

### Q28: What is the difference between list, tuple, set, and dictionary?
**Answer:**

```python
# LIST - ordered, mutable, allows duplicates
my_list = [1, 2, 3, 2, "hello"]
my_list[0] = 10  # Can modify
my_list.append(4)  # Can add
print(my_list)  # [10, 2, 3, 2, 'hello', 4]

# TUPLE - ordered, immutable, allows duplicates
my_tuple = (1, 2, 3, 2, "hello")
# my_tuple[0] = 10  # Error! Cannot modify
# my_tuple.append(4)  # Error! Cannot add
print(my_tuple)  # (1, 2, 3, 2, 'hello')

# SET - unordered, mutable, NO duplicates
my_set = {1, 2, 3, 2, "hello"}
my_set.add(4)  # Can add
print(my_set)  # {1, 2, 3, 'hello', 4} - no duplicates!
print(2 in my_set)  # True - fast lookup O(1)

# DICTIONARY - key-value pairs, unordered (Python 3.7+), mutable
my_dict = {"name": "Alice", "age": 25, "city": "Mumbai"}
print(my_dict["name"])  # "Alice"
my_dict["age"] = 26  # Modify
my_dict["country"] = "India"  # Add new key-value
print(my_dict)  # {'name': 'Alice', 'age': 26, 'city': 'Mumbai', 'country': 'India'}
```

**Comparison table:**
| | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Ordered | ✓ | ✓ | ✗ | ✓ (3.7+) |
| Mutable | ✓ | ✗ | ✓ | ✓ |
| Duplicates | ✓ | ✓ | ✗ | ✗ (keys) |
| Use case | General purpose | Immutable, dict keys | Unique values, fast lookup | Key-value storage |

---

### Q29: How to work with dictionaries?
**Answer:**

```python
# Creating dictionaries
person = {"name": "Alice", "age": 25, "city": "Mumbai"}
person2 = dict(name="Bob", age=30)

# Accessing values
print(person["name"])  # "Alice"
print(person.get("age"))  # 25
print(person.get("country", "Not found"))  # "Not found" (default)

# Adding/Modifying
person["age"] = 26
person["country"] = "India"

# Removing
del person["city"]
person.pop("age")  # Also returns the value
person.popitem()  # Remove last item

# Checking existence
if "name" in person:
    print("Name exists")

# Iterating
for key, value in person.items():
    print(f"{key}: {value}")

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

# Dictionary methods
print(person.keys())    # dict_keys(['name', 'country'])
print(person.values())  # dict_values(['Alice', 'India'])
print(person.items())   # dict_items([('name', 'Alice'), ('country', 'India')])

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # {"a": 1, "b": 2, "c": 3, "d": 4}

# Or using update()
dict1.update(dict2)
```

---

### Q30: What is the difference between sort() and sorted()?
**Answer:**

```python
# sort() - modifies the list in place, returns None
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]

# sorted() - creates new sorted list, original unchanged
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(numbers)          # [3, 1, 4, 1, 5, 9] - unchanged
print(sorted_numbers)   # [1, 1, 3, 4, 5, 9]

# Reverse sorting
numbers.sort(reverse=True)  # sort() reverse
print(numbers)  # [9, 5, 4, 3, 1, 1]

sorted_desc = sorted(numbers, reverse=True)  # sorted() reverse
print(sorted_desc)  # [9, 5, 4, 3, 1, 1]

# Sort with key function
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# Case-insensitive sort
words = ["apple", "Banana", "cherry"]
sorted_words = sorted(words, key=str.lower)
print(sorted_words)  # ['apple', 'Banana', 'cherry']
```

**Comparison:**
| | sort() | sorted() |
|---|---|---|
| Works on | Lists only | Any iterable |
| Returns | None | New list |
| In-place | Yes | No |
| Speed | Slightly faster | Slightly slower |

---

### Q31: What is string slicing and formatting?
**Answer:**

**String slicing:**
```python
text = "Hello Python"
print(text[0])      # "H" - first character
print(text[-1])     # "n" - last character
print(text[0:5])    # "Hello" - characters 0 to 4
print(text[6:])     # "Python" - from position 6 to end
print(text[:5])     # "Hello" - from start to position 4
print(text[::2])    # "HloPto" - every 2nd character
print(text[::-1])   # "nohtyP olleH" - reversed!

# Negative indices
print(text[-6:])    # "Python" - last 6 characters
print(text[:-3])    # "Hello Pyt" - all except last 3
```

**String formatting:**
```python
# Method 1: % formatting (old)
name = "Alice"
age = 25
print("My name is %s and I'm %d years old" % (name, age))

# Method 2: .format() (better)
print("My name is {} and I'm {} years old".format(name, age))
print("I'm {1} and my name is {0}".format(name, age))  # Positional args
print("Name: {name}, Age: {age}".format(name=name, age=age))

# Method 3: f-strings (best - Python 3.6+)
print(f"My name is {name} and I'm {age} years old")
print(f"Next year I'll be {age + 1}")
print(f"Name: {name:>10}, Age: {age:<5}")  # Alignment

# Formatting numbers
pi = 3.14159
print(f"{pi:.2f}")  # "3.14" - 2 decimal places
print(f"{1000000:,}")  # "1,000,000" - with commas
print(f"{0.5:.0%}")  # "50%" - as percentage
```

---

### Q32: What are important string methods?
**Answer:**

```python
text = "Hello World"

# Case
print(text.lower())     # "hello world"
print(text.upper())     # "HELLO WORLD"
print(text.capitalize())  # "Hello world"
print(text.title())     # "Hello World"

# Searching
print(text.find("World"))    # 6 (index of first occurrence)
print(text.find("xyz"))      # -1 (not found)
print(text.count("l"))       # 3 (count of "l")
print(text.startswith("Hello"))  # True
print(text.endswith("World"))    # True

# Replacing
print(text.replace("World", "Python"))  # "Hello Python"
print(text.replace("l", "L", 1))        # "HeLlo World" (only first)

# Splitting and joining
words = text.split(" ")  # ["Hello", "World"]
print(" | ".join(words))  # "Hello | World"

# Stripping
text2 = "  Hello  \n"
print(repr(text2.strip()))   # "'Hello'" - removes whitespace
print(repr(text2.lstrip()))  # "'Hello  \n'" - left only
print(repr(text2.rstrip()))  # "'  Hello'" - right only

# Checking
print("Hello".isalpha())     # True - all letters
print("123".isdigit())       # True - all digits
print("Hello123".isalnum())  # True - letters and digits
print("   ".isspace())       # True - all whitespace
```

---

### Q33: What is a list and its common methods?
**Answer:**

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Adding items
fruits.append("date")           # Add at end
fruits.insert(1, "avocado")     # Add at specific position
numbers.extend([6, 7, 8])       # Add multiple items

# Removing items
fruits.remove("banana")         # Remove by value
removed = fruits.pop()          # Remove last item (returns it)
removed = fruits.pop(0)         # Remove first item
del fruits[0]                   # Delete by index
fruits.clear()                  # Remove all items

# Searching and counting
numbers = [1, 2, 3, 2, 4, 2]
print(numbers.index(2))         # 1 (first index of 2)
print(numbers.count(2))         # 3 (count of 2)
print(2 in numbers)             # True

# Copying
list1 = [1, 2, 3]
list2 = list1.copy()            # Shallow copy
list3 = list(list1)             # Another way
list4 = list1[:]                # Slice copy

# Sorting and reversing
numbers.sort()                  # In-place sort
numbers.reverse()               # In-place reverse
sorted_list = sorted(numbers)   # New sorted list

# Accessing
print(fruits[0])                # First element
print(fruits[-1])               # Last element
print(fruits[1:3])              # Slice
```

---

### Q34: How to check data types?
**Answer:**

```python
# Using type()
print(type(5))              # <class 'int'>
print(type("hello"))        # <class 'str'>
print(type(3.14))           # <class 'float'>
print(type([1, 2, 3]))      # <class 'list'>
print(type((1, 2, 3)))      # <class 'tuple'>
print(type({1, 2, 3}))      # <class 'set'>
print(type({"a": 1}))       # <class 'dict'>

# Using isinstance() (better for checking)
print(isinstance(5, int))           # True
print(isinstance(5, (int, float)))  # True - check multiple types
print(isinstance([1, 2], list))     # True

# Checking special cases
print(type(None))           # <class 'NoneType'>
print(type(True))           # <class 'bool'>
print(isinstance(True, int))  # True - bool is subclass of int

# isinstance() is better because of inheritance
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(type(dog))            # <class '__main__.Dog'>
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True - checks inheritance!
print(type(dog) == Animal)      # False
```

---

### Q35: What is a while and for loop? How to control them?
**Answer:**

```python
# For loop
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control: break and continue
for i in range(10):
    if i == 3:
        break  # Exit loop completely
    print(i)
# Output: 0 1 2

for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    print(i)
# Output: 0 1 2 4 5 6 7 8 9

# Else clause with loops (runs if no break)
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

# With break, else doesn't run
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("This won't print")  # Else skipped due to break
```

---

### Q36: What is pass, continue, break?
**Answer:**

```python
# break - exit loop completely
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # Stop loop
    print(num)
# Output: 1 2

# continue - skip current iteration
for num in numbers:
    if num == 3:
        continue  # Skip this number
    print(num)
# Output: 1 2 4 5

# pass - do nothing (placeholder)
for i in range(5):
    if i == 2:
        pass  # Do nothing, just continue
    print(i)
# Output: 0 1 2 3 4

# Practical use of pass
class MyClass:
    pass  # Empty class (implement later)

def my_function():
    pass  # Empty function (implement later)

if condition:
    pass  # Placeholder for code to write later
```

---

## Section 5: Advanced Python (Q37-50)

### Q37: What is a closure?
**Answer:**
A closure is a function that "remembers" variables from the scope where it was created, even after that scope has ended.

```python
# Simple closure
def outer(x):
    def inner(y):
        return x + y  # inner "remembers" x from outer
    return inner

add_five = outer(5)
print(add_five(3))   # 8 (5 + 3)
print(add_five(10))  # 15 (5 + 10)

# Multiple closures
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5))    # 10
print(triple(5))    # 15

# Practical example: counter
def make_counter():
    count = 0
    def increment():
        nonlocal count  # Modify outer scope variable
        count += 1
        return count
    return increment

counter1 = make_counter()
counter2 = make_counter()
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3
print(counter2())  # 1 (separate counter)
```

---

### Q38: What is a decorator with arguments?
**Answer:**
A decorator that accepts parameters. This is a decorator factory.

```python
# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello {name}")
    return f"Greeted {name}"

greet("Alice")
# Output:
# Hello Alice
# Hello Alice
# Hello Alice

# Decorator with optional arguments
def timing_decorator(enable=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if enable:
                import time
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"Execution time: {end - start:.4f}s")
                return result
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@timing_decorator(enable=True)
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()  # Shows execution time
```

---

### Q39: What is a regular expression (regex)?
**Answer:**
Regex is a pattern for matching and manipulating strings.

```python
import re

# Basic patterns
text = "Hello 123 World"

# re.search() - find first match
match = re.search(r"\d+", text)  # \d+ means one or more digits
if match:
    print(match.group())  # "123"

# re.findall() - find all matches
numbers = re.findall(r"\d+", "I have 2 cats and 5 dogs")
print(numbers)  # ['2', '5']

# re.sub() - replace matches
text = "I have 2 cats and 5 dogs"
new_text = re.sub(r"\d+", "X", text)
print(new_text)  # "I have X cats and X dogs"

# Common patterns
r"\d"      # Single digit
r"\d+"     # One or more digits
r"\w+"     # One or more word characters
r"\s"      # Whitespace
r"[a-z]"   # Any lowercase letter
r"[A-Z]"   # Any uppercase letter
r"[a-zA-Z0-9]"  # Alphanumeric
r"^Hello"  # Starts with Hello
r"World$"  # Ends with World
r"cat|dog" # Either cat or dog

# Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = "alice@example.com"
if re.match(email_pattern, email):
    print("Valid email")

# Phone number
phone_pattern = r"^\+?1?\d{9,15}$"
if re.match(phone_pattern, "+919876543210"):
    print("Valid phone")

# Extract data
text = "Date: 2024-01-15"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
```

---

### Q40: What is JSON and how to work with it?
**Answer:**
JSON (JavaScript Object Notation) is a data format. Python has `json` module to convert between JSON and Python objects.

```python
import json

# Python object to JSON string
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"],
    "active": True,
    "balance": None
}

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)
# Output:
# {
#   "name": "Alice",
#   "age": 25,
#   "hobbies": [
#     "reading",
#     "coding"
#   ],
#   "active": true,
#   "balance": null
# }

# JSON string to Python object
json_data = '{"name": "Bob", "age": 30, "city": "Delhi"}'
parsed = json.loads(json_data)
print(parsed["name"])  # "Bob"

# Reading from JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Writing to JSON file
with open("output.json", "w") as file:
    json.dump(data, file, indent=2)

# Pretty printing
print(json.dumps(data, indent=4, sort_keys=True))

# JSON vs Python types
# JSON: null, true, false, string, number, array, object
# Python: None, True, False, str, int/float, list, dict
```

---

### Q41: What is the difference between deepcopy and shallow copy?
**Answer:**
**Shallow copy**: Copies top level only. Nested objects still reference same memory.
**Deep copy**: Recursively copies everything including nested objects.

```python
import copy

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99  # Changes nested list
print(original)   # [[99, 2], [3, 4]] - original affected!
print(shallow)    # [[99, 2], [3, 4]]

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99  # Only deep copy affected
print(original)  # [[1, 2], [3, 4]] - unchanged
print(deep)      # [[99, 2], [3, 4]]

# With dictionaries
original_dict = {"a": [1, 2], "b": [3, 4]}
shallow_dict = original_dict.copy()
deep_dict = copy.deepcopy(original_dict)

original_dict["a"][0] = 99
print(original_dict)    # {"a": [99, 2], "b": [3, 4]}
print(shallow_dict)     # {"a": [99, 2], "b": [3, 4]} - affected
print(deep_dict)        # {"a": [1, 2], "b": [3, 4]} - unaffected
```

---

### Q42: What is *args and **kwargs with examples?
**Answer:** (Already covered in Q10, but here's deeper example)

```python
def function(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")  # tuple of remaining positional
    print(f"kwargs={kwargs}")  # dict of keyword arguments

function(1, 2, 3, 4, 5, name="Alice", age=25)
# Output:
# a=1, b=2
# args=(3, 4, 5)
# kwargs={'name': 'Alice', 'age': 25}

# Unpacking with *
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks list as separate arguments
print(result)  # 6

# Unpacking with **
def greet(name, age, city):
    return f"{name} is {age} years old, lives in {city}"

person = {"name": "Alice", "age": 25, "city": "Mumbai"}
message = greet(**person)  # Unpacks dict as keyword arguments
print(message)  # "Alice is 25 years old, lives in Mumbai"

# Forwarding arguments
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)  # Forward all arguments
    return wrapper

@decorator_function
def my_func(x, y, z=0):
    return x + y + z

print(my_func(1, 2, z=3))  # Arguments forwarded correctly
```

---

### Q43: What is a context manager? How to create one?
**Answer:**
Context manager ensures resource cleanup using `with` statement.

```python
# Using context manager (file handling)
with open("file.txt") as f:
    content = f.read()
# File automatically closed, even if error occurs

# Creating custom context manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):  # Runs when entering 'with' block
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):  # Runs when exiting
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Using custom context manager
with FileManager("data.txt", "r") as file:
    content = file.read()
    print(content)
# File auto-closes here

# Using contextlib for simple context managers
from contextlib import contextmanager

@contextmanager
def database_connection(url):
    print("Connecting to database...")
    conn = {"connected": True}  # Simulate connection
    try:
        yield conn
    finally:
        print("Closing database...")
        conn["connected"] = False

# Using it
with database_connection("mongodb://localhost") as db:
    print(f"Database: {db}")
# Output:
# Connecting to database...
# Database: {'connected': True}
# Closing database...
```

---

### Q44: What is the difference between is and is not?
**Answer:**
`is` and `is not` check object identity (same memory location), not equality.

```python
# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True - same values
print(a is b)    # False - different objects

print(a == c)    # True - same values
print(a is c)    # True - same object

# is None (standard way)
value = None
if value is None:  # Correct
    print("Value is None")

if value == None:  # Works but not Pythonic
    print("Value is None")

# is not
if value is not None:
    print("Value is not None")

# Remember: Small integers cached
x = 5
y = 5
print(x is y)  # True - Python caches -5 to 256

x = 257
y = 257
print(x is y)  # False - outside cache range (usually)
```

---

### Q45: What is a namespace and scope?
**Answer:**
- **Namespace**: Collection of names (variables, functions, etc.) and their values
- **Scope**: Region of code where a name is accessible

**LEGB rule** (order of scope lookup):
1. **L**ocal - inside current function
2. **E**nclosing - in enclosing functions
3. **G**lobal - in global scope
4. **B**uilt-in - Python's built-in scope

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Checks Local first -> "local"
    
    inner()
    print(x)  # Enclosing scope -> "enclosing"

print(x)  # Global scope -> "global"
outer()

# Output:
# global
# local
# enclosing

# global keyword
x = 10

def change_global():
    global x
    x = 20  # Modifies global x

change_global()
print(x)  # 20

# nonlocal keyword (for enclosing scope)
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20  # Modifies enclosing scope x
    
    inner()
    print(x)  # 20

outer()
```

---

### Q46: What is the difference between module, package, and library?
**Answer:**

**Module**: Single .py file containing Python code
```
# file: math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**Package**: Directory containing modules and __init__.py
```
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
```

**Library**: Collection of packages (like numpy, pandas)

```python
# Importing from module
import math_operations
result = math_operations.add(5, 3)

# Importing specific function
from math_operations import add
result = add(5, 3)

# Importing from package
from my_package import module1
from my_package.sub_package import module3

# Using library
import numpy as np
array = np.array([1, 2, 3])
```

---

### Q47: What is *args vs **kwargs again with use cases?
**Answer:** (Expanded from Q10)

```python
# *args for varying number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))      # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs for varying number of keyword arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="Mumbai")
# Output:
# name: Alice
# age: 25
# city: Mumbai

# Real use case: Function wrapper
def api_call(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")
    # Call actual API with these arguments
    return "API response"

api_call(1, 2, 3, key="value", timeout=30)

# Unpacking lists and dicts
def greet(name, age, city):
    return f"{name}, {age}, {city}"

args_list = ["Alice", 25, "Mumbai"]
result = greet(*args_list)  # Unpacks list
print(result)  # "Alice, 25, Mumbai"

kwargs_dict = {"name": "Bob", "age": 30, "city": "Delhi"}
result = greet(**kwargs_dict)  # Unpacks dict
print(result)  # "Bob, 30, Delhi"
```

---

### Q48: What is the difference between print() and return?
**Answer:**

**print()**: Displays output to console. Doesn't return anything (returns None).
**return**: Sends value back from function. Can be assigned to variable.

```python
def function_with_print():
    print("Hello")  # Shows in console
    # Implicitly returns None

def function_with_return():
    return "Hello"  # Doesn't show in console
    # Returns the string

# Using them
result1 = function_with_print()
print(result1)  # None

result2 = function_with_return()
print(result2)  # "Hello"

# Common mistakes
def add_numbers(a, b):
    print(a + b)  # Wrong! Just prints, doesn't return
    # When used in calculation: result = add_numbers(5, 3) + 10 -> Error!

def add_numbers_correct(a, b):
    return a + b  # Correct! Returns value
    # Can use: result = add_numbers_correct(5, 3) + 10 -> 18

# Early return
def check_age(age):
    if age < 0:
        return "Invalid age"  # Exit function early
    if age < 18:
        return "Minor"
    return "Adult"

print(check_age(15))   # "Minor"
print(check_age(25))   # "Adult"
```

---

### Q49: What is eval() and exec()?
**Answer:**
Both execute Python code as strings. **DANGER**: Never use with untrusted input!

```python
# eval() - evaluates expression, returns result
result = eval("2 + 3 * 4")
print(result)  # 14

result = eval("len('hello')")
print(result)  # 5

# With variables
x = 10
result = eval("x * 2 + 5")
print(result)  # 25

# exec() - executes statements, returns None
code = """
x = 10
y = 20
z = x + y
print(f"Sum: {z}")
"""
exec(code)  # Output: "Sum: 30"

# Difference
eval("2 + 3")      # Returns 5
exec("print(2 + 3)")  # Prints 5, returns None

# **SECURITY WARNING**: Never use with untrusted input!
# Malicious code can be executed
user_input = "import os; os.system('rm -rf /')"
# eval(user_input)   # DO NOT DO THIS!
# exec(user_input)   # DO NOT DO THIS!

# Instead, use ast.literal_eval for safe evaluation
import ast
safe_data = "{'name': 'Alice', 'age': 25}"
result = ast.literal_eval(safe_data)  # Safe!
print(result)  # {'name': 'Alice', 'age': 25}
```

---

### Q50: What is the difference between append() and extend()?
**Answer:**

**append()**: Add single element (even if it's a list)
**extend()**: Add multiple elements from iterable

```python
# append()
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

numbers.append([5, 6])
print(numbers)  # [1, 2, 3, 4, [5, 6]] - list added as single element!

# extend()
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6] - elements added individually

numbers.extend([7, 8])
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8]

# Other iterables
numbers = [1, 2, 3]
numbers.extend((4, 5))      # Tuple
numbers.extend("67")        # String (adds '6', '7')
print(numbers)  # [1, 2, 3, 4, 5, '6', '7']

# += behavior
list1 = [1, 2, 3]
list1 += [4, 5]     # Uses extend behavior
print(list1)  # [1, 2, 3, 4, 5]

list2 = [1, 2, 3]
list2 += [[4, 5]]   # Adds list as element
print(list2)  # [1, 2, 3, [4, 5]]

# Performance
# append() - O(1) always
# extend() - O(n) where n is items being added
```

---

---


# PART 2: DATA STRUCTURES & ALGORITHMS (DSA) - TOP 50 QUESTIONS
## Section 1: Arrays & Strings (Q1-10)
### Q1: Reverse an array in-place
**Answer:**

```python
# Method 1: Two-pointer approach (best for in-place)
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # [5, 4, 3, 2, 1]

# Method 2: Using slicing (creates new array)
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print(reversed_arr)  # [5, 4, 3, 2, 1]

# Method 3: Using reversed() function
arr = [1, 2, 3, 4, 5]
print(list(reversed(arr)))  # [5, 4, 3, 2, 1]
```

**Complexity:** Time O(n), Space O(1)

---

### Q2: Find duplicate element in array
**Answer:**

```python
# Method 1: Hash Set (fast)
def find_duplicate_set(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

print(find_duplicate_set([1, 2, 3, 2, 4]))  # 2

# Method 2: Sort and compare adjacent (space efficient)
def find_duplicate_sort(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return arr[i]
    return None

# Method 3: Floyd's Cycle Detection (no extra space, no sorting)
# Only works when array has n elements with values 1 to n-1
def find_duplicate_floyd(arr):
    slow = fast = arr[0]
    
    # Find cycle
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    # Find cycle start
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

print(find_duplicate_floyd([1, 3, 4, 2, 2]))  # 2
```

**Complexity:** Method 1: Time O(n), Space O(n) | Method 3: Time O(n), Space O(1)

---

### Q3: Two Sum - Find pair that adds to target
**Answer:**

```python
# Method 1: Hash Map (best)
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Return indices
        seen[num] = i
    return None

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]

# Method 2: Two Pointers (for sorted array)
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

print(two_sum_sorted([2, 7, 11, 15], 9))  # [0, 1]
```

**Complexity:** Method 1: Time O(n), Space O(n) | Method 2: Time O(n), Space O(1)

---

### Q4: Find maximum subarray sum (Kadane's Algorithm)
**Answer:**

```python
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend current sum or start fresh
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 (subarray [4, -1, 2, 1])
print(max_subarray_sum([5, -3, 5]))  # 7

# To also get the subarray
def max_subarray_with_range(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, arr[start:end+1]

result, subarray = max_subarray_with_range([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(f"Max sum: {result}, Subarray: {subarray}")  # Max sum: 6, Subarray: [4, -1, 2, 1]
```

**Complexity:** Time O(n), Space O(1)

---

### Q5: Merge sorted arrays
**Answer:**

```python
# Method 1: Using two pointers (in-place if result array given)
def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]

# Method 2: Merge in-place (modifying first array)
def merge_inplace(arr1, m, arr2, n):
    """Merge arr2 into arr1. arr1 has size m+n, arr2 has size n"""
    i = m - 1          # Last element in arr1
    j = n - 1          # Last element in arr2
    k = m + n - 1      # Last position in arr1
    
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    
    # Add remaining arr2 elements (arr1 remaining already in place)
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    
    return arr1

arr1 = [1, 3, 5, 0, 0, 0]
arr2 = [2, 4, 6]
print(merge_inplace(arr1, 3, arr2, 3))  # [1, 2, 3, 4, 5, 6]
```

**Complexity:** Time O(m + n), Space O(1) for inplace

---

### Q6: Remove duplicates from sorted array
**Answer:**

```python
# Method 1: Two-pointer approach
def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    
    write_ptr = 0  # Position to write unique element
    
    for read_ptr in range(1, len(arr)):
        if arr[read_ptr] != arr[write_ptr]:
            write_ptr += 1
            arr[write_ptr] = arr[read_ptr]
    
    return write_ptr + 1  # Number of unique elements

arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
count = remove_duplicates(arr)
print(arr[:count])  # [1, 2, 3, 4, 5]

# Method 2: Keep track of duplicates count
def remove_duplicates_with_count(arr, k=2):
    """Remove duplicates keeping at most k occurrences"""
    if len(arr) <= k:
        return len(arr)
    
    write_ptr = k
    
    for read_ptr in range(k, len(arr)):
        if arr[read_ptr] != arr[write_ptr - k]:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1
    
    return write_ptr

arr = [1, 1, 1, 2, 2, 3]
count = remove_duplicates_with_count(arr, k=2)
print(arr[:count])  # [1, 1, 2, 2, 3] - max 2 duplicates
```

**Complexity:** Time O(n), Space O(1)

---

### Q7: Rotate array by k positions
**Answer:**

```python
# Method 1: Using slicing (simple but creates new array)
def rotate_array_slice(arr, k):
    k = k % len(arr)  # Handle k > len(arr)
    return arr[-k:] + arr[:-k]

print(rotate_array_slice([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]

# Method 2: Reverse approach (in-place, elegant)
def rotate_array(arr, k):
    k = k % len(arr)
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Reverse entire array
    reverse(0, len(arr) - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, len(arr) - 1)
    
    return arr

arr = [1, 2, 3, 4, 5]
print(rotate_array(arr, 2))  # [4, 5, 1, 2, 3]

# Example of reversal process:
# Original: [1, 2, 3, 4, 5], k=2
# After reverse all: [5, 4, 3, 2, 1]
# After reverse first 2: [4, 5, 3, 2, 1]
# After reverse remaining: [4, 5, 1, 2, 3]
```

**Complexity:** Time O(n), Space O(1)

---

### Q8: Search in rotated sorted array
**Answer:**

```python
def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which side is sorted
        if arr[left] <= arr[mid]:  # Left side is sorted
            # Check if target is in sorted left side
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Search left
            else:
                left = mid + 1   # Search right
        else:  # Right side is sorted
            # Check if target is in sorted right side
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Search right
            else:
                right = mid - 1  # Search left
    
    return -1  # Not found

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(search_rotated([1], 1))                    # 0
```

**Complexity:** Time O(log n), Space O(1)

---

### Q9: Longest substring without repeating characters
**Answer:**

```python
def longest_substring_no_repeats(s):
    char_index = {}  # Store last seen index of character
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        char = s[end]
        
        # If character seen before and in current window
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # Move start forward
        
        # Update last seen index
        char_index[char] = end
        
        # Update max length
        max_length = max(max_length, end - start + 1)
    
    return max_length

print(longest_substring_no_repeats("abcabcbb"))  # 3 ("abc")
print(longest_substring_no_repeats("bbbbb"))     # 1 ("b")
print(longest_substring_no_repeats("pwwkew"))    # 3 ("wke")
print(longest_substring_no_repeats("au"))        # 2 ("au")

# To return the actual substring
def longest_substring_with_str(s):
    char_index = {}
    max_length = 0
    start = 0
    max_start = 0
    
    for end in range(len(s)):
        char = s[end]
        
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_start = start
    
    return s[max_start:max_start + max_length]

print(longest_substring_with_str("abcabcbb"))  # "abc"
```

**Complexity:** Time O(n), Space O(min(n, charset_size))

---

### Q10: Valid Parentheses
**Answer:**

```python
def is_valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0  # All opening brackets matched

print(is_valid_parentheses("()"))        # True
print(is_valid_parentheses("()[]{}"))    # True
print(is_valid_parentheses("([)]"))      # False
print(is_valid_parentheses("{[]}"))      # True
print(is_valid_parentheses(""))          # True

# Alternative approach
def is_valid_parentheses_v2(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping:  # Closing bracket
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

print(is_valid_parentheses_v2("()[]{}"))  # True
```

**Complexity:** Time O(n), Space O(n)

---

## Section 2: Linked Lists (Q11-15)

### Q11: Reverse a Linked List
**Answer:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Method 1: Iterative (best)
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        # Store next node
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move prev forward
        prev = current
        # Move current forward
        current = next_temp
    
    return prev

# Create list: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
new_head = reverse_linked_list(head)
# Result: 3 -> 2 -> 1 -> None

# Method 2: Recursive
def reverse_linked_list_recursive(head):
    if not head or not head.next:
        return head
    
    # Reverse the rest
    new_head = reverse_linked_list_recursive(head.next)
    
    # Make next node point back to current
    head.next.next = head
    # Remove cycle
    head.next = None
    
    return new_head

# Method 3: Recursive with different approach
def reverse_recursive_v2(head):
    def helper(node):
        if not node or not node.next:
            return node, node
        
        new_head, last = helper(node.next)
        last.next = node
        node.next = None
        return new_head, node
    
    return helper(head)[0]
```

**Complexity:** Time O(n), Space O(1) iterative | O(n) recursive

---

### Q12: Detect cycle in Linked List (Floyd's Algorithm)
**Answer:**

```python
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

# Find cycle start node
def find_cycle_start(head):
    if not head or not head.next:
        return None
    
    slow = head
    fast = head
    
    # Find intersection point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow  # Cycle start node

# Get cycle length
def get_cycle_length(head):
    if not head or not head.next:
        return 0
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0
    
    # Count cycle length
    length = 1
    current = slow.next
    while current != slow:
        length += 1
        current = current.next
    
    return length
```

**Complexity:** Time O(n), Space O(1)

---

### Q13: Merge Two Sorted Linked Lists
**Answer:**

```python
def merge_sorted_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = list1 if list1 else list2
    
    return dummy.next

# Recursive approach
def merge_sorted_lists_recursive(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.val <= list2.val:
        list1.next = merge_sorted_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_sorted_lists_recursive(list1, list2.next)
        return list2
```

**Complexity:** Time O(n + m), Space O(1) iterative | O(n + m) recursive

---

### Q14: Find Middle of Linked List
**Answer:**

```python
def find_middle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # slow is at middle

# If odd number of nodes, returns middle
# If even number of nodes, returns second middle
# Example: 1->2->3->4->5, returns 3
# Example: 1->2->3->4, returns 3

# To get first middle for even length:
def find_middle_first(head):
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    return prev if prev else slow
```

**Complexity:** Time O(n), Space O(1)

---

### Q15: Remove Nth Node From End
**Answer:**

```python
def remove_nth_from_end(head, n):
    # Create dummy node to handle edge case (removing first node)
    dummy = ListNode(0)
    dummy.next = head
    
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        if not first:
            return head  # n is greater than list length
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node
    second.next = second.next.next
    
    return dummy.next

# Example: 1->2->3->4->5, n=2
# Remove 4 (second from end)
# Result: 1->2->3->5

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = remove_nth_from_end(head, 2)
```

**Complexity:** Time O(n), Space O(1)

---

## Section 3: Trees (Q16-25)

### Q16: Binary Tree Level Order Traversal (BFS)
**Answer:**

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Example tree:
#       3
#      / \
#     9  20
#        / \
#       15  7
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order_traversal(tree))  # [[3], [9, 20], [15, 7]]
```

**Complexity:** Time O(n), Space O(n)

---

### Q17: Binary Tree Inorder, Preorder, Postorder Traversal
**Answer:**

```python
# Inorder: Left -> Node -> Right (for BST gives sorted)
def inorder(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    
    traverse(root)
    return result

# Preorder: Node -> Left -> Right
def preorder(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
    
    traverse(root)
    return result

# Postorder: Left -> Right -> Node
def postorder(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
    
    traverse(root)
    return result

# Iterative versions using stack
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

# Example:
#       1
#      / \
#     2   3
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print(inorder(tree))    # [2, 1, 3]
print(preorder(tree))   # [1, 2, 3]
print(postorder(tree))  # [2, 3, 1]
```

**Complexity:** Time O(n), Space O(h) where h is height

---

### Q18: Maximum Depth of Binary Tree
**Answer:**

```python
# DFS Recursive
def max_depth_recursive(root):
    if not root:
        return 0
    
    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))

# BFS Iterative
def max_depth_bfs(root):
    if not root:
        return 0
    
    queue = deque([(root, 1)])  # (node, depth)
    
    while queue:
        node, depth = queue.popleft()
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return depth

# DFS Iterative using stack
def max_depth_dfs(root):
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    
    return max_depth
```

**Complexity:** Time O(n), Space O(h)

---

### Q19: Lowest Common Ancestor (LCA) of Binary Search Tree
**Answer:**

```python
def lowest_common_ancestor_bst(root, p, q):
    """
    Find LCA in BST where p and q are nodes with values
    Use BST property: left < root < right
    """
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        # Both in left subtree
        return lowest_common_ancestor_bst(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        # Both in right subtree
        return lowest_common_ancestor_bst(root.right, p, q)
    else:
        # One on each side or one is root
        return root

# For regular Binary Tree (no BST property)
def lowest_common_ancestor_bt(root, p, q):
    """Find LCA in any binary tree"""
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor_bt(root.left, p, q)
    right = lowest_common_ancestor_bt(root.right, p, q)
    
    if left and right:
        return root  # p and q on different sides
    
    return left if left else right  # Both on same side

# Example:
#         3
#        / \
#       5   1
#      / \  / \
#     6  2 0  8
#       / \
#      7   4
tree = TreeNode(3,
    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(0), TreeNode(8))
)
print(lowest_common_ancestor_bst(tree, TreeNode(5), TreeNode(1)).val)  # 3
print(lowest_common_ancestor_bst(tree, TreeNode(5), TreeNode(4)).val)  # 5
```

**Complexity:** Time O(log n) BST | O(n) BT, Space O(h)

---

### Q20: Validate Binary Search Tree
**Answer:**

```python
# Method 1: Recursive with min/max
def is_valid_bst_minmax(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return (is_valid_bst_minmax(root.left, min_val, root.val) and
            is_valid_bst_minmax(root.right, root.val, max_val))

# Method 2: Inorder traversal (should be sorted)
def is_valid_bst_inorder(root):
    def inorder(node):
        if not node:
            return True
        
        # Check left subtree
        if not inorder(node.left):
            return False
        
        # Check current node
        if node.val <= inorder.prev:
            return False
        inorder.prev = node.val
        
        # Check right subtree
        return inorder(node.right)
    
    inorder.prev = float('-inf')
    return inorder(root)

# Method 3: Iterative
def is_valid_bst_iterative(root):
    stack = [(root, float('-inf'), float('inf'))]
    
    while stack:
        node, min_val, max_val = stack.pop()
        
        if not node:
            continue
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        stack.append((node.left, min_val, node.val))
        stack.append((node.right, node.val, max_val))
    
    return True

# Example:
#       5
#      / \
#     3   7
#    / \
#   2   4
tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
print(is_valid_bst_minmax(tree))  # True

# Invalid:
#       5
#      / \
#     3   8
#    / \
#   2   6  (6 > 5, violates BST property)
invalid_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(6)), TreeNode(8))
print(is_valid_bst_minmax(invalid_tree))  # False
```

**Complexity:** Time O(n), Space O(h)

---

### Q21: Balanced Binary Tree
**Answer:**

```python
def is_balanced(root):
    """
    A balanced tree: for every node, heights of left and right subtrees
    differ by at most 1
    """
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        # Check if current node is balanced
        if abs(left_height - right_height) > 1:
            return -1  # Not balanced
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1

# Alternative approach
def is_balanced_v2(root):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    
    if not root:
        return True
    
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    
    return is_balanced_v2(root.left) and is_balanced_v2(root.right)

# Example:
#       3
#      / \
#     9  20
#       / \
#      15  7
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(is_balanced(tree))  # True

# Unbalanced:
#        1
#         \
#          2
#           \
#            3
unbalanced = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
print(is_balanced(unbalanced))  # False
```

**Complexity:** Time O(n), Space O(h)

---

### Q22: Path Sum
**Answer:**

```python
def has_path_sum(root, target_sum):
    """Check if tree has root-to-leaf path that sums to target"""
    if not root:
        return False
    
    # Base case: leaf node
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Recursively check left and right
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))

# Return all paths that sum to target
def path_sum(root, target_sum):
    result = []
    
    def dfs(node, remaining, path):
        if not node:
            return
        
        remaining -= node.val
        path.append(node.val)
        
        # Check if leaf and sum matches
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])
        
        # Recurse
        dfs(node.left, remaining, path)
        dfs(node.right, remaining, path)
        
        # Backtrack
        path.pop()
    
    dfs(root, target_sum, [])
    return result

# Example:
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#   / \      \
#  7   2      1
tree = TreeNode(5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
)
print(has_path_sum(tree, 22))  # True (5->4->11->2)
print(path_sum(tree, 22))      # [[5, 4, 11, 2]]
```

**Complexity:** Time O(n), Space O(h)

---

### Q23: Construct Binary Tree from Traversals
**Answer:**

```python
# From Inorder and Preorder
def build_tree_inpre(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # First element in preorder is root
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # Find root in inorder
    idx = inorder.index(root_val)
    
    # Left subtree elements
    left_inorder = inorder[:idx]
    left_preorder = preorder[1:1+len(left_inorder)]
    
    # Right subtree elements
    right_inorder = inorder[idx+1:]
    right_preorder = preorder[1+len(left_inorder):]
    
    root.left = build_tree_inpre(left_preorder, left_inorder)
    root.right = build_tree_inpre(right_preorder, right_inorder)
    
    return root

# From Inorder and Postorder
def build_tree_inpost(inorder, postorder):
    if not inorder or not postorder:
        return None
    
    # Last element in postorder is root
    root_val = postorder[-1]
    root = TreeNode(root_val)
    
    # Find root in inorder
    idx = inorder.index(root_val)
    
    # Left subtree elements
    left_inorder = inorder[:idx]
    left_postorder = postorder[:len(left_inorder)]
    
    # Right subtree elements
    right_inorder = inorder[idx+1:]
    right_postorder = postorder[len(left_inorder):-1]
    
    root.left = build_tree_inpost(left_inorder, left_postorder)
    root.right = build_tree_inpost(right_inorder, right_postorder)
    
    return root

# Example:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
tree = build_tree_inpre(preorder, inorder)
# Builds:
#       3
#      / \
#     9  20
#       / \
#      15  7
```

**Complexity:** Time O(n²), Space O(n)

---

### Q24: Serialize and Deserialize Binary Tree
**Answer:**

```python
class Codec:
    def serialize(self, root):
        """Convert tree to string"""
        result = []
        
        def preorder(node):
            if not node:
                result.append('None')
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ','.join(result)
    
    def deserialize(self, data):
        """Convert string back to tree"""
        values = iter(data.split(','))
        
        def preorder():
            val = next(values)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        
        return preorder()

# Example:
tree = TreeNode(1, TreeNode(2), TreeNode(3))
codec = Codec()
serialized = codec.serialize(tree)
print(serialized)  # "1,2,None,None,3,None,None"
deserialized = codec.deserialize(serialized)
# Reconstructs original tree
```

**Complexity:** Time O(n), Space O(n)

---

### Q25: Binary Tree Right Side View
**Answer:**

```python
from collections import deque

def right_side_view(root):
    """Return values visible from right side"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Last node in each level is visible from right
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Alternative: DFS approach
def right_side_view_dfs(root):
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        # Add node if first time seeing this level
        if level == len(result):
            result.append(node.val)
        
        # Process right first, then left
        # (right is more likely to be rightmost)
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    
    dfs(root, 0)
    return result

# Example:
#       1
#      / \
#     2   3
#      \   \
#       5   4
tree = TreeNode(1,
    TreeNode(2, None, TreeNode(5)),
    TreeNode(3, None, TreeNode(4))
)
print(right_side_view(tree))  # [1, 3, 4]
```

**Complexity:** Time O(n), Space O(n)

---

## Section 4: Graphs & Sorting (Q26-40)

### Q26: Graph Traversal - BFS and DFS
**Answer:**

```python
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        """Breadth-First Search"""
        visited = set()
        queue = deque([start])
        result = []
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Depth-First Search - Recursive"""
        visited = set()
        result = []
        
        def traverse(node):
            visited.add(node)
            result.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    traverse(neighbor)
        
        traverse(start)
        return result
    
    def dfs_iterative(self, start):
        """DFS using stack"""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Add neighbors (reverse for same order as recursive)
                stack.extend(reversed(self.graph[node]))
        
        return result

# Example:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g.bfs(0))            # [0, 1, 2, 3]
print(g.dfs(0))            # [0, 1, 3, 2]
print(g.dfs_iterative(0))  # [0, 1, 3, 2]
```

**Complexity:** Time O(V + E), Space O(V)

---

### Q27: Topological Sort
**Answer:**

```python
# Method 1: Using DFS
def topological_sort_dfs(graph, n):
    """
    Topological sort of directed acyclic graph
    Returns nodes in order such that for every edge u->v, u comes before v
    """
    visited = [False] * n
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]

# Method 2: Using Kahn's Algorithm (BFS)
def topological_sort_kahn(graph, n):
    """Using indegree"""
    indegree = [0] * n
    queue = deque()
    result = []
    
    # Calculate indegree
    for node in range(n):
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    # Add nodes with indegree 0
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []  # [] if cycle exists

# Example: Course prerequisites
# Courses: 0, 1, 2, 3
# 1 -> 0 (must take 1 before 0)
# 2 -> 1
# 2 -> 3
graph = {0: [], 1: [0], 2: [1, 3], 3: []}
print(topological_sort_kahn(graph, 4))  # [2, 3, 1, 0] or similar
```

**Complexity:** Time O(V + E), Space O(V)

---

### Q28: Course Schedule (Cycle Detection)
**Answer:**

```python
def can_finish_courses(num_courses, prerequisites):
    """
    Check if courses can be completed (no cycle in graph)
    prerequisites[i] = [a, b] means take b before a
    """
    # Build adjacency list and indegree
    graph = defaultdict(list)
    indegree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # Kahn's algorithm
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    completed = 0
    
    while queue:
        course = queue.popleft()
        completed += 1
        
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    return completed == num_courses

# DFS approach
def can_finish_dfs(num_courses, prerequisites):
    # 0: unvisited, 1: visiting, 2: visited
    state = [0] * num_courses
    graph = defaultdict(list)
    
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    def has_cycle(course):
        if state[course] == 1:
            return True  # Cycle detected
        if state[course] == 2:
            return False
        
        state[course] = 1
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        state[course] = 2
        return False
    
    for course in range(num_courses):
        if has_cycle(course):
            return False
    
    return True

# Examples:
print(can_finish_courses(2, [[1, 0]]))           # True (can take 0 then 1)
print(can_finish_courses(2, [[1, 0], [0, 1]]))   # False (circular)
print(can_finish_courses(3, [[1, 0], [2, 1]]))   # True
```

**Complexity:** Time O(V + E), Space O(V + E)

---

### Q29: Merge K Sorted Lists
**Answer:**

```python
import heapq

def merge_k_lists(lists):
    """Merge k sorted linked lists"""
    min_heap = []
    result = dummy = ListNode(0)
    
    # Add first node of each list to heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst.val, i, lst))
    
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        dummy.next = node
        dummy = dummy.next
        
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    
    return result.next

# Alternative: Merge two at a time
def merge_k_lists_v2(lists):
    if not lists:
        return None
    
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two_lists(l1, l2))
        lists = merged
    
    return lists[0]

def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    return dummy.next
```

**Complexity:** Time O(n log k), Space O(k) where k = number of lists

---

### Q30: Merge Sort
**Answer:**

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# In-place merge sort
def merge_sort_inplace(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)
    
    return arr

def merge_inplace(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
    
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
    
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1

# Example:
print(merge_sort([64, 34, 25, 12, 22, 11, 90]))  # [11, 12, 22, 25, 34, 64, 90]
```

**Complexity:** Time O(n log n) always, Space O(n)

---

### Q31-40: Quick Sort, Binary Search, LRU Cache, etc.

Due to length constraints, I'll provide condensed versions:

### Q31: Quick Sort
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# In-place
def quick_sort_inplace(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        pivot_idx = partition(arr, left, right)
        quick_sort_inplace(arr, left, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, right)
    
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
```
**Complexity:** Time O(n log n) avg, O(n²) worst | Space O(log n)

---

### Q32: Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

print(binary_search([1, 3, 5, 7, 9], 5))  # 2
```
**Complexity:** Time O(log n), Space O(1)

---

### Q33: LRU Cache
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            # Update and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add new item
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)

# Using dict implementation
class LRUCacheDict:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))

# Example:
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)      # Evicts 2
print(lru.get(2))  # -1 (evicted)
```
**Complexity:** Time O(1), Space O(capacity)

---

### Q34: Sliding Window Maximum
```python
from collections import deque

def max_sliding_window(nums, k):
    """Find max in each sliding window of size k"""
    if not nums or k == 0:
        return []
    
    result = []
    dq = deque()  # Stores indices
    
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
# [3, 3, 5, 5, 6, 7]
```
**Complexity:** Time O(n), Space O(k)

---

### Q35-40: (Condensed)

**Q35: Word Ladder**
```python
def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    graph = defaultdict(list)
    wordList.append(beginWord)
    
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            graph[pattern].append(word)
    
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            for next_word in graph[pattern]:
                if next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    
    return 0
```

**Q36: Number of Islands**
```python
def numIslands(grid):
    if not grid:
        return 0
    
    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    
    return count
```

**Q37: Dijkstra's Algorithm**
```python
def dijkstra(graph, start, end):
    import heapq
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances[end]
```

**Q38: Group Anagrams**
```python
def groupAnagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)
    
    return list(groups.values())
```

**Q39: Longest Increasing Subsequence**
```python
def lengthOfLIS(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

**Q40: Edit Distance (Levenshtein)**
```python
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]
```
---