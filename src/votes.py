import csv

class Votes:
    votes = {}
    
    def add_vote(self, vote:str):
        if vote in self.votes:
            self.votes.update({vote: self.votes[vote]+1})
        else:
            self.votes[vote] = 1

    def write_results_to_file(self, filename: str):
        with open(filename, 'w') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in self.votes.items():
                writer.writerow([key, value]) 
    
    def print(self):
        print(self.votes)

    