from pathlib import Path
import os

"""
--- 1 ---
This is a simple log analyzer that reads a log file and prints each line (Just for practice).
"""

def analyze_log_1(file_path):
    
    with open(file_path, 'r') as file:
        for line in file:
            print(line)


"""
--- 2 ---
This counts the successful and failed login attempts in the log file.
"""

def count_attempts(file_path):
    
    with open(file_path, 'r') as file:
        success = 0
        failed = 0
        for line in file:
            if "LOGIN_SUCCESS" in line:
                success += 1
            elif "LOGIN_FAILED" in line:
                failed += 1
        return success, failed
        

"""
--- 3 ---
This  keeps track of how many times each user failed to log in
"""

def get_user(log):
    temp = log.split()
    return temp[3]

def users_failed_attempts(file_path):
    with open(file_path, 'r') as file:
        failed_logins = {}
        
        for line in file:
            user = get_user(line)
            
            if user not in failed_logins:
                failed_logins[user] = 0
            
            if "LOGIN_FAILED" in line:
                failed_logins[user] += 1

    return failed_logins
    

"""
--- 4 ---
Main: Analyzes all activity
Displays number of successful and failed login attemps.
Displays number of failed attempts per user
Detects suspicious activity from users having too many failed login attempts
"""

def analyze(log_file_path,func):
    #func = input("Enter the function you want to run on each log file:\n1. Count successful and failed login attempts\n2. Count failed login attempts per user\n3. Find suspicious users\n4. Analyze all activity\n")
    
    if func == "1":
        success, failed = count_attempts(log_file_path)
        print("Successful logins:", success)
        print("Failed logins:", failed)

    elif func == "2":
        failed_logins = users_failed_attempts(log_file_path)
        
        print("=====================\nFailed logins per user\n---------------------" )
        for person in failed_logins:
            if failed_logins[person] > 0:
                print(person + " : ", failed_logins[person])

    elif func == "3":
        failed_logins = users_failed_attempts(log_file_path)
        for person in failed_logins:
            if failed_logins[person] > 3:
                print(person + " has suspicious activity with " + str(failed_logins[person]) + " failed login attempts.")

    elif func == "4":
        success, failed = count_attempts(log_file_path)
        print("=====================\nSuccessful and Failed Login Attempts\n---------------------")
        print("Successful logins:", success)
        print("Failed logins:", failed)

        failed_logins = users_failed_attempts(log_file_path)
        print("=====================\nFailed logins per user\n---------------------" )
        for person in failed_logins:
            if failed_logins[person] > 0:
                print(person + " : ", failed_logins[person])

        print("=====================\nSuspicious Users\n---------------------")
        for person in failed_logins:
            if failed_logins[person] > 3:
                print(person + " has suspicious activity with " + str(failed_logins[person]) + " failed login attempts.")

    else:
        print("Invalid input. Please enter 1, 2, or 3.")


""" 
--- 5 ---
This is the main entry point of the program. It allows the user to enter a folder containing multiple log files and analyzes each file in the folder. It also allows the user to specify which analysis function to run on each log file.
"""

if __name__ == "__main__":
    log_folder_path = input("Enter the path to the folder containing log files: ")
    f = input("Enter the function you want to run on each log file:\n1. Count successful and failed login attempts\n2. Count failed login attempts per user\n3. Find suspicious users\n4. Analyze all activity\n")
    for log_file in os.listdir(log_folder_path):
        log_file_path = os.path.join(log_folder_path, log_file)
        print(f"\nAnalyzing log file: {log_file}")
        analyze(log_file_path, f)




