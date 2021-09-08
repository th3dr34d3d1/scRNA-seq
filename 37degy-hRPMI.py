import matplotlib.pyplot as plt
from matplotlib import pyplot as pllt

#x-axis title
xaxislabel = ['t0', 't1', 't2', 't4', 't24']

#yeast, pseudohyphae, hyphae average % representation from cultures 1 and 2
yeastave = [1, .083333, 0, 0, 0]
pseudoave = [0, .66667, 0, 0, .025862]
hyphaeave = [0, .25, 1, 1, .974138]


#yeast upper and lower values from cultures 1 & 2
yeast_lower_val = [.99, .083333, 0, 0, 0]
yeast_upper_val = [1.01, .08333, 0, 0, 0]
#range represented as error
yeast_lower_err = [v-yeast_lower_val[i] for i,v in enumerate(yeastave)]
yeast_upper_err = [yeast_upper_val[i]-v for i,v in enumerate(yeastave)]

#pseudohyphae counts from cultures 1 & 2
pseudo_lower_val = [0, .66667, 0, 0, 0]
pseudo_upper_val = [0, .66667, 0, 0, 0.051724]
#range represented as error
pseudo_lower_err = [v-pseudo_lower_val[i] for i,v in enumerate(pseudoave)]
pseudo_upper_err = [pseudo_upper_val[i]-v for i,v in enumerate(pseudoave)]

#hyphae counts from cultures 1 & 2
hyphae_lower_val = [0, .25, 1, 1, .948276]
hyphae_upper_val = [0, .25, 1, 1, 1]
#range represented as error
hyphae_lower_err = [v-hyphae_lower_val[i] for i,v in enumerate(hyphaeave)]
hyphae_upper_err = [hyphae_upper_val[i]-v for i,v in enumerate(hyphaeave)]


#raw counts from cultures 1 and 2 represented as error
asymmetricyeast_error = [yeast_lower_err, yeast_upper_err]
asymmetricpseudo_error = [pseudo_lower_err, pseudo_upper_err]
asymmetrichyphae_error = [hyphae_lower_err, hyphae_upper_err]


#width of bars
width = 0.35

fig, ax = plt.subplots()

ax.bar(xaxislabel, yeastave, width, yerr=asymmetricyeast_error, label='Yeast')
ax.bar(xaxislabel, pseudoave, width, yerr=asymmetricpseudo_error, bottom=yeastave, label='Pseudohyphae')
ax.bar(xaxislabel, hyphaeave, width, yerr=asymmetrichyphae_error, bottom=[sum(x) for x in zip(yeastave,pseudoave)], label='Hyphae')


#axes labels and title
ax.set_ylabel('cell state count/total')
ax.set_xlabel('elapsed time (hrs)')
ax.set_title('Yeast, Pseudo, and Hyphae distribution @ 37deg RPMI')
ax.legend()
plt.show()
