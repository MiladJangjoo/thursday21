# You are given a string s representing an attendance record for a student where each character
#  signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.
# check= { 'A':0,
#         'L':0,
#         }

# def quality(str):
#     for i in str:
#         if i == 'A':
#             check['A'] += 1
#         elif i == 'L':
#             check['L'] += 1
#     if check['A'] >= 2:
#         return False
#     elif 'LLL' in str:
#         return False
#     else:
#         return True


# print(quality('AALLALA'))


def quality(str): 
    
       