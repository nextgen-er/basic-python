if __name__ == "__main__":
    # ------------------------------------------------------------------
    # Amstrong Numbers
    # ------------------------------------------------------------------
    def is_amstrong(n):
        original = n
        digits = len(str(n))
        total = 0

        while n > 0:
            digit = n % 10
            total += digit**digits
            n //= 10

        return total == original

    print(is_amstrong(153))

    # ------------------------------------------------------------------
    # Fibonacci Numbers
    # ------------------------------------------------------------------
    def fibonacci(n):
        result = []

        a, b = 0, 1

        for _ in range(n):
            result.append(a)
            a, b = b, a + b

        return result

    print(fibonacci(10))
