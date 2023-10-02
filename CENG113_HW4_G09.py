#280201082-Nurcan Yıldız
#280201057-Damla Keleş
#CENG113-HW4
import csv
from typing import final
gene_dict={}
frag_dict = {}

def main():
    file_path= open("input.txt", "r")                     #the file is opened with the 'r'ead  mode
    gene_dict=read_genes(file_path)
    file_path.close()
    frag_dict= get_fragments(gene_dict,frag_len=50)                         #call the functions sequentially in the main function
    dissimilar_frag_dict = filter_frags(frag_dict, threshold = 0.7) 
    sentences_dict=get_sentences(dissimilar_frag_dict)
    clean_sentences_dict=clean_dict(sentences_dict)
    write_genes(file_path, clean_sentences_dict)
    print('Number of genes:',len(gene_dict))                                  #print expected outputs
    print('Number of fragments:', len(frag_dict))
    print('Number of the dissimilar fragments:',len(dissimilar_frag_dict))

def read_genes(file_path):
    line=1
    while line <=230:
        header= file_path.readline()                          
        dna_sequence= file_path.readline()
        line +=2 
        header=header.replace("\n","")
        header= header.replace('>', "")
        gene_dict[header] = dna_sequence
    return gene_dict
        
def get_fragments(gene_dict,frag_len):
    header = list(gene_dict.keys())                      #convert the keys in the gene_dict to a list
    for id in header:                                 #for each key in the list
        genes = gene_dict[id]
        
        id=str(id)
        chr= id.split('|')[0]                                #ID part in the key 
        original_range= str(id.split('|')[1])                #unchanged range of the key 
        range1 = int(original_range.split('-')[0])           #first range
        range2 = int(original_range.split('-')[1])           
        temp_range=range1                                    #temporary range will be added 50 on range 1
        
        frag_len=50
        index=0                                              #in the while loop, index will be used as first range to take genes
        while temp_range <= range2:
            sep_genes = genes[index:frag_len]
            sep_genes=sep_genes.replace("\n","")
            if len(sep_genes)<50:
                break
            index+=50
            frag_len+=50
            temp_range = range1+50                           #the range we increased                
            
            new_range= str(range1)+'-'+str(temp_range)       #final range 
            id=chr+'|'+str(new_range)
            range1= int(range1)
            range1 +=50

            frag_dict[id] =sep_genes                         
    return frag_dict

def filter_frags(frag_dict, threshold = 0.7):
    dissimilar_frag_dict=frag_dict.copy()
    
    def get_similarity(s1, s2):  
        a=0                                                  #a is for controlling the gen order
        sim_count=0                                          #to count the similarity of sequences
        while a<50: 
            if s1[a]== s2[a]:                                # if the two sequences are similar
                sim_count +=1                              
                a +=1
            else:
                a +=1
        return sim_count/len(s1)                             #rate of similarity  
    
    original_sequences=list(frag_dict.values())
    for i in range(0,len(frag_dict)):
        sequence1= original_sequences[i]
        index= 1+i
        while index < len(original_sequences):
            sequence2= original_sequences[index]
            similarity = get_similarity(sequence1,sequence2)
            index +=1
            
            if similarity >= threshold: 
                key=(list(dissimilar_frag_dict.keys())[list(dissimilar_frag_dict.values()).index(sequence2)])  #to take the key of the value of sequence2
                del dissimilar_frag_dict[key]                   #first one will be kept,second one will be deleted
    return dissimilar_frag_dict
  

def get_sentences(dissimilar_frag_dict):
    sentences_dict={}
    dna_sequence=list(dissimilar_frag_dict.values())
    k=0
    def generate_kmers(seq, k):  
        temp_list=[]
        k=0
        while k <= 46:
            new_sequence= seq[k:k+4]                          #we seperated the sequence and take it as quadruples
            temp_list.append(new_sequence)                   
            k +=1
        return temp_list 
        
    for i in dna_sequence:
        temp_list=generate_kmers(i,k) 
        temp_list = " ".join(temp_list)
        key=(list(dissimilar_frag_dict.keys())[list(dissimilar_frag_dict.values()).index(i)])        #to take the key
        sentences_dict[key] = temp_list                                         #Combines values in the temp_list and keys
    return sentences_dict


def clean_dict(sentences_dict):
    clean_sentences_dict = sentences_dict.copy()                  #copy sentences_dict to clean_sentences_dict
     
    for i in list(sentences_dict.values()):                     #for each value
        
        def clean_sentence(sentence):
            index =0                                           
            temp_list=[]
            sentence=sentence.replace(" ","")                     #to delete the blanks
            while index <188:
                sentence=list(sentence)
                temp_gene=sentence[index:index +4]                 
                index +=4
                temp_list.append(temp_gene)
            
            for a in temp_list:
                c=temp_list.index(a)                          
                for b in temp_list[c+1:]:
                    if a==b:                                  #if the quadruples are same, we extract one of them
                        temp_list.pop(temp_list.index(b))

            newtemp_list=[]
            for seq in temp_list:
                seq=''.join(seq)                             #to delete the blanks
                newtemp_list.append(seq)                     #add new list
            newtemp_list=" ".join(newtemp_list)              #to add blanks
            return newtemp_list
      
        newtemp_list=clean_sentence(i)  
        key=(list(clean_sentences_dict.keys())[list(clean_sentences_dict.values()).index(i)])     #to take the key
        clean_sentences_dict[key] = newtemp_list                     #Combines values in the newtemp_list and keys
    return clean_sentences_dict    
                                     
def write_genes(file_path, clean_sentences_dict):
    titles=['FRAGMENT ID','SENTENCE','SENTENCE LENGHT','NUMBER OF WORDS']
    final_list=[]
    for k,v in clean_sentences_dict.items():             #k for keys and v for values
        temp_list=[]                                     #temporary list to add a row, to the final list
        count=0                                          #to count the number of words in a sequence
        temp_list.append(k)
        temp_list.append(v)
        temp_list.append(len(v))
            
        for j in list(v):
            if j != " ":                                   #if j equals to character, count will be added
                count +=1
        temp_list.append(int(count/4))                     #we divided 4 because the number of quadruples are required
        final_list.append(temp_list) 
    file= open('output.csv','w', newline='')                #write in a output file
    writer =csv.writer(file)
    writer.writerow(titles)
    writer.writerows(final_list)
    file.close()
main()      
         