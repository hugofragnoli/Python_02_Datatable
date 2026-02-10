import pandas as pd


# panda : Biblio standard pour importer les csv

def load(path: str) -> Dataset: # (you have to
# adapt the type of return according to your library)
    """
    Docstring pour load
    
    :param path: Description
    :type path: str
    :return: Description
    :rtype: Not defined yet bro
    """
    try:
        # ici read_csv cree un "Dataframe" (un tab de données)
        # Il faut lassigner a une variable pour taffer avec
        
        if not path.endswith(".csv"):
            raise AssertionError("Wrong Extension Format")
        tab_data = pd.read_csv(path)
        # pour les dimensions on utilise shape comme module precedent
        # (comme un attribut)
        print(f"Dimensions du tableau : {tab_data.shape}")

        return tab_data


    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
