

def check_employee(path):
    roles=[ "administrator", "operator", "engineer"]
    with open(path,"rt") as file:
        for line in file:
            employee=line.strip().split(",")
            print(employee)
            if len(employee)<=1:
                print("No roles")
                print(False)
            valid_role=True
            for i in range(1,len(employee)):
                if employee[i] not in roles:
                    print("Invalid role")
                    valid_role=False
                    break
            if valid_role:
                print("valid roles")
                print(True)
            print(False)

check_employee("employee.csv")

