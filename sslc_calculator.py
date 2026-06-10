def get_valid_mark(subject_name, max_marks):
    """
    Prompts the user to enter marks for a subject and validates the input.
    Ensures input is a float, non-negative, and does not exceed max_marks.
    """
    while True:
        try:
            val = input(f"Enter marks obtained in {subject_name} (Out of {max_marks}): ")
            marks = float(val)
            if marks < 0:
                print("❌ Marks cannot be negative. Please try again.")
            elif marks > max_marks:
                print(f"❌ Marks cannot exceed the maximum limit of {max_marks}. Please try again.")
            else:
                return marks
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def display_report(subjects_data, total_obtained, total_max):
    """
    Prints a formatted report of the marks, percentage, grade, and pass/fail status.
    """
    percentage = (total_obtained / total_max) * 100
    
    print("\n" + "=" * 50)
    print("               SSLC REPORT CARD")
    print("=" * 50)
    print(f"{'Subject':<25} | {'Marks Obtained':<15} | {'Max Marks':<10} | {'Status':<8}")
    print("-" * 50)
    
    all_passed = True
    for item in subjects_data:
        subj = item["name"]
        obtained = item["obtained"]
        max_m = item["max_marks"]
        
        # Calculate subject pass status (typically 35% is the passing mark)
        passing_min = max_m * 0.35
        status = "Pass" if obtained >= passing_min else "Fail"
        if status == "Fail":
            all_passed = False
            
        print(f"{subj:<25} | {obtained:<15.1f} | {max_m:<10.1f} | {status:<8}")
        
    print("-" * 50)
    print(f"{'TOTAL MARKS':<25} | {total_obtained:<15.1f} | {total_max:<10.1f} |")
    print("=" * 50)
    print(f"Overall Percentage: {percentage:.2f}%")
    
    # Determine the grade and overall result
    if not all_passed:
        result = "FAIL (Failed in one or more subjects)"
        grade = "N/A"
    else:
        result = "PASS"
        if percentage >= 85:
            grade = "Distinction"
        elif percentage >= 60:
            grade = "First Class"
        elif percentage >= 50:
            grade = "Second Class"
        elif percentage >= 35:
            grade = "Pass Class"
        else:
            grade = "Fail"
            result = "FAIL"

    print(f"Result Status:      {result}")
    if all_passed:
        print(f"Grade/Class:        {grade}")
    print("=" * 50 + "\n")

def run_karnataka_calculator():
    print("\n--- Karnataka Board SSLC Calculator ---")
    print("Note: First Language is out of 125, others are out of 100. Total marks: 625.")
    
    subjects = [
        {"name": "First Language", "max_marks": 125},
        {"name": "Second Language", "max_marks": 100},
        {"name": "Third Language", "max_marks": 100},
        {"name": "Mathematics", "max_marks": 100},
        {"name": "Science", "max_marks": 100},
        {"name": "Social Science", "max_marks": 100}
    ]
    
    subjects_data = []
    total_obtained = 0.0
    total_max = 0.0
    
    for sub in subjects:
        marks = get_valid_mark(sub["name"], sub["max_marks"])
        subjects_data.append({
            "name": sub["name"],
            "max_marks": sub["max_marks"],
            "obtained": marks
        })
        total_obtained += marks
        total_max += sub["max_marks"]
        
    display_report(subjects_data, total_obtained, total_max)

def run_tamilnadu_calculator():
    print("\n--- Tamil Nadu Board SSLC Calculator ---")
    print("Note: 5 subjects, each out of 100. Total marks: 500.")
    
    subjects = [
        {"name": "Language (Tamil/Other)", "max_marks": 100},
        {"name": "English", "max_marks": 100},
        {"name": "Mathematics", "max_marks": 100},
        {"name": "Science", "max_marks": 100},
        {"name": "Social Science", "max_marks": 100}
    ]
    
    subjects_data = []
    total_obtained = 0.0
    total_max = 0.0
    
    for sub in subjects:
        marks = get_valid_mark(sub["name"], sub["max_marks"])
        subjects_data.append({
            "name": sub["name"],
            "max_marks": sub["max_marks"],
            "obtained": marks
        })
        total_obtained += marks
        total_max += sub["max_marks"]
        
    display_report(subjects_data, total_obtained, total_max)

def get_kerala_grade_and_points(obtained, max_m):
    percentage = (obtained / max_m) * 100
    if percentage >= 90:
        return "A+", 9
    elif percentage >= 80:
        return "A", 8
    elif percentage >= 70:
        return "B+", 7
    elif percentage >= 60:
        return "B", 6
    elif percentage >= 50:
        return "C+", 5
    elif percentage >= 40:
        return "C", 4
    elif percentage >= 30:
        return "D+", 3
    elif percentage >= 20:
        return "D", 2
    else:
        return "E", 1

