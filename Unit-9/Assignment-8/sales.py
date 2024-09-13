def display_title():
    print("The Quarterly Sales Program")


def get_sales():
    sales = []
    sales.append(int(input("Enter sales for q1: ")))
    sales.append(int(input("Enter sales for q2: ")))
    sales.append(int(input("Enter sales for q3: ")))
    sales.append(int(input("Enter sales for q4: ")))
    return sales


def get_total(sales):
    total = 0
    for i in sales:
        total += i
    return round(total, 2)

def average(sales, total):
    return round(total / len(sales), 2)


def lowest(sales):
    return min(sales)


def highest(sales):
    return max(sales)

    
def main():
    sales = get_sales()
    total = get_total(sales)
    print(f"\nTotal: {total}")
    print(f"Average Quarter: {average(sales, total)}")
    print(f"Lowest Quarter: {lowest(sales)}")
    print(f"Highest Quarter: {highest(sales)}")

if __name__ == "__main__":
    main()