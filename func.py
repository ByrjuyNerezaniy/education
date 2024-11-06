def count(start_date, finish_date):
    return finish_date - start_date
def main():
    n1, n2 = map(int, input().split())
    return count(n1, n2)
print(main())