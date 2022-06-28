import csv

class Votes:
    votes = {}
    
    def add_vote(self, vote:str):
        if vote in self.votes:
            self.votes.update({vote: self.votes[vote]+1})
        else:
            self.votes[vote] = 1

    def write_results_to_file(self, filename: str):
        # put them in descending order
        with open(filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames= ['Submission', 'Number of Votes'])
            writer.writeheader()
            writer.writerows(self.votes)
    