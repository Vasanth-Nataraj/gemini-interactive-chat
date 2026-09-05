'''import requests
base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print("Failed")
pokemon="pikachu"
info=get_pokemon_info(pokemon)
if info:
    print(f"Name: {info["name"]}")
    print(f"ID: {info["id"]}")'''
"""
Employee Performance and Payroll Analytics System
Single Unified Script for Capstone Review 1 (Phases 1 - 4: Units I, II, III)
"""

import math

# ==============================================================================
# 1. UNIT I & II: PAYROLL LOGIC, LAMBDAS, ATTENDANCE CALCULATIONS & DATA STRUCTURES
# ==============================================================================

# Lambda expressions for allowances and statutory deductions (Unit I)
calculate_hra = lambda basic: basic * 0.20  # House Rent Allowance (20%)
calculate_da = lambda basic: basic * 0.10   # Dearness Allowance (10%)
calculate_pf = lambda basic: basic * 0.12   # Provident Fund (12%)

TOTAL_WORKING_DAYS = 26

def calculate_income_tax(taxable_income: float) -> float:
    """Calculates income tax using standard progressive tax slabs (Unit I: Conditionals)."""
    if taxable_income <= 250000:
        return 0.0
    elif taxable_income <= 500000:
        return (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        return (250000 * 0.05) + ((taxable_income - 500000) * 0.20)
    else:
        return (250000 * 0.05) + (500000 * 0.20) + ((taxable_income - 1000000) * 0.30)

def calculate_attendance_penalty(days_present: int, basic_salary: float) -> tuple:
    """
    Calculates attendance rate and leave deductions (Unit II: Tuples).
    Allows 2 paid casual leaves; remaining unworked days are deducted.
    """
    days = max(0, min(days_present, TOTAL_WORKING_DAYS))
    attendance_pct = (days / TOTAL_WORKING_DAYS) * 100
    daily_rate = basic_salary / TOTAL_WORKING_DAYS
    leaves_taken = TOTAL_WORKING_DAYS - days
    
    unpaid_leaves = max(0, leaves_taken - 2)
    deduction = unpaid_leaves * daily_rate

    return round(attendance_pct, 2), round(deduction, 2)

def generate_payslip(emp_data: dict) -> dict:
    """Computes gross earnings, deductions, and net pay (Unit II: Dictionaries)."""
    basic_salary = emp_data.get("basic_salary", 0.0)
    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    pf = calculate_pf(basic_salary)
    
    gross_salary = basic_salary + hra + da
    
    rating = emp_data.get("performance_score", 3.0)
    if rating >= 4.5:
        bonus = basic_salary * 0.15
    elif rating >= 3.5:
        bonus = basic_salary * 0.08
    else:
        bonus = 0.0
        
    annual_taxable_est = (gross_salary + bonus - pf) * 12
    monthly_tax = calculate_income_tax(annual_taxable_est) / 12
    
    att_deduction = emp_data.get("attendance_deduction", 0.0)
    total_deductions = pf + monthly_tax + att_deduction
    net_salary = (gross_salary + bonus) - total_deductions

    return {
        "basic": basic_salary,
        "hra": hra,
        "da": da,
        "bonus": bonus,
        "gross": gross_salary + bonus,
        "pf": pf,
        "tax": monthly_tax,
        "attendance_penalty": att_deduction,
        "total_deductions": total_deductions,
        "net_salary": net_salary
    }

# ==============================================================================
# 2. UNIT III: STATISTICAL ANALYSIS & MODELING MODULE
# ==============================================================================

def calculate_mean(values: list) -> float:
    return sum(values) / len(values) if values else 0.0

def calculate_median(values: list) -> float:
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0
    return float(sorted_vals[mid])

def calculate_variance(values: list) -> float:
    n = len(values)
    if n < 2:
        return 0.0
    mean_val = calculate_mean(values)
    return sum((x - mean_val) ** 2 for x in values) / (n - 1)

def calculate_std_deviation(values: list) -> float:
    return math.sqrt(calculate_variance(values))

def calculate_pearson_correlation(x_vals: list, y_vals: list) -> float:
    """Calculates Pearson correlation coefficient (r) between two continuous variables."""
    if len(x_vals) != len(y_vals) or len(x_vals) < 2:
        return 0.0

    mean_x = calculate_mean(x_vals)
    mean_y = calculate_mean(y_vals)

    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, y_vals))
    denom_x = math.sqrt(sum((x - mean_x) ** 2 for x in x_vals))
    denom_y = math.sqrt(sum((y - mean_y) ** 2 for y in y_vals))

    if denom_x == 0 or denom_y == 0:
        return 0.0

    return numerator / (denom_x * denom_y)

