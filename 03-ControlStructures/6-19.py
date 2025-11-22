#Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. 
#Write a program that prints a survey consisting of three questions. Save the answers to logical type variables.
#Then view the survey result. Sample result:

#SURVEY Are you interested in computer science? (y/n): y
#Do you like playing computer games? (y/n): n
#Do you have an Instagram account? (y/n): y

#SURVEY RESULTS Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes
def run_survey():
    print("SURVEY")
    
    # Question 1
    q1_input = input("Are you interested in computer science? (y/n): ").strip().lower()
    # Save the answer as a boolean (True for 'y', False otherwise)
    # This stores the *meaning* of the answer, not the raw 'y'/'n' string.
    is_interested_in_cs = (q1_input == 'y') 

    # Question 2
    q2_input = input("Do you like playing computer games? (y/n): ").strip().lower()
    is_interested_in_games = (q2_input == 'y')

    # Question 3
    q3_input = input("Do you have an Instagram account? (y/n): ").strip().lower()
    has_instagram = (q3_input == 'y')

    print("\nSURVEY RESULTS")

    # Display the results
    # Use a ternary operator or if-else blocks to convert boolean back to "Yes"/"No" strings for display
    
    # Method 1: Using a helper function or direct logic (clearer for beginners)
    
    q1_result_str = "Yes" if is_interested_in_cs else "No"
    q2_result_str = "Yes" if is_interested_in_games else "No"
    q3_result_str = "Yes" if has_instagram else "No"

    print(f"Interested in computer science: {q1_result_str}")
    print(f"Playing computer games: {q2_result_str}")
    print(f"Has an Instagram account: {q3_result_str}")

# Run the survey program
if __name__ == "__main__":
    run_survey()