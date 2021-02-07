import pandas as pd
import numpy as np
import itertools
import random

def tripletQ(a, b, c, f, descriptionCol):
    """
    a: the ID # of the product that is presented
    b: the ID # of the 1st (left most on a horizontal multiple choice in a Qualtrics survey) product choice
    c: the ID # of the 2nd product choice
    f: txt file for survey
    """
    
    urla = data.loc[a, urlCol]
    urlb = data.loc[b, urlCol]
    urlc = data.loc[c, urlCol]
    
    descriptiona = data.loc[a, descriptionCol]
    descriptionb = data.loc[b, descriptionCol]
    descriptionc = data.loc[c, descriptionCol]
    
    namea = data.loc[a, nameCol]
    nameb = data.loc[b, nameCol]
    namec = data.loc[c, nameCol]
    
    questiontype = r'[[Question:MC:SingleAnswer:Horizontal]]'
    questionid = r'[[ID:%02d%02d%02d]]' % (a, b, c)
    questiontext = r'<center><strong>%s</strong><br><img src="%s" style="height:150px !important;"><br>Function: %s</center>' % (namea, urla, descriptiona)
    choiceinitial = r'[[AdvancedChoices]]'
    choice1recode = r'[[Choice:%02d]]' % (b)
    choice1 = r'<center><strong>%s</strong><br><img src="%s" style="height:150px !important;"><br>Function: %s</center>' % (nameb, urlb, descriptionb)
    choice2recode = r'[[Choice:%02d]]' % (c)
    choice2 = r'<center><strong>%s</strong><br><img src="%s" style="height:150px !important;"><br>Function: %s</center>' % (namec, urlc, descriptionc)
    pgbreak = r'[[PageBreak]]'
    f.write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (pgbreak, questiontype, questionid, questiontext, choiceinitial, choice1recode, choice1, choice2recode, choice2))
    
def fullSurvey(participantNum):
    surveyname = '../surveys/' + 'survey' + str(participantNum) + '.txt'
    survey=open(surveyname, "a+")
    survey.write('[[AdvancedFormat]]\n')
    
    # Insert consent form
    # Insert instructions
    # Begin task
    survey.write('[[Question:DB]]\nThe task will begin on the next page.\n')
    indSurvey = surveyTrips[participantNum]
    if participantNum % 2 == 0:
        # for x in range(0, len(indSurvey)):
            # y = len(indSurvey) - 1 - x
            # tripletQ(indSurvey[x][0],indSurvey[x][1][0],indSurvey[x][1][1], survey, "Overall function description")
            # tripletQ(indSurvey[y][0],indSurvey[y][1][0],indSurvey[y][1][1], survey, "Detailed function description")
            # if x % 4 == 0 and x !=0:
                # explanationQuestion(survey)            
            
        for x in range(0,len(indSurvey)):
            tripletQ(indSurvey[x][0],indSurvey[x][1][0],indSurvey[x][1][1], survey, "Overall function description")
            if x % 6 == 0 and x !=0:
              explanationQuestion(survey)
        random.Random(1).shuffle(indSurvey)
        for x in range(0,len(indSurvey)):
            tripletQ(indSurvey[x][0],indSurvey[x][1][0],indSurvey[x][1][1], survey, "Detailed function description")
            if x %  6== 0 and x !=0:
              explanationQuestion(survey)
    else:
        # for x in range(0, len(indSurvey)):
            # y = len(indSurvey) - 1 - x
            # tripletQ(indSurvey[y][0],indSurvey[y][1][0],indSurvey[y][1][1], survey, "Detailed function description")
            # if x % 4 == 0 and x !=0:
                # explanationQuestion(survey)
            # tripletQ(indSurvey[x][0],indSurvey[x][1][0],indSurvey[x][1][1], survey, "Overall function description")
            
        for x in range(0, len(indSurvey)):
            tripletQ(indSurvey[x][0],indSurvey[x][1][0],indSurvey[x][1][1], survey, "Detailed function description")
            if x % 6 == 0 and x !=0:
              explanationQuestion(survey)
        random.Random(2).shuffle(indSurvey)
        for x in range(0, len(indSurvey)):
            tripletQ(indSurvey[x][0],indSurvey[x][1][0],indSurvey[x][1][1], survey, "Overall function description")
            if x % 6 == 0 and x !=0:
              explanationQuestion(survey)
    #pb = r'[[PageBreak]]'
    #sline = r'[[Question:TE:SingleLine]]'
    #entemail = r'Please enter your email (we will send your $10 Amazon gift card to this email).'
    #survey.write('%s\n%s\n%s\n' % (pb, sline, entemail))
    survey.close()

def questionBank():
    questionbankname = '../surveys/' + 'questionbank' + '.txt'
    questionbank=open(questionbankname, "a+")
    questionbank.write('[[AdvancedFormat]]\n')
    questionbank.write('[[Question:DB]]\nFor all of the questions, select the item that is MORE functionally similar to the presented item, based on the available information\n')
    questionbank.write('[[Block]]\n')
    for t in triplets:
        tripletQ(t[0],t[1][0],t[1][1], questionbank, "Overall function description")
    questionbank.write('[[Block]]\n')
    for t in triplets:
            tripletQ(t[0],t[1][0],t[1][1], questionbank, "Detailed function description")
    questionbank.close()
    
def consentForm(textfile):
    qt = r'[[Question:MC:SingleAnswer:Vertical]]'
    qtext1 = 'We are interested in understanding the similarity between how products function.' + \
    'For this study, you will be presented with information relevant to a set of consumer products and asked to assess their similarity.' +  \
    'The results from the study may help us understand analogical inspiration for design.<br><br>' 
    qtext2 = 'The study should take you around 30 minutes to complete. You will receive $10 via an Amazon gift card for your participation after completion.' + \
    'Your participation in this research is voluntary. You have the right to withdraw at any point during the study.' + \
    'You can contact ananyan@berkeley.edu with any questions or concerns. Below you can find the detailed consent form.<br><br>'
    cform = '<a href="https://berkeley.qualtrics.com/CP/File.php?F=F_6Sh3RwKHDmMv5e6" target="_blank">Consent form<br></a><br>' 
    qtext3 = 'By clicking the button below, you acknowledge that you have read the consent form and agree to take part in this research.'
    choices = r'[[Choices]]'
    accept = r'Accept, begin the study'
    reject = r'I do not consent, I do not wish to participate'
    pgbreak = r'[[PageBreak]]'
    textfile.write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (qt, qtext1, qtext2, cform, qtext3, choices, accept, reject, pgbreak))
    
def explanationQuestion(textfile):
    qt = r'[[Question:TE:Essay]]'
    qtext = r'Please briefly explain why you selected the product to be more similar.'
    textfile.write('%s\n%s\n' % (qt, qtext))
       
if __name__=="__main__":
    data = pd.read_csv("../data/01_raw/functiondescriptions.csv")
    urlCol = "Image URL"
    nameCol = "Product"
    numRatings = 20 
    numParticipants = 162
    numProds = np.arange(20) 
    triplets_duplicates = [x for x in itertools.permutations(numProds, 3)] #list of all triplet permutations
    allCombs = [list(x) for x in itertools.combinations(numProds,2)]
    triplets = [(x,y) for x in numProds for y in allCombs if x not in y]
    random.Random(3).shuffle(triplets)
    surveyTrips = [triplets[i:i+numRatings] for i in range(0, numRatings*numParticipants, numRatings)]
    for i in range(0,numParticipants):
        fullSurvey(i)
    questionBank()