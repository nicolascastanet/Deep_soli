exemple d'appel du script:

python importation/main.py --data_path data --nb_frames 40 --mode cross_user --channel 4

nb_frames : nombre de frames des s�quences lors du subsampling (on ajoute des frames nuls ou on supprime des frames pour ramener toutes les s�quences � la m�me taille)
nb_channel : 4 pour Soli
mode : mode 'cross user' -> 11x25x10 = 2750 sequences (10 users) utilis� dans le papier Soli
       mode 'single user' -> 11x50x5 = 2750 sequences (1 users) utilis� pour la reconnaissance personalis�e


output : fichiers pickle

	import pickle
	soli_data = pickle.load( open( "data_numpy.p", "rb" ) )
	soli_labels = pickle.load( open( "labels_numpy.p", "rb" ) )

dim = (nb_geste, nb_sessions, nb_instances, nb_channel, nb_frames, 32, 32)