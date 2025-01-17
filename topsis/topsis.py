import numpy as np

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = data
        self.weights = weights
        self.impacts = impacts

    def normalise(self):
        total_sum = np.sum(self.data**2, axis=0)
        norm_mat = self.data / np.sqrt(np.sqrt(total_sum))
        return norm_mat
    
    def weighted_normalise(self, norm_mat):
        weighted_mat = norm_mat * self.weights
        return weighted_mat

    def find_ideal_solution(self, weighted_mat):
        ideal_best = []
        ideal_worst = []
        
        for i, impact in enumerate(self.impacts):
            if impact == "+":
                ideal_best.append(np.max(weighted_mat[:, i]))
                ideal_worst.append(np.min(weighted_mat[:, i]))
            else:
                ideal_best.append(np.min(weighted_mat[:, i]))
                ideal_worst.append(np.max(weighted_mat[:, i]))

        return np.array(ideal_best), np.array(ideal_worst)
    

    def calculate_distances(self, weighted_mat, ideal_best, ideal_worst):
        dist_to_ideal_best = np.sqrt(np.sum((weighted_mat - ideal_best)**2, axis=1))
        dist_to_ideal_worst = np.sqrt(np.sum((weighted_mat - ideal_worst)**2, axis=1))
        return dist_to_ideal_best, dist_to_ideal_worst
    
    def calculate_scores(self, dist_to_ideal_best, dist_to_ideal_worst):
        scores = dist_to_ideal_worst / (dist_to_ideal_best + dist_to_ideal_worst)
        return scores
    
    def rank(self, scores):
        norm_mat = self.normalise()
        weighted_mat = self.weighted_normalise(norm_mat)
        ideal_best, ideal_worst = self.find_ideal_solution(weighted_mat)
        dist_to_ideal_best, dist_to_ideal_worst = self.calculate_distances(weighted_mat, ideal_best, ideal_worst)
        scores = self.calculate_scores(dist_to_ideal_best, dist_to_ideal_worst)
        rankings = np.argsort(-scores) + 1
        return rankings, scores
