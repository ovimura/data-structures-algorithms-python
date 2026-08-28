

arr = ["abc", "def", "ghi", "abc"]

def decorators(f):
    def wrapper(args):
        s = set()
        for i in arr:
            s.add(i)
        s = sorted(s)
        rr = f(args)
        r = "".join(s)
        return r
    return wrapper


@decorators
def foo(a1="i"):
    return "".join(arr)


def main():
    print("foo: ", foo(4))


if __name__ == "__main__":
    main()

