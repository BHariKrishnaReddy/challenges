# Q1.  Write the UNIX command to count the occurrence of the word "Unix" in a given file. The file will be given as command line argument while the script containing your command will be run.


 grep -o -i unix | wc -l


# Q2. Write the unix command to count the number of words in the first 3 lines of a file.The file will be given as a command line argument when the script containing your command will run.


head -3|wc -w


# Q3. Write a shell script to find the sum of all even numbers from a list of given numbers. The script should first of all take the count of numbers to be added as user input followed by the numbers one by one.
# The output should print the following :
# Total = <Sum>


read n
awk '
    BEGIN
        {
            sum=0;
        }
        {
            if( $0%2==0)
                {
                    sum=sum+$0;
                }
        }
    END
        {
            print "Total","=",sum
        }'

# Q4. Student details are stored in a file in the following order with space as the delimiter:
# RollNo Name Score
# Write a unix command to find the name of the Student who has the highest score.
# The file will be given as a command line argument when the script containing your command will run.


sort -k3,3 -rn -t" " | head -n1 | awk '{print $2}'
