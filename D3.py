import json

def block(name, *args):
	if len(args)==0:
		return {"name": name}
	else:	
		return {"name": name, "children": args}






output = block("ZOO", block("Mamals", block("Elephants"), block("Zebras")), block ("Birds", block("Hummingbirds"), block("Flamingos")), block("Lizards", block("Geckos"), block("Chameleons")))

with open("flare.json", "w") as f:
	json.dump(output, f)
