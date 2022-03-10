from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
import nltk
import pprint
from nltk.tree import *
import re
import os

sen1 = "Education is a perpetual topic of our times. One indisputable fact is that nowadays some students will choose some popular majors while they are enrolled in the university. According to the graph about the number of bachelor's degrees given across five majors in 2011 to 2012 in USA, we can see that there are 367,000 students choose to study in business, the population of history is equal to the education, the health profession is little lower than these two one. However, there are only 109,000 students that are given the degree of psychology. As for this picture, I personally believe that students are willing to choose the popular major because it is easier to study and has more chance to find a better job. First of all, it is safe to say that the easiest major appeals to more students. To be specific, like the business, we can just get a bachelor degree and come to the career fair to look for a job with the working experience or projects we have had since the four years studying in university. However, majors that should learn numerous theories such as the psychology and health profession should have more time to apply it, so after they graduate as the undergraduate students, they cannot easily find a job for the lack of experience and application, thus some students will choose to study for the master degree even the doctor. My friend's brother  is a great example to explain this statement. When he graduated with a bachelor degree from the college of business, he just went to the job fair and looked for the job he wanted. Because of his major business and his experience about the internship, he quickly found the job in a large company. However, his friends Jacob, who is majoring in history, decided to study for the master degree because he did not have some experience of internship, and he did not know where he could apply because of the too professional major and content. To sum up, it is easier for students to choose the major that they can study less and quickly find the job. In addition, it is undeniable that students are willing to work with a high-salary job. To illustrate, taking business as an example. Nowadays an increasing number of companies have been set up, so they need more workers to help them establish these companies. According to this statement, the employer are more likely to hire some students whose major is business, because they are taught how to manage a company and how to attain the balance between the income and outcome. To compare with, these other major such as education, psychology and history contain too many theories and the students graduate from these majors are not needed by a company. A recent research, conducted by the China Daily, proved that during the past three years, 71% of the companies were looking for the business-major students, and only 6% of students majoring in the history were hired. These figures show that the business students are paid more attention by companies, so they have more chance and more probability to be hired during the career fair. Therefore, based on this situation, students prefer the business major rather than these theory major. Finally, although some students will choose the major that they are interested in, they are not free to say that they are not concerned about the chances of finding a job. Consequently, I still firmly advocate that the major becomes popular because of the easier study process and the more chance of finding a job."
sen2 = "Education is a perpetual topic of our times. One heated-discussed issue is that there are numerous students choosing to study abroad nowadays. As for the research conducted by the Institute of International Education, shows that there were 304,040 students choosing to study abroad in China from 2014 to 2015, which was extremely more than Canada that only have 27240 students. And the second large population of studying abroad was India, which had 132,888 students. The number of students in South Korea are almost equal to the Saudi Arabia, which is 63,710 and 59,945. According to the research about studying abroad, I personally believe that the reason why students choose to study abroad is looking for the better education and more chances to work. First of all, it is undeniable that students are willing to study in the higher educational environment. To be specific, in China the best university is Beijing University, which ranks in 130 in US News World University Rank. However, the top 100 universities are more located in United States, so in order to get higher education, some students choose to study abroad and most of them come to America. Taking my friends as an example. While she was studying in high school, she was the top student of our class, also she got good grades in the University Enrollment Test. However, she was interested in aerospace engineering, which was not very well in our country. So during the summer vacation she started studying for English and prepared to study abroad. Now she is studying in Purdue University, and she thinks while chatting with the friends in our domestic universities with the same major, she learns more knowledge and gets more chance to internship, so she is happy to make the decision about studying abroad. In a way, studying abroad can help students get higher education and learn more knowledge. In addition, it is safe to say that studying abroad may have more chances to find a better job. To illustrate, nowadays, in China and India, numerous jobs in many aspects are fulfilling with the employees so there are no empty for students who just graduated from university to work. To compare with, it has more chances and more objective for students to choose in the United States. Because of the rapidly developing society, there are numerous companies hiring students to work with them in many majors such as business, computer science, mechanical engineering an so on. Students that studying abroad can better adopt the environment and the study methods so they will face little difficulties in finding jobs after they graduate. A 2016 research, conducted by Ministry of Education, proved that 63% of students that studying abroad found jobs in the United States and only 18% of students that studying in the domestic universities found jobs after graduating. These figures show that there are more chances for students to seek for a job in the United States. Therefore, it is better for students to find a better job in the United States so they choose to study abroad. Finally, although some students may think that their hometowns are appropriate for them to study, consequently, I still firmly assert that it is better to study abroad."