def calculate_linear_regression(x_vals: list, y_vals: list) -> tuple:
    """Fits an OLS simple linear regression line: y = m*x + c."""
    if len(x_vals) != len(y_vals) or len(x_vals) < 2:
        return 0.0, 0.0

    mean_x = calculate_mean(x_vals)
    mean_y = calculate_mean(y_vals)

    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, y_vals))
    denominator = sum((x - mean_x) ** 2 for x in x_vals)

    if denominator == 0:
        return 0.0, mean_y

    slope = numerator / denominator
    intercept = mean_y - (slope * mean_x)

    return slope, intercept

# ==============================================================================
# 3. DATA REPOSITORY & APPLICATION INTERFACE
# ==============================================================================

# Core In-Memory Dataset (Nested Python Dictionaries & Lists)
employees_db = {
    101: {
        "name": "Srisudharsan V",
        "department": "Engineering",
        "experience_years": 4.5,
        "basic_salary": 65000.0,
        "days_present": 25,
        "performance_score": 4.2
    },
    102: {
        "name": "Vasanth Nataraj M",
        "department": "Analytics",
        "experience_years": 6.0,
        "basic_salary": 85000.0,
        "days_present": 26,
        "performance_score": 4.8
    },
    103: {
        "name": "Vignesh S",
        "department": "Engineering",
        "experience_years": 2.0,
        "basic_salary": 42000.0,
        "days_present": 21,
        "performance_score": 3.1
    },
    104: {
        "name": "Stalin N",
        "department": "HR",
        "experience_years": 5.0,
        "basic_salary": 58000.0,
        "days_present": 24,
        "performance_score": 3.9
    },
    105: {
        "name": "Sujan S",
        "department": "Analytics",
        "experience_years": 1.5,
        "basic_salary": 38000.0,
        "days_present": 20,
        "performance_score": 2.8
    }
}

def add_employee():
    print("\n--- Add New Employee ---")
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees_db:
            print(f"Error: Employee ID {emp_id} already exists.")
            return

        name = input("Enter Employee Name: ").strip()
        dept = input("Enter Department (Engineering/Analytics/HR): ").strip()
        exp = float(input("Enter Experience (Years): "))
        basic = float(input("Enter Monthly Basic Salary (INR): "))
        present = int(input("Enter Days Present (out of 26): "))
        perf = float(input("Enter Performance Score (1.0 to 5.0): "))

        employees_db[emp_id] = {
            "name": name,
            "department": dept,
            "experience_years": exp,
            "basic_salary": basic,
            "days_present": present,
            "performance_score": perf
        }
        print(f"Success: Record for {name} (ID: {emp_id}) added successfully.")
    except ValueError:
        print("Invalid input format. Please enter numeric values where expected.")

def view_all_employees():
    print("\n" + "=" * 90)
    print(f"{'ID':<6} {'Name':<18} {'Dept':<14} {'Exp(Yrs)':<10} {'Basic (INR)':<14} {'Present':<10} {'Rating':<6}")
    print("=" * 90)
    for emp_id, info in employees_db.items():
        print(f"{emp_id:<6} {info['name']:<18} {info['department']:<14} {info['experience_years']:<10.1f} {info['basic_salary']:<14.2f} {info['days_present']:<10} {info['performance_score']:<6.1f}")
    print("=" * 90)

