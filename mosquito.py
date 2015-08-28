import pandas
from matplotlib import pyplot as plt
plt.show()
data= pandas.read_csv('mosquito_data.csv')
print plt.plot(data['year'], data['mosquitos'])


#print data['rainfall'][data['rainfall']>200]
#print data.mean()
#
#for temp in data['temperature']:
#    celsius= (temp-32)/1.8
#    print celsius

#data= open("mosquito_data.csv")
#headers= data.readlines()
#print headers

#data= open("mosquito_data.csv")
#for line in data:
#    columns= line.split(',')
#    print columns 
#print data