import time


def retry_operation(max_attempts=3, delay=2):
    """Retry a simulated operation and return True if it succeeds."""
    attempt = 1

    while attempt <= max_attempts:
        print(f"Attempt {attempt} of {max_attempts}...")

        # Simulate a temporary failure on attempts one and two.
        if attempt < 3:
            print(f"Attempt {attempt} failed: temporary simulated error.")
        else:
            print(f"Operation succeeded on attempt {attempt}.")
            return True

        if attempt < max_attempts:
            time.sleep(delay)

        attempt += 1

    print(f"Operation failed after {max_attempts} attempt(s).")
    return False


def main():
    retry_operation()


if __name__ == "__main__":
    main()
