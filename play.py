from game import Game
from funcs import playMatchesBetweenVersions
import loggers as lg

env = Game()
scores, _, points, sp_scores = playMatchesBetweenVersions(env, 4, -1, 17, 1, lg.logger_tourney, 0)
print('\nSCORES')
print(scores)
print('\nSTARTING PLAYER / NON-STARTING PLAYER SCORES')
print(sp_scores)