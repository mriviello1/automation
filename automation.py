


#run the jewel; you can also use system arguments to take input from user
#jackhmmer --domtblout <output-file.tblout> <query-input-file.fasta> <target-input-file.fasta>


#Calculate Query coverage from Jackhmmer alignments/Jackhmmer output, and sort them if needed:

#awk '{$1 = ($17-$16)/$6}1' <output-file.tblout> | sort -nr -k 11 | column -t > <new-output-file.tblout>

#parse Proteome-Drugbank merged sequences;
python3
Import Bio
From Bio Import SeqIO
#Import whateverdependency is required to parse jackhmmer, if in fact you will use the name hmm parser available in biopython


#THIS IS INDEXING THE SEQUENCES
SeqIO.to_dict(SeqIO.parse("lomento2.fasta", "fasta")


#THIS IS SUPPOSED TO BE CODE TO PARSE JACKHMMER OUTPUT
#Parse <new-output-file.tblout>
#we're keeping 3 columns; the query ID, target ID and the query coverage, which was calculated above
#output: <ParsedJackhmmerOutput.tblout>


#Iterate over dictionary and print Id and ID value (?)
#for key in indexedProteomeAndDrugBankFile:
    #if key in ParsedJackhmmerOutput:
        #print key, indexedProteomeAndDrugBankFile[value]



 #take print function output as argument
 #touch(print) #idk the best way to write this at the moment

#Question: How do I "get the pairs" and cat newfile or touch newfile?
#Dealing with duplicates in drugbank file
#going from pairs to MSAs, do I really need to using sort -nr -k? I would assume that, if multiple target IDs exist in the parsed jackhmmer output, I could match those up and append to the existing file that has stored other sequences aligning to it, and name the files with a nomenclature that allows this to happen easily. Lots of different ways to solve these various thing I'm sure


#or we can just take them out lol as we don't actually need them when indexing because they already exist 
 #below is a possible solution
#>>> from collections import OrderedDict
#>>> list(OrderedDict.fromkeys('abracadabra'))
#['a', 'b', 'r', 'c', 'd']

#^this is probably going to be slow. This keeps it in the original order

#better solution
#list(set(source_list))

#better solution as well
#def remove_duplicates(l):
    #return list(set(l))


















