#Vamos a importar la biblioteca Pandas y la llamamos pd
import pandas as pd
psg_players = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'],
    #index=[1,7,10,30]
)
psg_dict = { 1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}
psg_players_dict = pd.Series(psg_dict)
#print(psg_players)
print(psg_players_dict)
print(psg_players_dict[7])
print(psg_players_dict[0:3])
dict = {
  'jugador':['Navas','Mbape','Neymar','Messi'],
   'Altura':[183.0,170.0,170.0,165.0],
   'Goles':[2,200,150,200]}
#crear un Dataframe con el dicionario y indice personalizados
df= pd.DataFrame(dict,index=[1,7,10,30])
#imprimir el Dataframe
print(df)