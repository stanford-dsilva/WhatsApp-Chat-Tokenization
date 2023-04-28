# Importing Libraries
import calendar
import datetime
import emojis
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Defining paths, Ideally I would have liked to export the chat in the script but that requires other APIs
# Can be explored later
path = "Chat History/"
filename = "_chat.txt"
# Defining variables
My_Words = []
Person1_Words = []
My_Emojis = []
Person1_Emojis = []
Your_Name = "Stanford Dsilva"
Contact1_Name = "Mary Jane"

# Opening files for formatting
searchfile = open(path+filename,encoding="utf-8")
writefile = open(path+'Chat_Output.txt',"w",encoding="utf-8")

# Starting Tokenization
datetime_object = datetime.datetime.now()
print("Start Time:")
print(datetime_object)


# Defining additional stopwords that you may want to exclude from your analysis
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
new_stopwords = ["I","u","to","omitted","will","\u200eimage","\u200esticker","’"
    ,",","it","d","me","No","?","was","have","n","'s","U","is","no","ur","not","Ya"
    ,"in","Ok","dat","dnt","a","my","do","b","of","But","Wat","her","she","you","It","now"
    ,"can","n't","for","so","knw","She","wat","too"]
stop_words = stop_words.union(new_stopwords)

# Doing basic cleansing on data
for line in searchfile:
    if " omitted" in line:
        Datetime = datetime.datetime.strptime(line[2:22], "%d/%m/%Y, %H:%M:%S")
        Day_Of_Week = calendar.day_name[Datetime.weekday()]
        Date = Datetime.strftime("%Y-%m-%d")
        Time = Datetime.strftime("%H:%M:%S")
        temp_var_1 = line[24:].split(':')
        Author = temp_var_1[0]
        Chat_Text = temp_var_1[1]
    elif line.startswith('['):
        Datetime = datetime.datetime.strptime(line[1:21], "%d/%m/%Y, %H:%M:%S")
        Day_Of_Week = calendar.day_name[Datetime.weekday()]
        Date = Datetime.strftime("%Y-%m-%d")
        Time = Datetime.strftime("%H:%M:%S")
        temp_var_1 = line[23:].split(':')
        Author = temp_var_1[0]

        if len(temp_var_1) == 2:
            Chat_Text = temp_var_1[1]
        else:
            temp_var_1.pop(0)
            Chat_Text = ':'.join(temp_var_1)
    else:
        Chat_Text = line

# This is the main piece of code where words are tokenized
    if Author == Your_Name:
        tokenize_word = word_tokenize(Chat_Text)
        for w in tokenize_word:
            if w.lower() not in stop_words:
                My_Words.append(w)
            if emojis.count(w.lower()) > 0:
                for a in emojis.get(w.lower()):
                    My_Emojis.append(a)

    if Author == Contact1_Name:
        tokenize_word = word_tokenize(Chat_Text)
        for w in tokenize_word:
            if w.lower() not in stop_words:
                Person1_Words.append(w)
            if emojis.count(w.lower()) > 0:
                for a in emojis.get(w.lower()):
                    Person1_Emojis.append(a)

# Writing the cleansed output into a separate file for additional analysis
    output_var = str(Datetime)+"|"+str(Time)+"|"+Day_Of_Week+"|"+Author+"|"+Chat_Text
    writefile.write(output_var)
searchfile.close()


# Frequency Distribution of all Words
Your_Name_Fd = nltk.FreqDist(My_Words)
Your_Name_Emoji_Fd = nltk.FreqDist(My_Emojis)
Contact1_Name_Fd = nltk.FreqDist(Person1_Words)
Contact1_Name_Emoji_Fd = nltk.FreqDist(Person1_Emojis)


print(Your_Name+"'s Most Common words:")
Your_Name_Fd.tabulate(10) #print(Your_Name_Fd.most_common(10))
print(Your_Name+"'s Most Common Emojis:")
Your_Name_Emoji_Fd.tabulate(10) #print(Your_Name_Emoji_Fd.most_common(10))


print("\n\n"+Contact1_Name+"'s Most Common words:")
Contact1_Name_Fd.tabulate(10) #print(Contact1_Name_Fd.most_common(10))
print(Contact1_Name+"'s Most Common Emojis:")
Contact1_Name_Emoji_Fd.tabulate(10) #print(Contact1_Name_Emoji_Fd.most_common(10))



datetime_object = datetime.datetime.now()
print("End Time:")
print(datetime_object)
