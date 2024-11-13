import matplotlib.pyplot as plt

def plot_data(fcfs_data, sjf_data):
  # Data for plotting
  labels = ['Average Waiting Time', 'Average Turnaround Time']
  fcfs_data = list(fcfs_data)
  sjf_data = list(sjf_data)

  # Create a plot of the the plots to compare the algorithms
  x = range(len(labels))
  width = 0.40

  _, ax = plt.subplots()
  ax.bar(x, fcfs_data, width, label='FCFS')
  ax.bar([i + width for i in x], sjf_data, width, label='SJF')

  ax.set_ylabel('Time')
  ax.set_title('Comparison of FCFS and SJF Algorithms')

  ax.set_xticks([i + width / 2 for i in x])
  ax.set_xticklabels(labels)

  ax.legend()
  plt.show()