def display_kerala_report(subjects_data, total_obtained, total_max):
    print("\n" + "=" * 65)
    print("               KERALA SSLC REPORT CARD")
    print("=" * 65)
    print(f"{'Subject':<25} | {'Marks':<8} | {'Max':<5} | {'Grade':<6} | {'Points':<6} | {'Status':<6}")
    print("-" * 65)
    
    all_passed = True
    total_gp = 0
    for item in subjects_data:
        subj = item["name"]
        obtained = item["obtained"]
        max_m = item["max_marks"]
        
        grade, gp = get_kerala_grade_and_points(obtained, max_m)
        total_gp += gp
        status = "Pass" if gp >= 3 else "Fail"
        if status == "Fail":
            all_passed = False
            
        print(f"{subj:<25} | {obtained:<8.1f} | {max_m:<5.1f} | {grade:<6} | {gp:<6} | {status:<6}")
        
    print("-" * 65)
    print(f"{'TOTAL MARKS':<25} | {total_obtained:<8.1f} | {total_max:<5.1f} | {'':<6} | {total_gp:<6} |")
    print("=" * 65)
    
    overall_percentage = (total_obtained / total_max) * 100
    gpa = total_gp / len(subjects_data)
    result = "PASS" if all_passed else "FAIL (Failed in one or more subjects)"
    
    print(f"Overall Percentage:    {overall_percentage:.2f}%")
    print(f"Total Grade Points:    {total_gp} / {len(subjects_data) * 9}")
    print(f"Grade Point Average:   {gpa:.2f}")
    print(f"Result Status:         {result}")
    print("=" * 65 + "\n")

def run_kerala_calculator():
    print("\n--- Kerala Board SSLC Calculator ---")
    print("Note: Total marks: 640 (English, Maths, Social Science out of 100, IT out of 40, others out of 50).")
    
    subjects = [
        {"name": "First Language Part 1", "max_marks": 50},
        {"name": "First Language Part 2", "max_marks": 50},
        {"name": "Second Language (English)", "max_marks": 100},
        {"name": "Third Language (Hindi)", "max_marks": 50},
        {"name": "Physics", "max_marks": 50},
        {"name": "Chemistry", "max_marks": 50},
        {"name": "Biology", "max_marks": 50},
        {"name": "Mathematics", "max_marks": 100},
        {"name": "Social Science", "max_marks": 100},
        {"name": "Information Technology", "max_marks": 40}
    ]
    
    subjects_data = []
    total_obtained = 0.0
    total_max = 0.0
    
    for sub in subjects:
        marks = get_valid_mark(sub["name"], sub["max_marks"])
        subjects_data.append({
            "name": sub["name"],
            "max_marks": sub["max_marks"],
            "obtained": marks
        })
        total_obtained += marks
        total_max += sub["max_marks"]
        
    display_kerala_report(subjects_data, total_obtained, total_max)

def run_custom_calculator():
    print("\n--- Custom Board SSLC Calculator ---")
    
    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects <= 0:
                print("❌ Number of subjects must be greater than 0.")
            else:
                break
        except ValueError:
            print("❌ Invalid input! Please enter an integer number.")
            
    subjects_data = []
    total_obtained = 0.0
    total_max = 0.0
    
    for i in range(1, num_subjects + 1):
        name = input(f"Enter the name of Subject {i}: ").strip()
        if not name:
            name = f"Subject {i}"
            
        while True:
            try:
                max_marks = float(input(f"Enter maximum marks for {name}: "))
                if max_marks <= 0:
                    print("❌ Maximum marks must be greater than 0.")
                else:
                    break
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
                
        marks = get_valid_mark(name, max_marks)
        subjects_data.append({
            "name": name,
            "max_marks": max_marks,
            "obtained": marks
        })
        total_obtained += marks
        total_max += max_marks
        
    display_report(subjects_data, total_obtained, total_max)

def main():
    print("==================================================")
    print("          SSLC PERCENTAGE CALCULATOR")
    print("==================================================")
    
    while True:
        print("Choose your examination board / mode:")
        print("1. Karnataka Board (KSEEB - Total 625 Marks)")
        print("2. Tamil Nadu Board (TNDGE - Total 500 Marks)")
        print("3. Kerala Board (Total 640 Marks)")
        print("4. Custom Board (Specify your own subjects & marks)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            run_karnataka_calculator()
        elif choice == '2':
            run_tamilnadu_calculator()
        elif choice == '3':
            run_kerala_calculator()
        elif choice == '4':
            run_custom_calculator()
        elif choice == '5':
            print("\nThank you for using the SSLC Percentage Calculator. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice! Please select an option between 1 and 5.\n")

if __name__ == "__main__":
    main()
