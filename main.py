from functools import wraps

request_count = 0


def main():
    for i in range(27):
        method_to_be_counted(i)

    print(f"Number of requests called: {request_count}")


# TODO: Add retry decorator for retrying number, raise proper exceptions using
# try catch methods and raise exception
# if the request is not failing then return the main function


def count_requests(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global request_count
        request_count += 1

        return func(*args, **kwargs)

    return wrapper


@count_requests
def method_to_be_counted(i):
    yield


if __name__ == "__main__":
    main()
