import pandas as pd
import os

 


def survey2trip(filename, fileout1, fileout2, participantNum):
    '''
    Return txt of triplets in the following form (based on MATLAB script): (a,b,c) where a is more similar to b than it is to c
    filename is the name of the file from which the survey results are being read
    fileout1 is the name of the file to which the triplets are being written for the overall function description
    fileout2 is the name of the file to which the triplets are being written for the detailed function description
    participantNum is the participant number which indicates whether the overall or detailed function description was presented first 
    '''
    fo1 = open(fileout1, "a+")
    fo2 = open(fileout2, "a+")
    results = pd.read_csv("../data/03_results/surveydata/%s" % (filename)) 
    results = results[results["Finished"] == "1"] #check for finished
    results = results[results["Q1"] == "1"]
    results = results.reset_index(drop=True)
    startCol = 18
    cols = [7,14,21]
    data1 = results.iloc[:,startCol:startCol+23]
    data2 = results.iloc[:,startCol+23:startCol+46]
    data1 = data1.drop(data1.columns[cols], axis = 1)
    data2 = data2.drop(data2.columns[cols], axis = 1)

    # compare answer (in response row) with col name
    # swap in the final triplet if needed
    # return tuple of properly formatted triplets
    
    if participantNum % 2 == 0:
    # shorter description is first 20, longer description is second 20
    
        for n in data1.columns:
            final_triplet = switchtriplet(n, data1)
            fo1.write(','.join(str(t) for t in final_triplet) + '\n')
        fo1.close()
    
        for n in data2.columns:
            final_triplet = switchtriplet(n, data2)
            fo2.write(','.join(str(t) for t in final_triplet) + '\n')
        fo2.close()
    
    else:
    # longer description is first 20, shorter description is second 20
    
        for n in data1.columns:
            final_triplet = switchtriplet(n, data1)
            fo2.write(','.join(str(t) for t in final_triplet) + '\n')
        fo2.close()
    
        for n in data2.columns:
            final_triplet = switchtriplet(n, data2)
            fo1.write(','.join(str(t) for t in final_triplet) + '\n')
        fo1.close()
       
    
def switchtriplet(name, data):
    trip_displayed = [name[i:i+2] for i in range(0, len(name), 2)]
    if int(data.loc[0, name]) == int(trip_displayed[2]):
        final_triplet = (str(int(trip_displayed[0])),str(int(trip_displayed[2])), str(int(trip_displayed[1])))
    else:
        final_triplet = (str(int(trip_displayed[0])), str(int(trip_displayed[1])), str(int(trip_displayed[2])))
    return final_triplet
    
    
if __name__=="__main__":
    directory = "../data/03_results/surveydata"
    for f in os.listdir(directory):
        num = int(f[12:14]) #replace with whereever the survey number is listed in the filename 
        response1 = '../data/03_results/tripletresponses/overall/' + 'response' + str(num) + '.txt'
        response2 = '../data/03_results/tripletresponses/detailed/' + 'response' + str(num) + '.txt'
        survey2trip(f, response1, response2, num)