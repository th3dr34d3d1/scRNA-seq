import matplotlib.pyplot as plt
from matplotlib import pyplot as pllt

#x-axis title representing data obtained at elapsed time intervals, in hours, 0, 1, 2, 4, and 24 hours respectively
xaxislabel = ['t0', 't1', 't2', 't4', 't24']

#yeast, pseudohyphae, hyphae average % representation from cultures 1 and 2
yeastave = [1, .23146, .00909, 0, 0]
pseudoave = [0, .736156, .886265, .81059, 0]
hyphaeave = [0, .01515, .10646, .18942, 1]

#yeast upper and lower values from cultures 1 & 2
yeast_lower_val = [.99, .06897, 0, 0, 0]
yeast_upper_val = [1.01, .39394, .01818, 0, 0]
#range represented as error
yeast_lower_err = [v-yeast_lower_val[i] for i,v in enumerate(yeastave)]
yeast_upper_err = [yeast_upper_val[i]-v for i,v in enumerate(yeastave)]

#pseudohyphae counts from cultures 1 & 2
pseudo_lower_val = [0, .57576, .83636, .68966, 0]
pseudo_upper_val = [0, .89655, .93617, .93151, 0]
#range represented as error
pseudo_lower_err = [v-pseudo_lower_val[i] for i,v in enumerate(pseudoave)]
pseudo_upper_err = [pseudo_upper_val[i]-v for i,v in enumerate(pseudoave)]

#hyphae counts from cultures 1 & 2
hyphae_lower_val = [0, 0, .06383, 0.06849, .99]
hyphae_upper_val = [0, 0.0303, .14545, .31034, 1.01]
#range represented as error
hyphae_lower_err = [v-hyphae_lower_val[i] for i,v in enumerate(hyphaeave)]
hyphae_upper_err = [hyphae_upper_val[i]-v for i,v in enumerate(hyphaeave)]


#raw counts from cultures 1 and 2 represented as error
asymmetricyeast_error = [yeast_lower_err, yeast_upper_err]
asymmetricpseudo_error = [pseudo_lower_err, pseudo_upper_err]
asymmetrichyphae_error = [hyphae_lower_err, hyphae_upper_err]



#width of bars: can also be len(x) sequence
width = 0.35
 
fig, ax = plt.subplots()
ax.bar(xaxislabel, yeastave, width, yerr=asymmetricyeast_error, label='Yeast')
ax.bar(xaxislabel, pseudoave, width, yerr=asymmetricpseudo_error, bottom=yeastave,label='Pseudohyphae')
ax.bar(xaxislabel, hyphaeave, width, yerr=asymmetrichyphae_error, bottom=[sum(x) for x in zip(yeastave, pseudoave)], label='Hyphae')

#axes labels and title
ax.set_ylabel('cell state count/total')
ax.set_xlabel('elapsed time (hrs)')
ax.set_title('Yeast, Pseudo, and Hyphae distribution @ 30deg RPMI')
ax.legend()
plt.show()
