# small-py-func

1. `time_3(credit)`:
   - Description: This function calculates the time based on a given credit value.
   - Parameters:
     - `Credit` (float): The credit value used to calculate the time.
   - Returns:
     - If the `credit` value is within the range of 9 (exclusive) to 13.5 (inclusive), the function returns a string representing the time in the format "hour:minute". The time is calculated by subtracting the `credit` value from 13.5 and converting it to minutes. For example, if the `credit` value is 10, the function returns "9:30" since 13.5 - 10 is 3.5, equal to 210 minutes (3.5 * 60), representing 9 hours and 30 minutes.
     - If the `credit` value is not within the specified range, the function returns the string `'not right time'`.

2. `time_2(credit)`:
   - Description: This function calculates the time based on a given credit value.
   - Parameters:
     - `credit` (float): The credit value used to calculate the time.
   - Returns:
     - If the `credit` value is within the range of 4 (exclusive) to 8.5 (inclusive), the function returns a string representing the time in the format "hour:minute". The time is calculated by subtracting the `credit` value from 8.5 and converting it to minutes. For example, if the `credit` value is 6, the function returns "9:30" since 8.5 - 6 is 2.5, equal to 150 minutes (2.5 * 60), representing 9 hours and 30 minutes.
     - If the `credit` value is not within the specified range, the function returns the string `'not right time'`.
