from utils.Result import Result

def test_result():
    result = Result().err("Error message")
    print(result.is_error())

if __name__ == "__main__":
    test_result()
    print("result.py passed")
