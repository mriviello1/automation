#run the jewel; you can also use system arguments to take input from user
#I'd like to be able to feed it in the input files with sysarg tooo
jackhmmer --domtblout <output-file.tblout> <query-input-file.fasta> <target-input-file.fasta> 



#Calculate Query coverage from Jackhmmer alignments/Jackhmmer output, and sort them if needed:
awk '{$1 = ($17-$16)/$6}1' <output-file.tblout> | sort -nr -k 11 | column -t > <new-output-file.tblout>


python3 
Import Bio 
From Bio Import SeqIO
Import #whateverdependency is required to parse jackhmmer, if in fact you will use the name hmm parser available in biopython; alternatively you can parse it with a one-liner as all's you need is the fields containing the IDs


REMOVING DUPLICATES FROM DRUGBANK-PROTEOME-MERGED

def to_dict_remove_dups(sequences):
    return {record.id: record for record in sequences}

print(to_dict_remove_dups(SeqIO.parse("indexedProteomeAndDrugtargetFile.fa", "fasta")))


THIS IS INDEXING THE DRUGBANK-PROTEOME-MERGED  
SeqIO.to_dict(SeqIO.parse("indexedProteomeAndDrugtargetFile.fa", "fasta")


#PARSE JACKHMMER OUTPUT HERE WITH SED/GREP
#Parse <jackhmmer-output.tblout>
#we're keeping 3 columns; the query ID, target ID and the query coverage, which was calculated above
#output: <ParsedJackhmmerOutput.tblout>


#Iterate over dictionary and print key + value
for key in indexedProteomeAndDrugBankFile:
    if key in ParsedJackhmmerOutput:
        print key, indexedProteomeAndDrugBankFile[value]



 #take print function output as argument
 touch(print) #idk the best way to write this at the moment

