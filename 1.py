def emp(a, b, c="INDIA"):
    print(a, b, c, sep="\n")


name = input()
employee_edu = input()
country = input()
if country == "INDIA" or country == "india":
    emp(name, employee_edu)
else:
    emp(name, employee_edu, country)
