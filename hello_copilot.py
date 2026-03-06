# 定义一个函数，接收一个名字参数，并返回一句热情的问候语，包含感叹号
def greet(name):
    return f"Hello, {name}!"
# 调用函数并打印结果
print(greet("Alice"))
print(greet("Bob"))
print(greet("GitHub Copilot"))

# 如果名字是空的，返回 "Hello, Stranger!"
def greet(name):
    if not name:
        return "Hello, Stranger!"
    return f"Hello, {name}!"
# 调用函数并打印结果
print(greet(""))
print(greet("Charlie"))
