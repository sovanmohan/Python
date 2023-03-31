release_year_dict={"Thriller":"1982","Back in black":"1980","The dark side of the moon":"1973","The bodyguard":"1992","Bat out of the hell":"1997","Their greatest hits(1971-1975)":"1976","Saturday Night Fever":"1997","Rumours":"1977"}
print(release_year_dict.keys())
print(release_year_dict.values())
del(release_year_dict["The bodyguard"])
release_year_dict["metered production"]="1967"
print(release_year_dict)
print("Saturday Night Fever" in release_year_dict)
