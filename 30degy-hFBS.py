import matplotlib.pyplot as plt
from matplotlib import pyplot as pllt

#x-axis title representing data obtained at elapsed time intervals, in hours, 0, 1, 2, 4, and 24 hours respectively
xaxislabel = ['t0', 't1', 't2', 't4', 't24']


#yeast, pseudohyphae, hyphae average % representation from cultures 1 and 2
yeastave = [1, .422575, .121325, .247335, .91005]
pseudoave = [0, .577425, .80544, .688225, .066795]
hyphaeave = [0, 0, .073235, .06443, .023065]


#yeast upper and lower values from cultures 1 & 2
yeast_lower_val = [.99, .21053, .02778, .11111, .86408]
yeast_upper_val = [1.01, .63462, .21487, .38356, .95602]
#range represented as error
yeast_lower_err = [v-yeast_lower_val[i] for i,v in enumerate(yeastave)]
yeast_upper_err = [yeast_upper_val[i]-v for i,v in enumerate(yeastave)]

#pseudohyphae counts from cultures 1 & 2
pseudo_lower_val = [0, .36538, .69421, .56164, 0.0365]
pseudo_upper_val = [0, .78947, .91667, .81481, 0.09709]
#range represented as error
pseudo_lower_err = [v-pseudo_lower_val[i] for i,v in enumerate(pseudoave)]
pseudo_upper_err = [pseudo_upper_val[i]-v for i,v in enumerate(pseudoave)]

#hyphae counts from cultures 1 & 2
hyphae_lower_val = [0, 0, .05556, .05479, .0073]
hyphae_upper_val = [0, 0, .09091, .07407, .03883]
#range represented as error
hyphae_lower_err = [v-hyphae_lower_val[i] for i,v in enumerate(hyphaeave)]
hyphae_upper_err = [hyphae_upper_val[i]-v for i,v in enumerate(hyphaeave)]


#raw counts from cultures 1 and 2 represented as error
asymmetricyeast_error = [yeast_lower_err, yeast_upper_err]
asymmetricpseudo_error = [pseudo_lower_err, pseudo_upper_err]
asymmetrichyphae_error = [hyphae_lower_err, hyphae_upper_err]



#width of the bars
width = 0.35



fig, ax = plt.subplots()

ax.bar(xaxislabel, yeastave, width, yerr=asymmetricyeast_error, ecolor='red', label='Yeast')
ax.bar(xaxislabel, pseudoave, width, yerr=asymmetricpseudo_error, bottom=yeastave, label='Pseudohyphae')
ax.bar(xaxislabel, hyphaeave, width, yerr=asymmetrichyphae_error, ecolor='red', bottom=[sum(x) for x in zip(yeastave, pseudoave)], label='Hyphae')

#axes labels and title
ax.set_ylabel('cell state count/total')
ax.set_xlabel('elapsed time (hrs)')
ax.set_title('Yeast, Pseudo, and Hyphae distribution @ 30deg FBS')
ax.legend()
plt.show()