"""
if len(sen1)<len(sen2):
    print("Sentence 2 was expanded, and/or Sentence 1 had deleted items.")
else:
    print("Sentence 1 was expanded, and/or Sentence 2 had deleted items.")
"""

parser_folder = "/Users/Ivana/Downloads/stanford-parser-full-2015-12-09/"

parser_jar = parser_folder + "stanford-parser.jar"
models_jar = parser_folder + "stanford-parser-3.6.0-models.jar"

const_parser = StanfordParser(parser_jar, models_jar) #model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
dep_parser = StanfordDependencyParser(parser_jar, models_jar)
const_output1 = const_parser.raw_parse(sen1.lower())
const_output2 = const_parser.raw_parse(sen2.lower())
tree = []
TreeN1 = []
TreeN2 = []
tree1 = []
TreeA1 = []
TreeA2 = []
TreeAj1 = []
TreeAj2 = []
for item in const_output1:
    #print("Here is the syntax tree: ", '\n', item, '\n')
    tree.append(item)
    TreeV1 = re.findall('\((VB|VBD|VBG|VBN|VBP|VBZ)', str(item))
    TreeN1 = re.findall('\((NN|NNS|NNP|NNPS)', str(item))
    TreeA1 = re.findall('\((RB|RBR|RBS)', str(item))
    TreeAj1 = re.findall('\((JJ|JJR|JJS)', str(item))
print("Task 1 has ", str(len(TreeV1)), " verbs, ", str(len(TreeN1)), " nouns, ", str(len(TreeA1)), " adverbs, and ", str(len(TreeAj1)), "adjectives.")
for item in const_output2:
    #print("Here is the syntax tree: ", '\n', item, '\n')
    tree.append(item)
    TreeV2 = re.findall('\((VB|VBD|VBG|VBN|VBP|VBZ)', str(item))
    TreeN2 = re.findall('\((NN|NNS|NNP|NNPS)', str(item))
    TreeA2 = re.findall('\((RB|RBR|RBS)', str(item))
    TreeAj2 = re.findall('\((JJ|JJR|JJS)', str(item))

print("Task 2 has " + len(TreeV2) + " verbs, " + len(TreeN2) + " nouns, " + len(TreeA2) + " adverbs, and " + len(TreeAj2) + "adjectives.")

""""
if len(TreeV1)<len(TreeV2):
    print("Sentence 2 has ", len(TreeV2)-len(TreeV1),  "additional verb(s).")
else:
    print("Sentence 1 has", len(TreeV1)-len(TreeV2),  "additional verb(s).")

if len(TreeN1)<len(TreeN2):
    print("Sentence 2 has ", len(TreeN2)-len(TreeN1),  "additional noun(s).")
else:
    print("Sentence 1 has", len(TreeN1)-len(TreeN2),  "additional noun(s).")

if len(TreeN1)<len(TreeN2):
    print("Sentence 2 has ", len(TreeN2)-len(TreeN1),  "additional noun(s).")
else:
    print("Sentence 1 has", len(TreeN1)-len(TreeN2),  "additional noun(s).")

if len(TreeA1)<len(TreeA2):
    print("Sentence 2 has ", len(TreeA2)-len(TreeA1),  "additional adverb(s).")
else:
    print("Sentence 1 has", len(TreeA1)-len(TreeA2),  "additional adverb(s).")

if len(TreeAj1)<len(TreeAj2):
    print("Sentence 2 has ", len(TreeAj2)-len(TreeAj1),  "additional adjective(s).")
else:
    print("Sentence 1 has", len(TreeAj1)-len(TreeAj2),  "additional adjective(s).")
"""
