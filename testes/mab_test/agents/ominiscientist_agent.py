
import numpy as np

class OmniscientAgent( object ):
    def __init__( self, prob_list ):
        self.prob_list = prob_list

    def pull( self, bandit_machine):
        if np.random.random() < self.prob_list[bandit_machine]:
            reward = 1
        else:
            reward = 0

        return reward    

# probability of having a positive result
prob_list = [0.3, 0.8]

# experiment parameters
trials = 1000
episodes = 200

#agent
bandit = OmniscientAgent( prob_list )

prob_reward_array = np.zeros( len(prob_list))
accumulated_reward_array = list()
avg_accumulated_reward_array = list()
for episode in range(episodes):
    reward_array = np.zeros(len(prob_list))
    bandit_array = np.full( len( prob_list), 1.0e-5 )
    accumulated_reward = 0
    for trial in range( trials ):
            
        #agent - choise
        bandit_machine = np.argmax( prob_list )

        #agent - reward
        reward = bandit.pull(bandit_machine)

        #agent - keep reward
        reward_array[bandit_machine] += reward
        bandit_array[bandit_machine] += 1
        accumulated_reward += reward

    prob_reward_array += reward_array / bandit_array
    accumulated_reward_array.append( accumulated_reward )
    avg_accumulated_reward_array.append(np.mean(accumulated_reward_array))

prob01 = 100*np.round(prob_reward_array[0] / episodes, 2)
prob02 = 100*np.round(prob_reward_array[1] / episodes, 2)

print(f'\nProb Bandit 01: {prob01}% - Prob Bandit 02: {prob02}%')
print(f'\nAVG accumulated reward: :{np.mean(avg_accumulated_reward_array)}%')
