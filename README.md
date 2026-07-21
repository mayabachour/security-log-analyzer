# Security Log Analyzer

A Python project that analyzes login log files and detects suspicious login activity.

## Features

- Counts successful login attempts
- Counts failed login attempts
- Displays failed login attempts per user
- Detects users with suspicious numbers of failed login attempts
- Supports analyzing multiple log files in a folder

## Technologies Used

- Python 3
- Dictionaries
- File handling
- Functions
- Loops

## Sample Log Format

2026-07-21 08:15:03 LOGIN_SUCCESS alice
2026-07-21 08:16:11 LOGIN_FAILED admin

## Example Output

Successful logins: 8
Failed logins: 12

Failed logins per user
admin : 8
eve : 2
charlie : 1

Suspicious Users
admin has suspicious activity with 8 failed login attempts.


## Future Improvements

- Analyze live log files
- Detect suspicious IP addresses
- Export reports to CSV
- Support different log formats

