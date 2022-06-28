class Votes:
    votes = {}
    
    def add_vote(self, vote:str):
        if vote in self.votes:
            self.votes.update({vote: self.votes[vote]+1})
        else:
            self.votes[vote] = 1

    