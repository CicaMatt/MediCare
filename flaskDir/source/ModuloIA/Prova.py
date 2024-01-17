import random
import math
from deap import base, creator, tools, algorithms
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from flaskDir.source.ModuloIA.DataPreparation import df,predict,train

# Definire la funzione di fitness (accuratezza del modello KNN)
def fitness_function(K):
    knn = KNeighborsClassifier(n_neighbors=K)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_val)
    precision = precision_score(y_val, y_pred)
    return precision

# Definire la funzione obiettivo per DEAP (massimizzare l'accuratezza)
def objective_function(chromosome):
    K = chromosome[0]# Un solo gene rappresenta il valore di K
    return fitness_function(K),  # Massimizzare l'accuratezza è equivalente a minimizzare l'opposto

#Crossover personalizzato
def crossover(parent1,parent2):
    child=tools.cxBlend(parent1,parent2, alpha=0.5)
    child[0][0]=math.ceil(child[0][0])
    if child[0][0]<0:
        child[0][0]=abs(child[0][0])
    elif child[0][0]==0:
        child[0][0]=random.randint(1,40)
    return child

def mutation(chromosome):
    newChromosome=tools.mutUniformInt(chromosome,5,40,0.1)
    newChromosome[0][0]=math.ceil(newChromosome[0][0])
    return newChromosome

if __name__ == "__main__":

    # Suddividere i dati
    trainset=df[train]
    X_train, X_val, y_train, y_val = train_test_split(trainset, predict, test_size=0.2, random_state=42)

    # Inizializzare DEAP
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_int", random.randint,1,40)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", objective_function)
    toolbox.register("mate", crossover)
    toolbox.register("select", tools.selTournament, tournsize=4)
    toolbox.register("mutate", mutation)


    # Eseguire l'algoritmo genetico con DEAP
    population = toolbox.population(n=50)
    algorithms.eaMuPlusLambda(population, toolbox, mu=125, lambda_=250, cxpb=0.7, mutpb=0.3, ngen=20, stats=None, halloffame=None, verbose=True)

    # Trovare il miglior individuo
    best_individual = tools.selBest(population, k=1)[0]
    best_K = best_individual[0]
    print(f"Il miglior valore di K trovato è: {best_K}")