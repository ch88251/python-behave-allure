def repeated_string(s, n):
    """
    Given a string {s} of lowercase English letters that is repeated infinitely many times,
    and an integer {n}, return the number of letter a's in the first {n} letters of the infinite string.
    :param s: A string that can repeat indefinitely
    :param n: The number of letters from the beginning of the string to evaluate
    :return: The number of times the letter 'a' appears in the first {n} letters.
    """
    result = s.count("a") * (n // len(s)) + sum(i == 'a' for i in s[:n % len(s)])
    return result
