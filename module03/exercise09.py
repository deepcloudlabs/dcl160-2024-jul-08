customer = "11111111110,jack bauer,  100000\t\n,\ttr1,  \tIT:  SALES:HR,1956"
print(customer)
tokens = []
for token in customer.split(","):
    tokens.append(token.strip())
print(tokens)
identity, fullname, salary, *other = tokens
print(identity)
first_name, last_name = fullname.split(" ")
print(first_name)
print(last_name)
iban, departments, birth_year = other
print(iban)
print(birth_year)
primary_department, *other_departments = departments.split(":")
print(primary_department.strip())
for dept in other_departments:
    print(dept.strip())
