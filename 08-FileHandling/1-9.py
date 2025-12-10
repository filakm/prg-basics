###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
   content = file.read()
   con = content.splitlines()
   for line in con:
      if job_title in line:
        print(line)
