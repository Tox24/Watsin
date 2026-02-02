from watsin_core import app


def sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    app.compile()
    app.toy_func()
    
    ret = sum(27843, 543275433)
    print(ret)
    
