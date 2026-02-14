import pandas as pd


# panda : Biblio standard pour importer les csv

def load(path: str) -> pd.DataFrame | None:
    """
    Charge un fichier CSV dans un DataFrame pandas et affiche ses dimensions.

    Cette fonction vérifie l'extension du fichier, tente de le lire et gère
    les erreurs courantes de lecture ou d'accès.

    Args:
        path (str): Le chemin relatif ou absolu vers le fichier .csv à charger.

    Returns:
        pd.DataFrame | None: Un objet DataFrame contenant les données du CSV
                             en cas de succès, sinon None.

    Raises:
        AssertionError: Si le fichier ne possède pas l'extension '.csv'.
    """
    try:
        # ici read_csv cree un "Dataframe" (un tab de données)
        # Il faut lassigner a une variable pour taffer avec

        if not path.endswith(".csv"):
            raise AssertionError("Wrong Extension Format")
        tab_data = pd.read_csv(path)
        # pour les dimensions on utilise shape comme module precedent
        # (comme un attribut)
        print(f"Loadding dataset of dimensions {tab_data.shape}")

        return tab_data

    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
