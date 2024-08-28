# Carson Chadwick
# Section 04
# Practice with regular expressions
import re

sInput = "Welcome to the world of problem solving using Python. Problem solving is something that is done on a daily basis. Whether you are trying to decide where to eat, who to date, should you get a pet and if so, what type of pet, or just trying to determine what to buy at the grocery store, you implement problem solving skills on a daily basis. This course will try and help you practice problem solving skills in a technical environment using a programming language. There are a variety of opinions as to the number of steps involved in solving a problem but for this course we will suggest following a seven step program. \
\
Identify the problem.\
Define the goal.\
Make a list of solutions.\
Evaluate feasibility each option.\
Choose your solution.\
Implement your solutio.\
Evaluate success of the solution (which in turn might take you back to step 1).\
\
The more an individual follows a logical process to solving a problem, the more experienced one will become in knowing what situations might work and what to avoid. If technologists can implement better problem solving skills, they might be able to reduce the number of failed technology projects, often due to being over budget or over schedule.  Take a moment and perform a web search for failed software projects and take note of the reason the project was deemed a failure. You might see common themes such as scope creep (continuous and uncontrolled growth in the project requirements usually due to poor identification of full problem), not solving the problem (not fit for the purpose), cost overruns, and the solution not meeting the goal or not solving the problem. Through well planned problem solving, users can identify what is trying to be solved, determine the desired outcome, create a list of options, evaluate each solution’s feasibility, and implementing the chosen the solution to solve the problem. Of course, after implementing the solution you need to make sure that the defined goal was achieved."    
# Display the number of occurrences the word "problem"
pattern = r'\bproblem\b'
lstNum = re.findall(pattern, sInput)
print(lstNum)
print("# of times: " + str(len(lstNum)))
# Display the first occurrence of the word "problem"
iFound = re.search(pattern, sInput)
print("Found at: " + str(iFound.start()))
# Display the number of occurrences of "he" within the string
pattern = r'he'
lstNum = re.findall(pattern, sInput)
print(lstNum)
print("# of times: " + str(len(lstNum)))
# Display the number of occurrences of a word that begins with "ne"
pattern = r'\bne\w*'
lstNum = re.findall(pattern, sInput)
print(lstNum)
print("# of times: " + str(len(lstNum)))
# Display the number of occurrences of the pattern "lem"
pattern = r'lem'
lstNum = re.findall(pattern, sInput)
print(lstNum)
print("# of times: " + str(len(lstNum)))