# Reto1-Wind

Realizado por:
- Lucian Andrei Farcas
- Daniel Durán Fernandez
- Carlos Gutierrez Palmeiro
- Mario Rodriguez Serrano
- Fernando Lorente Calvo

# Afrontamiento del problema

Hemos calculado las coordenadas a partir de las pistas y de las fórmulas disponibles y hemos comprobado que ese es el molino correcto ya que tiene una velocidad superior a su máximo. Además, hemos recogido todos los molinos en un archivo [windmills](./windmills.xml), parseamos todos los datos con la clase [myparser](./myparser.py) y procedemos a buscar dentro de la propia clase [main](./main.py) todos los molinos que tienen una velocidad superior a su límite. El resultado en ambos métodos es el molino 987 por lo que podemos afirmar que es el defectuoso.
