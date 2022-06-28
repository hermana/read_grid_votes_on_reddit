import csv

class Votes:
    votes = {}
    
    def add_vote(self, vote:str):
        if vote in self.votes:
            self.votes.update({vote: self.votes[vote]+1})
        else:
            self.votes[vote] = 1

    def write_results_to_file(self, filename: str):
        file = open(filename, 'w+', newline ='') 
        with file:     
            write = csv.writer(file) 
            write.writerows(self.votes) 

    