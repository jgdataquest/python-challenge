import string
import sys

file = 'Resources/Adam.txt'
sys.stdout = open('PyParagraph.out', 'w')
    # Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the output
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
