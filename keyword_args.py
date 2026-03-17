def f(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
f(name="Alice", age=30, city="New York")