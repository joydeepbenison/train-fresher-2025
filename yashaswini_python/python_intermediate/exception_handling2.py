def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error:", e)
    except TypeError as e:
        print("Type Error:", e)
    else:
        print("Division Result:", result)
    finally:
        print("Execution finished.")

divide(10, 2)
divide(10, 0)
divide(10, "a")

