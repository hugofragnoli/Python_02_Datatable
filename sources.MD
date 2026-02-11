## DataFrame

Un DataFrame est une structure de données bidimensionnelle étiquetée, avec des colonnes de types potentiellement différents. On peut le comparer à une feuille de calcul, une table SQL ou un dictionnaire d'objets Series. C'est généralement l'objet pandas le plus utilisé. Comme Series, DataFrame accepte de nombreux types de données d'entrée :

Dictionnaire de tableaux 1D, de listes, de dictionnaires ouSeries

Tableau NumPy 2D

ndarray structuré ou enregistrement

UNSeries

Un autreDataFrame

Outre les données, vous pouvez éventuellement fournir des arguments d'index (étiquettes de lignes) et de colonnes (étiquettes de colonnes). Si vous spécifiez un index et/ou des colonnes, vous garantissez l'index et/ou les colonnes du DataFrame résultant. Ainsi, un dictionnaire de Series associé à un index spécifique exclura toutes les données ne correspondant pas à l'index fourni.

Si les étiquettes des axes ne sont pas fournies, elles seront construites à partir des données d'entrée selon des règles de bon sens.

source https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
https://gvallverdu.gitbooks.io/python_sciences/content/pandas_capp.html
https://pandas.pydata.org/docs/reference/general_functions.html
