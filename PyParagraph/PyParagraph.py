def main():
    # Store the file path associated with the file (note the backslash may be OS specific) 
    #import os
    import string
    file = 'Resources/Adam.txt'

    # Open the file in "read" mode ('r') and store the contents in the variable "text"
    with open(file, 'r') as text:

        # Store all of the text inside a variable called "lines"
        lines = text.read()

        # Print the contents of the text file
        print("Paragraph Analysis")
        print("--------------------------------------------")
        appr_sen_count = lines.count(".")
        print("Approximate Sentance Count:", appr_sen_count)
        appr_word_count = len(lines.split())+1
        print('Approximate Word Count:', appr_word_count)
        total_badword_count=lines.count(".") + lines.count(",") + lines.count(" ")\
                            + lines.count("-")
        #print(len(lines))
        av_letter_count = (len(lines) - total_badword_count)/appr_word_count
        print("Average Letter Count:", av_letter_count)
        av_sen_len = appr_word_count/appr_sen_count
        print("Average Sentence Length:", av_sen_len)        

            
main()