def generate_employee_payroll():
    print("\n--- Generate Payroll & Payslip ---")
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id not in employees_db:
            print(f"Error: Employee ID {emp_id} not found.")
            return

        emp = employees_db[emp_id]
        att_pct, deduction = calculate_attendance_penalty(emp["days_present"], emp["basic_salary"])
        emp["attendance_deduction"] = deduction

        slip = generate_payslip(emp)

        print("\n" + "*" * 45)
        print(f"          PAYSLIP: {emp['name'].upper()} (ID: {emp_id})")
        print("*" * 45)
        print(f"Department          : {emp['department']}")
        print(f"Attendance Rate     : {att_pct}% ({emp['days_present']}/26 Days)")
        print(f"Performance Score   : {emp['performance_score']} / 5.0")
        print("-" * 45)
        print(f"Basic Salary        : INR {slip['basic']:>10.2f}")
        print(f"HRA (20%)           : INR {slip['hra']:>10.2f}")
        print(f"DA (10%)            : INR {slip['da']:>10.2f}")
        print(f"Performance Bonus   : INR {slip['bonus']:>10.2f}")
        print(f"Gross Earnings      : INR {slip['gross']:>10.2f}")
        print("-" * 45)
        print(f"Provident Fund (12%): INR {slip['pf']:>10.2f}")
        print(f"Income Tax (Est.)   : INR {slip['tax']:>10.2f}")
        print(f"Attendance Penalty  : INR {slip['attendance_penalty']:>10.2f}")
        print(f"Total Deductions    : INR {slip['total_deductions']:>10.2f}")
        print("=" * 45)
        print(f"NET TAKE-HOME SALARY: INR {slip['net_salary']:>10.2f}")
        print("=" * 45)

    except ValueError:
        print("Error: Invalid ID format.")

def run_statistical_analysis():
    print("\n" + "=" * 55)
    print("    UNIT III: STATISTICAL ANALYSIS & MODELING")
    print("=" * 55)

    salaries = [e["basic_salary"] for e in employees_db.values()]
    ratings = [e["performance_score"] for e in employees_db.values()]
    experience = [e["experience_years"] for e in employees_db.values()]
    attendance_rates = [(e["days_present"] / TOTAL_WORKING_DAYS) * 100 for e in employees_db.values()]

    print("\n1. DESCRIPTIVE STATISTICS (Salaries & Performance)")
    print(f" - Mean Basic Salary      : INR {calculate_mean(salaries):.2f}")
    print(f" - Median Basic Salary    : INR {calculate_median(salaries):.2f}")
    print(f" - Salary Std. Deviation  : INR {calculate_std_deviation(salaries):.2f}")
    print(f" - Mean Performance Score : {calculate_mean(ratings):.2f} / 5.0")
    print(f" - Median Performance     : {calculate_median(ratings):.2f} / 5.0")
    print(f" - Performance Std. Dev   : {calculate_std_deviation(ratings):.2f}")

    print("\n2. CORRELATION ANALYSIS (Pearson r)")
    r_exp_salary = calculate_pearson_correlation(experience, salaries)
    r_att_perf = calculate_pearson_correlation(attendance_rates, ratings)
    
    print(f" - Correlation (Experience vs Basic Salary)   : {r_exp_salary:+.4f}")
    print(f" - Correlation (Attendance Rate vs Rating)    : {r_att_perf:+.4f}")

    print("\n3. LINEAR REGRESSION PREDICTOR (Salary based on Experience)")
    slope, intercept = calculate_linear_regression(experience, salaries)
    print(f" - Regression Equation : Salary = ({slope:.2f} * Experience) + ({intercept:.2f})")
    
    try:
        test_exp = float(input("\nEnter Years of Experience to Predict Salary: "))
        predicted_salary = (slope * test_exp) + intercept
        print(f"Estimated Basic Salary for {test_exp} Yrs Exp: INR {predicted_salary:.2f}")
    except ValueError:
        print("Invalid number format.")

def main():
    while True:
        print("\n========================================================")
        print("  EMPLOYEE PERFORMANCE AND PAYROLL ANALYTICS SYSTEM   ")
        print("                 (Review 1: Units I - III)             ")
        print("========================================================")
        print(" 1. View All Employee Records (Collections)")
        print(" 2. Add New Employee Record")
        print(" 3. Compute Payroll & Generate Payslip (Unit I & II)")
        print(" 4. Run Statistical Analysis & Regression (Unit III)")
        print(" 5. Exit")
        print("========================================================")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_all_employees()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            generate_employee_payroll()
        elif choice == "4":
            run_statistical_analysis()
        elif choice == "5":
            print("\nExiting System. Execution completed.")
            break
        else:
            print("Invalid selection. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()