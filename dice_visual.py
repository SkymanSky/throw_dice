from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die

#D6 oluştur.

die_1=Die()
die_2=Die()

#Bazı atışlar yap ve sonucu bir listede sakla.
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

#Sonuçları analiz et.
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides

for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#Sonuçları görselleştir.
x_values=list(range(2,max_result+1))
data= [Bar(x=x_values,y=frequencies)]
x_axis_config={'title':'Sonuç','dtick':1}
y_axis_config={'title':'Sonucun Frekansı'}
my_layout=Layout(title='İki D6 yı 1000 kez atmanın sonuçları',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_d6.html')

#print(frequencies)
