# Capstone Project
For this Capstone Project, assume that you have been approached by a small financial company and asked to create a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
- Create a new Python file in this folder called finance_calculators.py.
- At the top of the file include the line: import math.
- Write the code that will do the following:
  
1. The user should be allowed to choose which calculation they want to do. The first output that the user sees when the program runs should look like this:
> - investment - to calculate the amount of interest you'll earn on your investment
> - bond - to calculate the amount you'll have to pay on a home loan
> - Enter either 'investment' or 'bond' from the menu above to proceed:

2. How the user capitalises on their selection should not affect how the program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc., should all be recognised as valid entries. If the user doesn’t type in a valid input, show an appropriate error message.

3. If the user selects ‘investment’, do the following:
- Ask the user to input:
  1. The amount of money that they are depositing.
  2. The interest rate (as a percentage). Only the number of the interest rate should be entered — don’t worry about having to deal with the added ‘%’, e.g. The user should enter 8 and not 8%.
  3. The number of years they plan on investing.
  4. Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest. Depending on whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period, at the specified interest rate. 
  5. Print out the answer!

4. If the user selects ‘bond’, do the following:
- Ask the user to input:
  1. The present value of the house. e.g. 100000
  2. The interest rate. e.g. 7
  3. The number of months they plan to take to repay the bond. e.g. 120
  4. Calculate how much money the user will have to repay each month and output the answer.
